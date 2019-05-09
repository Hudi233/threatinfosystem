# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.utils import timezone

class Threat(models.Model):
        Threat_type = models.PositiveIntegerField(default=29)
        Malicious_IP = models.CharField(max_length=200)
        Inner_IP = models.CharField(max_length=200,blank=True)
        Domain = models.CharField(max_length=200,blank=True)
        Time = models.DateTimeField(default=timezone.now)
        Intelligence = models.CharField(max_length=200,blank=True)
        Wiki = models.URLField(max_length=200,blank=True)
        Count = models.PositiveIntegerField(default=0)



	def __str__(self):
                return self.Malicious_IP
