from django.contrib.sitemaps import Sitemap

from products.models import Product, ProductCategory, Guide


class CategorySitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.9

    def items(self):
        return ProductCategory.objects.all()



class ProductSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.9

    def items(self):
        return Product.objects.all()



class GuideSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.9

    def items(self):
        return Guide.objects.all()

