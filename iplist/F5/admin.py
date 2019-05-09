# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from import_export import resources
from import_export.resources import ModelResource
from import_export.admin import ImportExportMixin, ImportMixin, ExportActionModelAdmin
from .models import F5

class F5Resource(resources.ModelResource):
        class Meta:
                model = F5
                exclude = ('id',)
#               fields = ['VS','pool','pool_port','idc',]
                import_id_fields = ['VS',]
#		skip_unchanged = True
		dry_run = True


class F5Admin(ImportExportMixin,admin.ModelAdmin):
        fieldsets = [
            ('VS',      {'fields':['VS']}),
            ('pool',    {'fields':['pool']}),
            ('pool_port', {'fields':['pool_port']}),
            ('idc',        {'fields':['idc']})
        ]

        list_display = ('VS','pool','pool_port','idc')
        list_filter = ['pool_port']
        search_fields = ['VS','pool','pool_port','idc']
        resource_class = F5Resource

admin.site.register(F5,F5Admin)
