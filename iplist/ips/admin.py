# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import IPlist
from import_export import resources
from import_export.resources import ModelResource
from import_export.admin import ImportExportMixin, ImportMixin, ExportActionModelAdmin

class IPresource(resources.ModelResource):
        class Meta:
                model = IPlist
#               exclude = ('id','pool_text','refresh_time',)


class IPlistAdmin(ImportExportMixin, admin.ModelAdmin):

    fieldsets = [
        (None,               {'fields': ['ip_text']}),
        ('port',{'fields':['port_text']}),
        ('policy',{'fields':['policy_text']}),
        ('URL',{'fields':['URL_text']}),
        ('VS-name',{'fields':['VS_text']}),
        ('pool',{'fields':['pool_text']}),
        ('idc',{'fields':['idc_text']}),
        ('business',{'fields':['business_text']}),
#       ('idc',{'fields':['business_text']}),
#       ('business',{'fields':['idc_text']}),
        ('owner',{'fields':['owner']}),
        ('Date information', {'fields': ['refresh_time']}),
    ]
#    inlines = [ChoiceInline]

    list_display = ('ip_text','port_text','policy_text','URL_text','VS_text','idc_text','business_text','owner','refresh_time')
    list_filter = ['policy_text']
    search_fields = ['ip_text','URL_text','VS_text','business_text','owner','idc_text']
    resource_class = IPresource    

admin.site.register(IPlist, IPlistAdmin)
