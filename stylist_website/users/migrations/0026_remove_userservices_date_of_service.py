# Generated by Django 5.1.1 on 2024-09-27 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0025_userservices_datetime_of_service'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userservices',
            name='date_of_service',
        ),
    ]
