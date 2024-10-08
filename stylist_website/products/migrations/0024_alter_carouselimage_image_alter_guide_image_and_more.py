# Generated by Django 5.1.1 on 2024-10-08 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0023_carouselimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carouselimage',
            name='image',
            field=models.ImageField(upload_to='media/products/images_for_carousel/'),
        ),
        migrations.AlterField(
            model_name='guide',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/products/guides/<django.db.models.fields.SlugField>'),
        ),
        migrations.AlterField(
            model_name='notuserreview',
            name='reviewer_image',
            field=models.ImageField(upload_to='media/products/reviews/users_images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/products/products/<django.db.models.fields.SlugField>'),
        ),
    ]