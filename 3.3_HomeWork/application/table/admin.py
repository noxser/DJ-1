from django.contrib import admin

from .models import Field, CsvPath


# Register your models here.

@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    list_display = ('id', 'sort_number', 'name', 'width')
    ordering = ('sort_number',)


@admin.register(CsvPath)
class CsvPathAdmin(admin.ModelAdmin):
    list_display = ('csvPath',)
