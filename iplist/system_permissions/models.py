# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.utils import timezone
from django.db import models

class Permissions(models.Model):
        Permission_Detail = models.CharField(max_length=200)
        Permission_Example = models.CharField(max_length=200)
        #Permission_Picture = models.ImageField(upload_to='uploads/%Y/%m/%d',height_field=None, width_field=None,max_length=100,blank=True)
	def __str__(self):
		return self.Permission_Detail

class System_Permissions(models.Model):
	System_Name = models.CharField(max_length=200)
	System_Url = models.URLField(max_length=200)
	System_Owner = models.CharField(max_length=200)
	Permission_Name = models.ManyToManyField(Permissions)
	def __str__(self):
		return self.System_Name
