import sys
import locale
from django import template

register = template.Library()


@register.simple_tag
def get_verbose_field_name(instance, field_name):
    # получаем  verbose_name для данного поля
    return instance._meta.get_field(field_name).verbose_name.title()


@register.filter
def convert_data(value):
    # клевая штука позволяет месяца на русском выводить
    if sys.platform == 'win32':
        locale.setlocale(locale.LC_ALL, 'rus_rus')
    else:
        locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
    return value.strftime("%d %b %Y")

@register.filter
def convert_bool(value):
    if value:
        return 'присутствует'
    else:
        return 'отсутствует'
