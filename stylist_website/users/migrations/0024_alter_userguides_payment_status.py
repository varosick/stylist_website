# Generated by Django 5.1.1 on 2024-09-25 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0023_userguides'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userguides',
            name='payment_status',
            field=models.IntegerField(choices=[(0, 'Not Paid'), (1, 'Paid')], default=0),
        ),
    ]