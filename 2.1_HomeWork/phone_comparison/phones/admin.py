from django.contrib import admin

# Register your models here.

from .models import Xiaomi, Samsung, Apple, Phones

admin.site.register(Apple)

admin.site.register(Xiaomi)

admin.site.register(Samsung)

admin.site.register(Phones)