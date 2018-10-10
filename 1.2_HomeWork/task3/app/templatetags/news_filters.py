from django import template
from datetime import datetime


register = template.Library()


@register.filter
def format_date(value):
    # фильтр по дате
    posts_minutes = (datetime.timestamp(datetime.now()) - value)/60
    if posts_minutes < 10:
        return 'только что'
    if posts_minutes < 1440:
        return f'{round(posts_minutes/60)} часов назад'
    # если не одно условие не прошло то выводим дау ввиде "Год-месяц-число"
    return datetime.fromtimestamp(value).isoformat('#').split('#')[0]


@register.filter
def format_num_score(value, default_rating):
    if value == '':
        value = default_rating
    # фильтруем рейтинг
    if value  <= -5:
        return 'все плохо'
    if  -5 < value < 5:
        return 'нейтрально'
    if value >= 5:
        return 'хорошо'


@register.filter
def format_num_comments(value):
    # фильтруем кол-во комментариев
    if value == 0:
        return 'Оставьте комментарий'
    if  0 < value < 50:
        return value
    if value >= 50:
        return '50+'


@register.filter
def format_selftext(value, count):
    # обрезаем текст сначала и конца на count потом склеиваем
    if value:
        text_splitted = value.split()
        text_start = text_splitted[:count]
        text_end = text_splitted[len(text_splitted)-count:]
        new_text = ' '.join(text_start) + ' ... ' + ' '.join(text_end)
        return new_text
    return value


