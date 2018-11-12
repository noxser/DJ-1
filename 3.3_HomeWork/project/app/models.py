from django.db import models


# Create your models here.

class Route(models.Model):
    name = models.CharField(max_length=50, verbose_name='Маршрут')

    class Meta:
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруты'

    def __str__(self):
        return self.name


class Station(models.Model):
    latitude = models.FloatField(max_length=50, verbose_name='Широта')
    longitude = models.FloatField(max_length=50, verbose_name='Долгота')
    name = models.CharField(max_length=50, verbose_name='Название')
    routes = models.ManyToManyField(Route, related_name="stations", verbose_name='Маршруты')

    class Meta:
        verbose_name = 'Остановка'
        verbose_name_plural = 'Остановки'

    def display_routes(self):
        """
        Создаем список маршрутов для аминки
        """
        return ', '.join([route.name for route in self.routes.all()])

    display_routes.short_description = 'Маршруты'

    def route_numbers(self):
        """
        Создаем список маршрутов для отображения в шаблоне
        """
        return ', '.join([route.name for route in self.routes.all()])

    def __str__(self):
        return self.name
