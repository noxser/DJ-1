import re
from django.db import models
from django.template.defaultfilters import truncatewords_html


class Car(models.Model):
    brand = models.CharField(max_length=50, verbose_name='Марка')
    model = models.CharField(max_length=50, verbose_name='Модель')

    def __str__(self):
        return f'{self.brand} {self.model}'

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'

    def display_reviews(self):
        """
        Считаем обзоры для авто
        """
        return Review.objects.filter(car=self).count()

    display_reviews.short_description = 'Количество обзоров'


class Review(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='Автомобиль')
    title = models.CharField(max_length=100, verbose_name='Название')
    text = models.TextField(verbose_name='Обзор')

    def __str__(self):
        return str(self.car) + ' ' + self.text_without_html()[:50]

    def text_without_html(self):
        # return re.sub('<.*?>', '', self.text)
        return truncatewords_html(self.text, 0)

    class Meta:
        verbose_name = 'Обзор'
        verbose_name_plural = 'Обзоры'
