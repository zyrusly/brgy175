# Generated by Django 2.2.5 on 2019-11-13 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('residents', '0008_resident_is_pwd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resident',
            name='is_pwd',
            field=models.CharField(max_length=10),
        ),
    ]