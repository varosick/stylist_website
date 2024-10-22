from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.decorators.cache import cache_page

from products.views import (CategoryDetailView, GuideDetailView, IndexView,
                            ProductDetailView)

app_name = 'products'
urlpatterns = [
    path('', cache_page(60*60*24)(IndexView.as_view()), name='index'),
    path('products/<slug:category_slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('products/<slug:category_slug>/<slug:product_slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('guides/<slug:guide_slug>/', GuideDetailView.as_view(), name='guide_detail'),

    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)