# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-12 04:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gallery_app', '0002_auto_20170812_0338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='thumb',
        ),
        migrations.AddField(
            model_name='image',
            name='filename',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='title',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='uploaded',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]