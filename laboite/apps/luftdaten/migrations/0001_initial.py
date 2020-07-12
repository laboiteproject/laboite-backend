# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-25 21:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('boites', '0016_auto_20180708_2327'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppLuftdaten',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Date de création')),
                ('enabled', models.BooleanField(default=True, help_text='Indique si cette app est activée sur votre boîte', verbose_name='App activée ?')),
                ('last_activity', models.DateTimeField(null=True, verbose_name='Dernière activité')),
                ('sensor', models.CharField(default='11034', help_text="Veuillez saisir l'identifiant de votre capteur luftdaten", max_length=32, verbose_name='Identifiant du capteur Luftdaten')),
                ('aqi', models.PositiveSmallIntegerField(choices=[(0, 'Bon'), (1, 'Moyen'), (2, 'Mauvais')], default=0, verbose_name="Qualité de l'air mesuré par votre capteur")),
                ('boite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boites.Boite', verbose_name='Boîte')),
            ],
            options={
                'verbose_name': 'Configuration : luftdaten',
                'verbose_name_plural': 'Configurations : luftdaten',
            },
        ),
    ]