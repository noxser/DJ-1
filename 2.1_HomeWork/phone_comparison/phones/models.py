from django.db import models

class Samsung(models.Model):
    phone_model = models.ForeignKey('Phones', on_delete=models.CASCADE, verbose_name='Модель:')
    dual_cam = models.CharField(verbose_name='Двойная камера:', max_length=30)

    def __str__(self):
        return self.phone_model.phone_model

class Xiaomi(models.Model):
    phone_model = models.ForeignKey('Phones', on_delete=models.CASCADE, verbose_name='Модель:')
    fm_radio = models.CharField(verbose_name='FM радио:', max_length=30)
    dual_cam = models.CharField(verbose_name='Двойная камера:', max_length=30)

    def __str__(self):
        return self.phone_model.phone_model

class Apple(models.Model):
    phone_model = models.ForeignKey('Phones', on_delete=models.CASCADE, verbose_name='Модель:')

    def __str__(self):
        return self.phone_model.phone_model


class Phones(models.Model):
    phone_model = models.CharField(verbose_name='Модель:', max_length=30)
    cost = models.CharField(verbose_name='Цена:', max_length=30)
    operation_system = models.CharField(verbose_name='Операционная система:', max_length=30)
    display_resolution = models.CharField(verbose_name='Разрешение экрана:', max_length=30)
    ram = models.CharField(verbose_name='Оперативная память:', max_length=30)
    storage = models.CharField(verbose_name='Хранилище:', max_length=30)

    def __str__(self):
        return self.phone_model
