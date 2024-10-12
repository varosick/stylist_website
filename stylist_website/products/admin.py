from django.contrib import admin

from products.models import (CarouselImage, Guide, NotUserReview, Product,
                             ProductCategory, ProductDetail, Question)


@admin.register(ProductCategory)
class Admin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    ordering = ('name',)
    search_fields = ('name',)

@admin.register(Product)
class Admin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_display_links = ('name',)
    ordering = ('category', 'id')
    search_fields = ('name', 'category__name')
    list_filter = ('category__name',)

@admin.register(Question)
class Admin(admin.ModelAdmin):
    list_display = ('question', 'category')
    ordering = ('category', )
    search_fields = ('question', 'category__name')
    list_filter = ('category__name',)

@admin.register(ProductDetail)
class Admin(admin.ModelAdmin):
    list_display = ('title', 'product__name', 'product__category__name', 'is_include')
    list_display_links = ('title',)
    ordering = ('product__category', 'product__id', '-is_include')
    search_fields = ('title', 'product__name', 'product__category__name')
    list_filter = ('product__category__name', 'product__name')

@admin.register(Guide)
class Admin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    ordering = ('name',)
    search_fields = ('name',)


@admin.register(NotUserReview)
class Admin(admin.ModelAdmin):
    search_fields = ('reviewer_first_name', 'reviewer_last_name')
    ordering = ('date', )


@admin.register(CarouselImage)
class Admin(admin.ModelAdmin):
    list_display = ('id', 'category__name', )
    list_display_links = ('id', 'category__name')
    ordering = ('category', 'id')
    search_fields = ('category__name', )
    list_filter = ('category__name',)