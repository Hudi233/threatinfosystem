# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-03-22 02:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system_permissions', '0004_remove_permissions_permission_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='permissions',
            name='Permission',
        ),
        migrations.RemoveField(
            model_name='system_permissions',
            name='Permission_Name',
        ),
        migrations.AddField(
            model_name='system_permissions',
            name='Permission_Name',
            field=models.ManyToManyField(to='system_permissions.Permissions'),
        ),
    ]
