# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin


from .models import Threat
from import_export import resources
from import_export.resources import ModelResource
from import_export.admin import ImportExportMixin, ImportMixin, ExportActionModelAdmin

class Threatsource(resources.ModelResource):
        class Meta:
                model = Threat

class ThreatAdmin(ImportExportMixin, admin.ModelAdmin):
        fieldsets = [
                ('Threat_type',    {'fields': ['Threat_type']}),
                ('Malicious_IP',      {'fields': ['Malicious_IP']}),
                ('Inner_IP',      {'fields': ['Inner_IP']}),
                ('Domain',             {'fields':['Domain']}),
                ('Intelligence',      {'fields': ['Intelligence']}),
                ('Wiki',    {'fields': ['Wiki']}),
                ('Time', {'fields':['Time']}),
                ('Count',{'fields':['Count']})
        ]

        list_display = ('Threat_type','Malicious_IP','Inner_IP','Domain','Intelligence','Wiki','Time','Count')
        list_filter = ['Threat_type']
        search_fields = ['Threat_type','Malicious_IP','Inner_IP','Domain','Intelligence','Wiki','Time']
        resource_class = Threatsource
        admin.site.site_header = "Threat Intelligence System"

admin.site.register(Threat, ThreatAdmin)
