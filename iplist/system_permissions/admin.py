# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import System_Permissions, Permissions
from import_export import resources
from import_export.resources import ModelResource
from django.contrib import admin
from import_export.admin import ImportExportMixin, ImportMixin, ExportActionModelAdmin

class Systemsource(resources.ModelResource):
	class Meta:
		model = System_Permissions

class Systemadmin(ImportExportMixin, admin.ModelAdmin):
	
	fieldsets = (
		(None, {'fields' : ('Syetem_Name', 'System_Url', 'Syetem_Owner', 'Permission_Name', 'Permission_Detail', 'Permission_Example')
		}),
	)
	list_display = ('Syetem_Name', 'System_Url', 'Syetem_Owner', 'Permission_Detail', 'Permission_Example')
	list_filter = ['Syetem_Name']
	search_fields = ['Syetem_Name', 'System_Url', 'Syetem_Owner', 'Permission_Detail', 'Permission_Example']
	resource_class = Systemsource


admin.site.register(System_Permissions)
#admin.site.register(System_Permissions, Systemadmin)
