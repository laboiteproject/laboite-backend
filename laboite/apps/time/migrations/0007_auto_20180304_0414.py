# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-04 03:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('laboite.apps.time', '0006_auto_20171124_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apptime',
            name='boite',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boites.Boite', verbose_name='Boîte'),
        ),
    ]
