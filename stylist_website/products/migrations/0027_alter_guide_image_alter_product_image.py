# Generated by Django 5.1.1 on 2024-10-15 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0026_guidecarouselimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guide',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/products/guides/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/products/products/'),
        ),
    ]
