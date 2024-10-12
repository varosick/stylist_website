from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='media/products/categories/', null=True, blank=True)
    slug = models.SlugField(max_length=128, unique=True)
    preparation_offline = models.TextField(null=True, blank=True)
    preparation_online = models.TextField(null=True, blank=True)
    content_image = models.ImageField(upload_to='media/products/categories/', null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/products/{self.slug}/'

class CarouselImage(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=f'media/products/images_for_carousel/')

    def __str__(self):
        return f'Изображение для карусели категории: {self.category}'


class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    price_czk = models.DecimalField(max_digits=6, decimal_places=2)
    price_eur = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(to=ProductCategory, on_delete=models.PROTECT)
    slug = models.SlugField(max_length=128, unique=True)
    image = models.ImageField(upload_to=f'media/products/products/{slug}', null=True, blank=True)

    def __str__(self):
        return f'{self.name} {self.category.name}'

    def get_absolute_url(self):
        return f'/products/{self.category.slug}/{self.slug}/'


class Question(models.Model):
    question = models.TextField(null=False, blank=False)
    answer = models.TextField(null=False, blank=False)
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.question}'

class ProductDetail(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(null=False, blank=False)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    is_include = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Guide(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    price_czk = models.DecimalField(max_digits=6, decimal_places=2)
    price_eur = models.DecimalField(max_digits=6, decimal_places=2)
    gdrive_file_url = models.URLField(null=True, blank=True)
    slug = models.SlugField(max_length=128, unique=True)
    image = models.ImageField(upload_to=f'media/products/guides/{slug}', null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/guides/{self.slug}/'


class NotUserReview(models.Model):
    reviewer_first_name = models.CharField(max_length=128)
    reviewer_last_name = models.CharField(max_length=128)
    reviewer_image = models.ImageField(upload_to='media/products/reviews/users_images', null=False, blank=False)
    review = models.TextField(blank=False, null=False)
    date = models.DateField()

    def __str__(self):
        return f'{self.reviewer_first_name} {self.reviewer_last_name}'

