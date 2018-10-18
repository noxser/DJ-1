from django import template

register = template.Library()

@register.filter
def convert_data(value):
    return value.strftime("%Y-%m-%d")
