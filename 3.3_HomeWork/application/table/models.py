from django.db import models


# Create your models here.

class Field(models.Model):
    sort_number = models.CharField(max_length=50, verbose_name='Порядковый номер')
    name = models.CharField(max_length=50, verbose_name='Название')
    width = models.CharField(max_length=50, verbose_name='Ширина')

    class Meta:
        verbose_name = 'Поле таблицы'
        verbose_name_plural = 'Поля таблицы'

    def __str__(self):
        return self.name


class CsvPath(models.Model):
    csvPath = models.CharField(max_length=200, verbose_name='Путь до файла csv')

    class Meta:
        verbose_name = 'Путь к CSV'
        verbose_name_plural = 'Путь к CSV'

    def get_path(self):
        return self.csvPath

    def set_path(self, new_path):
        self.csvPath = new_path
        self.save()

    def save(self, *args, **kwargs):
        obj = CsvPath.objects.all()
        if obj.count() == 0 or self.pk == 1:
            super(CsvPath, self).save(*args, **kwargs)

    def __str__(self):
        """
        Получаем имя файла из пути
        """
        return self.csvPath.replace('\\', '/').split('/')[-1]
