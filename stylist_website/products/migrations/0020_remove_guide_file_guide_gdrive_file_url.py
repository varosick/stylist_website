# Generated by Django 5.1.1 on 2024-09-29 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_notuserreview'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guide',
            name='file',
        ),
        migrations.AddField(
            model_name='guide',
            name='gdrive_file_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
