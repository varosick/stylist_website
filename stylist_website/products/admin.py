from django.contrib import admin
from products.models import ProductCategory, Product, Question, ProductDetail, Guide, NotUserReview, CarouselImage

@admin.register(ProductCategory)
class Admin(admin.ModelAdmin):
    pass

@admin.register(Product)
class Admin(admin.ModelAdmin):
    pass

@admin.register(Question)
class Admin(admin.ModelAdmin):
    pass

@admin.register(ProductDetail)
class Admin(admin.ModelAdmin):
    pass

@admin.register(Guide)
class Admin(admin.ModelAdmin):
    pass

@admin.register(NotUserReview)
class Admin(admin.ModelAdmin):
    pass

@admin.register(CarouselImage)
class Admin(admin.ModelAdmin):
    pass