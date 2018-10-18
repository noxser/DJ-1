from django.contrib import admin

# Register your models here.

from .models import Phone


# регистрируем класс для автозаполнения поля slug ))) из name
class PhoneAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Phone, PhoneAdmin)
