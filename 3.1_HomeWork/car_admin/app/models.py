import re
from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=50, verbose_name='Марка')
    model = models.CharField(max_length=50, verbose_name='Модель')

    def __str__(self):
        return f'{self.brand} {self.model}'

    def review_count(self):
        return Review.objects.filter(car=self).count()

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'

    def display_reviews(self):
        """
        Считаем обзоры для авто с помощью обратной связи
        """
        return self.review_count()

    display_reviews.short_description = 'Колличество обзоров'


class Review(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='Автомобиль')
    title = models.CharField(max_length=100, verbose_name='Название')
    text = models.TextField(verbose_name='Обзор')

    def __str__(self):
        return str(self.car) + ' ' + self.text_without_html()[:50]

    def text_without_html(self):
        return re.sub('<.*?>', '', self.text)

    class Meta:
        verbose_name = 'Обзор'
        verbose_name_plural = 'Обзоры'