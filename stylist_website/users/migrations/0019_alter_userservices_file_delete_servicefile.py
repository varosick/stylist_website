# Generated by Django 5.1.1 on 2024-09-21 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_userservices_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userservices',
            name='file',
            field=models.FileField(upload_to='media/service_files/'),
        ),
        migrations.DeleteModel(
            name='ServiceFile',
        ),
    ]
