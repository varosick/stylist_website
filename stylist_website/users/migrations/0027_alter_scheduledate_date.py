# Generated by Django 5.1.1 on 2024-09-27 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0026_remove_userservices_date_of_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduledate',
            name='date',
            field=models.DateField(),
        ),
    ]