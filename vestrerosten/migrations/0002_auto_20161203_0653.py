# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-03 05:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vestrerosten', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='underskrifter',
            name='kommentar',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
