# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-14 05:48
from __future__ import unicode_literals

from django.db import migrations, models
import gallery_app.models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gallery_app', '0004_auto_20170812_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=sorl.thumbnail.fields.ImageField(editable=False, upload_to=gallery_app.models.image_upload_path),
        ),
        migrations.AlterField(
            model_name='tag',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
