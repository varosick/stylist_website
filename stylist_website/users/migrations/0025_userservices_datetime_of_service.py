# Generated by Django 5.1.1 on 2024-09-27 15:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0024_alter_userguides_payment_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='userservices',
            name='datetime_of_service',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
