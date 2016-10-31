# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-29 09:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('boites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppTasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField(default=True, help_text='Indique si cette app est activ\xe9e sur votre bo\xeete', verbose_name='App activ\xe9e ?')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Date de cr\xe9ation')),
                ('last_activity', models.DateTimeField(auto_now=True, verbose_name='Derni\xe8re activit\xe9')),
                ('asana_personal_access_token', models.CharField(default=None, help_text="Veuillez indiquer votre cl\xe9 d'API personnelle Asana (Personal Access Token)", max_length=64, null=True, verbose_name="Cl\xe9 d'API Asana ")),
                ('name', models.CharField(default=None, max_length=128, null=True, verbose_name='Nom de la prochaine t\xe2che')),
                ('tasks', models.PositiveSmallIntegerField(default=None, null=True, verbose_name='Nombre de t\xe2ches \xe0 traiter')),
                ('boite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boites.Boite', verbose_name='Bo\xeete')),
            ],
            options={
                'verbose_name': 'Configuration : t\xe2ches',
                'verbose_name_plural': 'Configurations : t\xe2ches',
            },
        ),
    ]
