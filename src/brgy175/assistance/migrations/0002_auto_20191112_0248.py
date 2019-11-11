# Generated by Django 2.2.7 on 2019-11-11 18:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('assistance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='scholar',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='burial',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 11, 18, 48, 52, 51913, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='scholar',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 11, 18, 48, 52, 50913, tzinfo=utc)),
        ),
    ]