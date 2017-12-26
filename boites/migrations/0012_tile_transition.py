# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-11 10:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boites', '0011_tile_brightness'),
    ]

    operations = [
        migrations.AddField(
            model_name='tile',
            name='transition',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Aucune'), (1, 'Fondu'), (2, 'Défilement ←'), (3, 'Défilement →'), (4, 'Défilement ↑'), (5, 'Défilement ↓')], default=0, verbose_name='Transition'),
        ),
    ]
