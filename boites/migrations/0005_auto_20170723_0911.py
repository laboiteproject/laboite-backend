# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-23 07:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boites', '0004_auto_20170719_1244'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tileapp',
            options={'verbose_name': 'App', 'verbose_name_plural': 'Apps'},
        ),
        migrations.AlterField(
            model_name='tile',
            name='boite',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boites.Boite'),
        ),
        migrations.AlterField(
            model_name='tileapp',
            name='tile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boites.Tile', verbose_name='Tuile'),
        ),
    ]