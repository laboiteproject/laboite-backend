# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-08 13:55
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('boites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppMetro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField(default=True, help_text='Indique si cette app est activ\xe9e sur votre bo\xeete', verbose_name='App activ\xe9e ?')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Date de cr\xe9ation')),
                ('last_activity', models.DateTimeField(auto_now=True, verbose_name='Derni\xe8re activit\xe9')),
                ('failure', models.BooleanField(default=False, verbose_name='Probl\xe8me en cours ?')),
                ('recovery_time', models.PositiveSmallIntegerField(default=None, null=True, verbose_name='Minutes avant r\xe9tablissement')),
                ('boite', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='boites.Boite', verbose_name='Bo\xeete')),
            ],
            options={
                'verbose_name': 'Configuration : M\xe9tro',
                'verbose_name_plural': 'Configurations : M\xe9tro',
            },
        ),
    ]
