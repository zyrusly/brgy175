# Generated by Django 2.2.5 on 2019-11-13 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('residents', '0011_resident_pwd_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resident',
            name='height',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='resident',
            name='weight',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
