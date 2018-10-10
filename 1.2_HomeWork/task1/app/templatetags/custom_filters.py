from django import template

register = template.Library()

@register.filter
def color_for_cell(value, cell):
	if cell == 0:
		return ''
	if cell == 13:
		return '#808080'
	if value:
		val = float(value)
		if val < 0:
			return '#008000'
		if 1< val <= 2:
			return '#FFC0CB'
		if  2 < val <= 5:
			return '#F08080'
		if  5 < val:
			return '#FF0000'
	return ''