# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-03-20 04:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system_permissions', '0003_auto_20190320_1141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='permissions',
            name='Permission_Picture',
        ),
    ]
