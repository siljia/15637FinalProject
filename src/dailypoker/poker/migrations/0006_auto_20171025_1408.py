# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-25 18:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poker', '0005_player'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='cards_on_table',
            field=models.ManyToManyField(null=True, related_name='ontable', to='poker.Card'),
        ),
        migrations.AlterField(
            model_name='game',
            name='cards_remain',
            field=models.ManyToManyField(null=True, related_name='remain', to='poker.Card'),
        ),
    ]