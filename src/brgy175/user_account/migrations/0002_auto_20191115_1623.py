# Generated by Django 2.2.7 on 2019-11-15 08:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.EmailField(max_length=60, unique=True, validators=[django.core.validators.EmailValidator(message='error email')], verbose_name='email'),
        ),
    ]
