# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-24 10:04
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboite.apps.bus', '0002_auto_20161203_0651'),
    ]

    operations = [
        migrations.AddField(
            model_name='appbus',
            name='stop_name',
            field=models.TextField(default='', verbose_name="Nom de l'arr\xeat"),
        ),
        migrations.AlterField(
            model_name='appbus',
            name='last_activity',
            field=models.DateTimeField(null=True, verbose_name='Derni\xe8re activit\xe9'),
        ),
    ]
