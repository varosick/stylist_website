# Generated by Django 5.1.1 on 2024-09-10 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_date_of_birth_alter_user_inst_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='inst_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
