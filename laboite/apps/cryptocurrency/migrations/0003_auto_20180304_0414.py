# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-04 03:14
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('laboite.apps.cryptocurrency', '0002_auto_20171207_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appcryptocurrency',
            name='boite',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boites.Boite', verbose_name='Boîte'),
        ),
    ]
