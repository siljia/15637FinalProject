# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-05 22:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poker', '0009_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='asset',
            field=models.IntegerField(default=10000),
        ),
    ]
