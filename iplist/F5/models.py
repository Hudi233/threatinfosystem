# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class F5(models.Model):
        VS = models.CharField(max_length=200)
        pool = models.CharField(max_length=200)
        pool_port = models.IntegerField()
        idc = models.CharField(max_length=200)

        def __str__(self):
                return self.VS
