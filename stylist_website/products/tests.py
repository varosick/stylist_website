from django.test import TestCase, Client
from django.urls import reverse
from products.models import ProductCategory, Product, Guide, Question, CarouselImage
from users.models import User


class ProductsViewsTests(TestCase):
    def setUp(self):
        # Настраиваем тестовые данные
        self.client = Client()

        self.category = ProductCategory.objects.create(
            name="Test Category",
            description="Test Description",
            slug="test-category",
            image='test.png',
            content_image='test.png',
        )

        self.product = Product.objects.create(
            name="Test Product",
            description="Test Product Description",
            price_czk=100.00,
            price_eur=4.00,
            category=self.category,
            slug="test-product",
            image = 'test.png'
        )

        self.guide = Guide.objects.create(
            name="Test Guide",
            description="Test Guide Description",
            price_czk=200.00,
            price_eur=8.00,
            slug="test-guide",
            image='test.png',
        )

    def test_index_view(self):
        # Тест главной страницы (IndexView)
        url = reverse('products:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/index.htm')
        self.assertIn('categories', response.context)
        self.assertIn('guides', response.context)

    def test_category_detail_view(self):
        # Тест детальной страницы категории (CategoryDetailView)
        url = reverse('products:category_detail', kwargs={'category_slug': self.category.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/category_detail.html')
        self.assertIn('products', response.context)
        self.assertIn('carousel_images', response.context)

    def test_product_detail_view_get(self):
        # Тест детальной страницы продукта (ProductDetailView)
        url = reverse('products:product_detail', kwargs={'category_slug': self.category.slug, 'product_slug': self.product.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')
        self.assertIn('product', response.context)
        self.assertIn('details', response.context)

    def test_guide_detail_view(self):
        # Тест страницы гида (GuideDetailView)
        url = reverse('products:guide_detail', kwargs={'guide_slug': self.guide.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/guide_detail.html')
        self.assertIn('guide', response.context)

