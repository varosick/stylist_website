from django.core.cache import cache
from django.shortcuts import (get_list_or_404, get_object_or_404, redirect, render)
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin
from django.views.generic.list import ListView

from products.models import (CarouselImage, Guide, Product, ProductCategory,
                             ProductDetail, Question)
from users.forms import ServicePurchaseForm
from users.models import ScheduleDate, UserGuides
from users.tasks import send_emails_guides, send_emails_services


def tr_handler404(request, exception):
    """
    Обработка ошибки 404
    """
    return render(request=request, template_name='errors/error_page.html', status=404, context={
        'title': 'Страница не найдена: 404',
        'error_message': 'К сожалению такая страница была не найдена, или перемещена',
    })


def tr_handler500(request):
    """
    Обработка ошибки 500
    """
    return render(request=request, template_name='errors/error_page.html', status=500, context={
        'title': 'Ошибка сервера: 500',
        'error_message': 'Внутренняя ошибка сайта, вернитесь на главную страницу, отчёт об ошибке мы направим администрации сайта',
    })


def tr_handler403(request, exception):
    """
    Обработка ошибки 403
    """
    return render(request=request, template_name='errors/error_page.html', status=403, context={
        'title': 'Ошибка доступа: 403',
        'error_message': 'Доступ к этой странице ограничен',
    })


class IndexView(ListView):
    """
    Отображение главной страницы с категориями услуг и гайдами.
    """
    model = ProductCategory
    template_name = 'products/index.htm'
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['guides'] = Guide.objects.all()
        context_data['title'] = 'Главная'
        return context_data

    def get_queryset(self):
        return ProductCategory.objects.all()


class CategoryDetailView(ListView):
    """
    Отображение детального представления каждой категории услуг со всем списком, относящихся услуг.
    """
    template_name = 'products/category_detail.html'
    model = Product
    context_object_name = 'products'

    def get_queryset(self):
        return get_list_or_404(Product.objects.order_by('id'), category__slug=self.kwargs['category_slug'])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['category'] = cache.get_or_set(self.kwargs['category_slug'],
                                                    ProductCategory.objects.get(slug=self.kwargs['category_slug']), 30)
        context_data['questions'] = cache.get_or_set(f'question_{self.kwargs['category_slug']}',
                                                     Question.objects.filter(category=context_data['category']), 30)
        context_data['carousel_images'] = cache.get_or_set(f'carousel_{self.kwargs['category_slug']}',
                                                           CarouselImage.objects.filter(
                                                               category=context_data['category']), 30)
        context_data['title'] = context_data['category']
        return context_data


class ProductDetailView(FormMixin, DetailView):
    """
        Отображение детального представления каждой услуги. Обработка формы записи на услугу от клиента.
    """
    model = Product
    template_name = 'products/product_detail.html'
    form_class = ServicePurchaseForm
    success_url = reverse_lazy('users:user_services')
    context_object_name = 'product'

    def get_object(self, **kwargs):
        return get_object_or_404(Product, slug=self.kwargs['product_slug'])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['category'] = self.get_object().category
        context_data['details'] = cache.get_or_set(f'details_{self.kwargs['product_slug']}',
                                                   ProductDetail.objects.filter(
                                                       product__slug=self.kwargs['product_slug']).order_by(
                                                       '-is_include', 'id'), 30)
        context_data['title'] = f'{self.get_object().name} {context_data["category"].name.lower()}'
        return context_data

    def post(self, request, *args, **kwargs):
        # Получаем объект продукта, к которому относится форма
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        # Сохраняем данные формы, создавая новый объект UserServices
        service_purchase = form.save(commit=False)
        service_purchase.user = self.request.user  # Привязываем пользователя
        service_purchase.service = self.object

        # Проверяем наличие даты в ScheduleDate
        if service_purchase.datetime_of_service:
            try:
                sd = ScheduleDate.objects.get(date=service_purchase.datetime_of_service.strftime("%Y-%m-%d"))
                if sd.is_booked:
                    form.add_error('datetime_of_service', 'Выбранная дата уже забронирована.')
                    return self.form_invalid(form)
                sd.is_booked = True
                sd.save()
            except ScheduleDate.DoesNotExist:
                # Если даты нет в ScheduleDate, возвращаем ошибку
                form.add_error('datetime_of_service', 'Вы выбрали неправильную дату. Выберите доступную в календаре.')
                return self.form_invalid(form)

        # Привязываем продукт
        service_purchase.save()
        send_emails_services.delay(service_purchase.id)
        return super().form_valid(form)


class GuideDetailView(DetailView):
    model = Guide
    template_name = 'products/guide_detail.html'
    context_object_name = 'guide'

    def get_object(self, **kwargs):
        return get_object_or_404(Guide, slug=self.kwargs['guide_slug'])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context_data['user_guides'] = UserGuides.objects.filter(user=self.request.user).values_list('guide__id',
                                                                                                        flat=True)
        context_data['title'] = f'{self.get_object().name}'
        return context_data

    def post(self, request, *args, **kwargs):
        guide = self.get_object()
        user = request.user

        # Создаем запись в модели UserGuides
        user_guide = UserGuides.objects.create(
            user=user,
            guide=guide
        )
        user_guide.save()
        send_emails_guides.delay(user_guide.id)
        return redirect('users:user_guides')
