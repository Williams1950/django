# Generated by Django 3.2.9 on 2021-12-08 12:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maxvtech', '0004_feature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='img',
            field=models.FileField(upload_to='pics/%Y/%m/', validators=[django.core.validators.FileExtensionValidator(['pdf', 'doc', 'svg'])]),
        ),
    ]
