# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-05 09:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sharestuff', '0006_auto_20161104_1957'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='liker_delt_resurs',
        ),
        migrations.AddField(
            model_name='profile',
            name='liker_delt_ressurs',
            field=models.ManyToManyField(blank=True, to='sharestuff.TeachPack'),
        ),
    ]
