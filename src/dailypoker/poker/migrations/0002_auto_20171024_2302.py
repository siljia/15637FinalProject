# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-25 03:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dealer', models.PositiveSmallIntegerField(default=1, null=True)),
                ('pot_size', models.IntegerField()),
                ('round_max_bet', models.IntegerField()),
                ('round_status', models.PositiveSmallIntegerField()),
                ('is_finished', models.BooleanField(default=False)),
                ('cards_on_table', models.ManyToManyField(related_name='ontable', to='poker.Card')),
                ('cards_remain', models.ManyToManyField(related_name='remain', to='poker.Card')),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='chip_remain',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='hand_card',
            field=models.ManyToManyField(to='poker.Card'),
        ),
        migrations.AddField(
            model_name='player',
            name='seat_id',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='state',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='accum_bet',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='player',
            name='begin_chip',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='player',
            name='round_bet',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='game',
            name='players',
            field=models.ManyToManyField(related_name='game', to='poker.Player'),
        ),
    ]
