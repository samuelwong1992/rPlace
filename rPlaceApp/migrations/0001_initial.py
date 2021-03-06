# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-26 11:44
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time_created', models.DateTimeField(auto_now_add=True)),
                ('x_coordinate', models.IntegerField(validators=[django.core.validators.MaxValueValidator(499), django.core.validators.MinValueValidator(0)])),
                ('y_coordinate', models.IntegerField(validators=[django.core.validators.MaxValueValidator(499), django.core.validators.MinValueValidator(0)])),
                ('colour', models.IntegerField(validators=[django.core.validators.MaxValueValidator(12), django.core.validators.MinValueValidator(0)])),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tiles', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('date_time_created',),
            },
        ),
    ]
