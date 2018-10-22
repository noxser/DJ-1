from django.db import models


class Scopes(models.Model):
    topic = models.CharField(max_length=30, verbose_name='Раздел')

    class Meta:
        verbose_name = 'Разделы'
        verbose_name_plural = 'Разделы'

    def __str__(self):
        return self.topic


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')
    scopes = models.ManyToManyField(Scopes, through='MainScopes')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

    def display_tag(self):
        """
        Создаем список тегов ))) для админки, в виде списка
        классная штука
        """
        return ', '.join([tag.topic for tag in self.scopes.all()[:3]])

    display_tag.short_description = 'Тематики статьи'


class MainScopes(models.Model):
    scopes = models.ForeignKey(Scopes, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    is_main = models.BooleanField(verbose_name='Основной')

    class Meta:
        verbose_name = 'Тематика статьи'
        verbose_name_plural = 'Тематика статьи'
