# Generated by Django 2.2.7 on 2019-11-11 21:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('assistance', '0006_auto_20191112_0527'),
    ]

    operations = [
        migrations.AddField(
            model_name='burial',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='burial',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 11, 21, 33, 42, 343795, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='scholar',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 11, 21, 33, 42, 343795, tzinfo=utc)),
        ),
    ]
