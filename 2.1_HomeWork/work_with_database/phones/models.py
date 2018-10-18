from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    id = models.IntegerField(verbose_name='id:', primary_key=True, unique=True)
    name = models.CharField(verbose_name='Название:', max_length=30)
    image = models.URLField(verbose_name='Изображение:')
    price = models.CharField(verbose_name='Стоимость:', max_length=30)
    release_date = models.DateField(verbose_name='Дата релиза:')
    lte_exists = models.BooleanField(verbose_name='Наличие LTE:')
    slug = models.SlugField(verbose_name='Slug:', unique=True)

    def __str__(self):
        return self.name

    # -----------------
    # конструкция необходима для формирования поля slug при загрузке данных
    # посредством скрипта ! через админку работает и без этого метода
    # ------------------
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super(Phone, self).save(*args, **kwargs)
