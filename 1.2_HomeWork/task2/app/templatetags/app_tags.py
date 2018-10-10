from django import template

register = template.Library()

@register.inclusion_tag('app/nav_button_tag.html') # регистрируем тег и подключаем шаблон
# обрашаем внимание на путь !!!! просто nav_button_tag.html не работало ((((
def nav_button_tag(rout):
    # получаем путь по которому сработало меню и выделяем соответствующее
    return {'current':rout}