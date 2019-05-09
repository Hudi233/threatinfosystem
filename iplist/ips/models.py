# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class IPlist(models.Model):
	ip_text = models.CharField(max_length=200)
	port_text = models.CharField(max_length=200)
        policy_text = models.CharField(max_length=200)
        URL_text = models.CharField(max_length=200)
        VS_text = models.CharField(max_length=200)
        pool_text = models.CharField(max_length=2000)
        business_text = models.CharField(max_length=200)
        idc_text = models.CharField(max_length=200)
        refresh_time = models.DateTimeField('date published')
        owner = models.CharField(max_length=200)

	#def __str__(self):
         #       return self.ip_text 
	def __unicode__(self):
		
		return self.business_text
		
        def was_published_recently(self):
                return self.refresh_time >= timezone.now() - datetime.timedelta(days=1)
        was_published_recently.admin_order_field = 'refresh_time'
        was_published_recently.boolean = True
        was_published_recently.short_description = 'Published recently?'
