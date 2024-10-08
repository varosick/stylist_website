# Generated by Django 5.1.1 on 2024-09-21 12:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_servicefile'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduleDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='userservices',
            name='date_of_service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.scheduledate'),
        ),
    ]