"""
URL configuration for stylist_website project.
"""
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from django.views.decorators.cache import cache_page

from products.sitemaps import CategorySitemap, GuideSitemap, ProductSitemap

#Site Map Configuration
sitemaps = {
    'categories': CategorySitemap,
    'products': ProductSitemap,
    'guides': GuideSitemap,
}

#Error page handlers
handler403 = 'products.views.tr_handler403'
handler404 = 'products.views.tr_handler404'
handler500 = 'products.views.tr_handler500'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls', namespace='products')),
    path('', include('users.urls', namespace='users')),
    path('sitemap.xml', cache_page(7 * 60 * 24)(sitemap), {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
