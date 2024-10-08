"""
URL configuration for stylist_website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from django.views.decorators.cache import cache_page

from products.sitemaps import ProductSitemap, CategorySitemap, GuideSitemap

sitemaps = {
    'categories': CategorySitemap,
    'products': ProductSitemap,
    'guides': GuideSitemap,
}

handler403 = 'products.views.tr_handler403' # New
handler404 = 'products.views.tr_handler404' # New
handler500 = 'products.views.tr_handler500' # New


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls', namespace='products')),
    path('', include('users.urls', namespace='users')),
    path('sitemap.xml', cache_page(7 * 60 * 24)(sitemap), {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
