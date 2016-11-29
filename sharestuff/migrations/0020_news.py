# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-26 22:24
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sharestuff', '0019_group_beskrivelse'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datotid', models.DateTimeField(default=datetime.datetime(2016, 11, 26, 22, 24, 24, 277349, tzinfo=utc))),
                ('tittel', models.CharField(max_length=24)),
                ('beskjed', models.CharField(max_length=255)),
                ('eier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]