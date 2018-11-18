from django.contrib import admin

from .models import Car, Review
from .forms import ReviewAdminForm


class CarAdmin(admin.ModelAdmin):
    ordering = ('-pk',)  # новые записи с верху
    list_display = ('brand', 'model', 'display_reviews')
    list_filter = ('brand', 'model')  # добавляем фильтры в админку
    search_fields = ['brand', 'model']  # фильтр по моделям и маркам


class ReviewAdmin(admin.ModelAdmin):
    ordering = ('-pk',)  # новые записи с верху
    list_display = ('car', 'title')
    list_filter = ('car', 'title')  # добавляем фильтры в админку
    search_fields = ['car__model', 'car__brand', 'title']  # ищем по связанным полям и по названию статьи
    form = ReviewAdminForm


admin.site.register(Car, CarAdmin)
admin.site.register(Review, ReviewAdmin)
