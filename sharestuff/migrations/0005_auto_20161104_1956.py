# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-04 18:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sharestuff', '0004_auto_20161104_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='liker_delt_resurs',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='sharestuff.TeachPack'),
        ),
    ]
