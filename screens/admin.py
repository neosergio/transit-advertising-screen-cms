from django.contrib import admin

from .models import Location, Screen


class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', )


class ScreenAdmin(admin.ModelAdmin):
    list_display = ('url', 'is_active', 'location', 'priority', 'seconds', 'text', 'created_at', 'modified_at')
    search_fields = ['text', 'location', 'url']


admin.site.register(Location, LocationAdmin)
admin.site.register(Screen, ScreenAdmin)
