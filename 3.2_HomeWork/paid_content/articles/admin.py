from django.contrib import admin

from .models import Article, Profile


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'is_paid')


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'has_subscription')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Profile, ProfileAdmin)
