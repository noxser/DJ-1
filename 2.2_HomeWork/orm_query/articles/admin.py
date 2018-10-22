from django.contrib import admin

from .models import Article, Genre, Author


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'published_at')
    pass


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone')
    pass
