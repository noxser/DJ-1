from django import forms
from django.forms import SelectDateWidget
import datetime
from .widgets import AjaxInputWidget, My_widjet
from .models import City


class SearchTicket(forms.Form):
    MONTHS = {
        1: ('Январь'), 2: ('Февраль'), 3: ('Март'), 4: ('Аперль'),
        5: ('Май'), 6: ('Июнь'), 7: ('Июль'), 8: ('Август'),
        9: ('Сентябрь'), 10: ('Октябрь'), 11: ('Ноябрь'), 12: ('Декабрь')
    }

    city_from = forms.CharField(label='Город отправления', label_suffix=':',
                                widget=AjaxInputWidget(url='api/city_ajax', attrs={'class': 'inline right-margin'}))
    city_to = forms.ModelChoiceField(queryset=City.objects.all(), label='Город прибытия', label_suffix=':',
                                     empty_label='----------')

    date_go = forms.DateField(label='Дата', label_suffix=':', initial=datetime.date.today, widget=SelectDateWidget(
        empty_label="Nothing", months=MONTHS
    ))
    Date = forms.DateField(label='Дата', label_suffix=':', widget=My_widjet())
