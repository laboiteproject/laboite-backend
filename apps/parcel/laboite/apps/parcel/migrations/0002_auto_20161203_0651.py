# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-03 05:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('laboite.apps.parcel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appparcel',
            name='boite',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='boites.Boite', verbose_name='Bo\xeete'),
        ),
    ]
