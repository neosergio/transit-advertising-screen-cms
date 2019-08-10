from django.contrib import admin

from .models import Location, Screen


class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {"slug": ("name",)}


class ScreenAdmin(admin.ModelAdmin):
    list_display = (
        'text',
        'url',
        'is_active',
        'seconds',
        'start_date',
        'due_date'
    )
    search_fields = ['text', 'location', 'url']
    readonly_fields = ('created_at', 'modified_at')


admin.site.register(Location, LocationAdmin)
admin.site.register(Screen, ScreenAdmin)
