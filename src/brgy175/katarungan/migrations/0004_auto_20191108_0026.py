# Generated by Django 2.2.5 on 2019-11-07 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('katarungan', '0003_auto_20191012_0026'),
    ]

    operations = [
        migrations.RenameField(
            model_name='katarungan',
            old_name='c_resident',
            new_name='convict',
        ),
    ]