# Generated by Django 5.1.1 on 2024-09-12 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_productcategory_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='slug',
            field=models.SlugField(blank=True, max_length=128, null=True),
        ),
    ]
