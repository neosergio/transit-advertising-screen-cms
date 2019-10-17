from django.contrib import admin

from import_export.admin import ImportExportMixin

from .models import Location, Screen


class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {"slug": ("name",)}


class ScreenAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = (
        'file_name',
        'is_active',
        'seconds',
        'start_date',
        'due_date'
    )
    search_fields = ['file_name', 'location']
    readonly_fields = ('created_at', 'modified_at')


admin.site.register(Location, LocationAdmin)
admin.site.register(Screen, ScreenAdmin)
