# Generated by Django 5.1.1 on 2024-09-21 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_scheduledate_is_booked'),
    ]

    operations = [
        migrations.AddField(
            model_name='userservices',
            name='file',
            field=models.FileField(default='', upload_to='media/service_files/'),
        ),
    ]
