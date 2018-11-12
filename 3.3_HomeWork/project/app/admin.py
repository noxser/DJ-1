from django.contrib import admin

# Register your models here.

from .models import Route, Station


@admin.register(Route)
class Route(admin.ModelAdmin):
    list_display = ('name',)



@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'latitude', 'longitude', 'display_routes')
    ordering = ('id',)

