
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404
from django.views.generic.edit import FormMixin
from django.views.generic.list import ListView
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DetailView, TemplateView
from django.contrib import messages
from users.models import User, Review, UserServices, UserGuides, EmailVerification
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm, ReviewAddForm, \
    CustomPasswordChangeForm, UserForgotPasswordForm, UserSetNewPasswordForm
from django.contrib.auth.mixins import LoginRequiredMixin
from products.models import NotUserReview
from django.core.cache import cache
class UserLoginView(LoginView):
    template_name = 'profile/login.html'
    form_class = UserLoginForm

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Авторизация'
        return context_data

    def form_invalid(self, form):
        # Добавляем сообщение об ошибке
        messages.error(self.request, "Имя пользователя или пароль введены неверно")
        return super().form_invalid(form)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('users:profile')
        return super().dispatch(request, *args, **kwargs)


class UserRegistrationView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'profile/registration.html'
    success_url = reverse_lazy('users:login')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Регистрация'
        return context_data

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('users:profile')
        return super().dispatch(request, *args, **kwargs)


class UserProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'profile/profile.html'
    login_url = reverse_lazy('users:login')
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        queryset = self.get_queryset()
        user = queryset.get(id=self.request.user.id)
        return user

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['password_change_form'] = CustomPasswordChangeForm(user=self.request.user)
        context_data['profile_form'] = self.get_form()
        context_data['title'] = 'Профиль'
        return context_data

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        profile_form = self.get_form()
        if 'first_name' in self.request.POST:
            if profile_form.is_valid():
                user = profile_form.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Изменения успешно внесены.')
                return self.form_valid(profile_form)
            else:
                messages.error(request,'Данные были введены неверно.')
                return self.form_invalid(profile_form)

        elif 'old_password' in request.POST:
            password_form = CustomPasswordChangeForm(user=request.user, data=request.POST)
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Ваш пароль был успешно изменён.')
                return self.form_valid(password_form)
            else:
                messages.error(request, 'Ваши пароли не совпадают или действующий пароль введен неверно.')
                return redirect('users:profile')

class UsersReviewsView(FormMixin, ListView):
    model = Review
    template_name = 'profile/reviews.html'
    form_class = ReviewAddForm
    success_url = reverse_lazy('users:reviews')
    context_object_name = 'reviews'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['not_user_reviews'] =  cache.get_or_set('not_user_reviews', NotUserReview.objects.all(), 30)
        context_data['title'] = 'Отзывы'
        return context_data

    def get_queryset(self):
        return Review.objects.filter(is_approved=True)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        # Сохраняем данные формы, создавая новый объект UserServices
        review_add_form = form.save(commit=False)
        review_add_form.user = self.request.user
        review_add_form.save()
        messages.success(self.request, 'Спасибо за отзыв! Он будет доступен после проверки')
        return super().form_valid(form)

@login_required
def user_logout(request):
    logout(request)
    return redirect('users:login')


class UserServicesView(LoginRequiredMixin, ListView):
    model = UserServices
    template_name = 'profile/user_services.html'
    login_url = reverse_lazy('users:login')
    success_url = reverse_lazy('users:user_services')
    context_object_name = 'user_services'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Мои услуги'
        return context_data

    def get_queryset(self):
        return UserServices.objects.filter(user=self.request.user)

class UserServiceDetailView(LoginRequiredMixin, DetailView):
    model = UserServices
    template_name = 'profile/service_detail.html'
    login_url = reverse_lazy('users:login')
    success_url = reverse_lazy('users:user_services')
    context_object_name = 'user_service'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = f'Услуга {self.get_object().service}'
        return context_data

    def get_object(self, queryset=None):
        return get_object_or_404(UserServices, user=self.request.user, id=self.kwargs['pk'], payment_status__gt=0)


class UserGuidesView(LoginRequiredMixin, ListView):
    model = UserGuides
    template_name = 'profile/user_guides.html'
    login_url = reverse_lazy('users:login')
    success_url = reverse_lazy('users:user_guides')
    context_object_name = 'user_guides'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Мои гайды'
        return context_data

    def get_queryset(self):
        return UserGuides.objects.filter(user=self.request.user)

class UserGuideDetailView(LoginRequiredMixin, DetailView):
    model = UserGuides
    template_name = 'profile/guide_detail.html'
    login_url = reverse_lazy('users:login')
    success_url = reverse_lazy('users:user_services')
    context_object_name = 'user_guide'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = f'Гайд {self.get_object().guide}'
        return context_data

    def get_object(self, queryset=None):
        return get_object_or_404(UserGuides, guide__slug=self.kwargs['guide_slug'], payment_status=1)

class EmailVerificationView(TemplateView):
    template_name = 'profile/email_verification.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Подтверждение электронной почты'
        return context_data

    def get(self, request, *args, **kwargs):
        code = kwargs['code']
        user = User.objects.get(email=kwargs['email'])
        email_verification = EmailVerification.objects.filter(user=user, code=code)
        if email_verification.exists() and not email_verification.first().is_expired():
            user.is_verified_email = True
            user.save()
            return super(EmailVerificationView, self).get(request, *args, **kwargs)
        else: HttpResponseRedirect(reverse('index'))

class UserForgotPasswordView(SuccessMessageMixin, PasswordResetView):
    """
    Представление по сбросу пароля по почте
    """
    form_class = UserForgotPasswordForm
    template_name = 'profile/recovery.html'
    success_url = reverse_lazy('users:login')
    success_message = 'Письмо с инструкцией по восстановлению пароля отправлена на ваш email'
    email_template_name = 'profile/password_reset_email.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Запрос на восстановление пароля'
        return context_data

    def post(self, request, *args, **kwargs):
        if User.objects.filter(email=request.POST['email']).exists():
            super().post(request, *args, **kwargs)
            return redirect('users:login')
        else:
            messages.error(self.request, 'Пользователь с данной почтой не найден')
            return redirect('users:password_reset')


class UserPasswordResetConfirmView(SuccessMessageMixin, PasswordResetConfirmView):
    """
    Представление установки нового пароля
    """
    form_class = UserSetNewPasswordForm
    template_name = 'profile/user_password_set_new.html'
    success_url = reverse_lazy('users:login')
    success_message = 'Пароль успешно изменен. Можете авторизоваться на сайте.'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Установка нового пароля'
        return context_data


