# Generated by Django 5.1.1 on 2024-09-12 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_productcategory_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/media'),
        ),
    ]
