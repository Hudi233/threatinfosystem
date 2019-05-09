# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-04-20 06:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Threat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Threat_type', models.CharField(default='29', max_length=200)),
                ('Malicious_IP', models.CharField(max_length=200)),
                ('Inner_IP', models.CharField(blank=True, max_length=200)),
                ('Domain', models.CharField(blank=True, max_length=200)),
                ('Time', models.DateTimeField(default=django.utils.timezone.now)),
                ('Intelligence', models.CharField(blank=True, max_length=200)),
                ('Wiki', models.URLField(blank=True)),
                ('Count', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]