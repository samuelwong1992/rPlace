# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-28 02:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rPlaceApp', '0002_canplace'),
    ]

    operations = [
        migrations.AlterField(
            model_name='canplace',
            name='time_to_place',
            field=models.IntegerField(default=1),
        ),
    ]
