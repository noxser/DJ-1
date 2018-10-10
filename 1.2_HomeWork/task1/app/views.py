from django.shortcuts import render
from django.views.generic import TemplateView
import csv


class InflationView(TemplateView):
    template_name = 'inflation.html'
    def get(self, request, *args, **kwargs):
        # чтение csv-файла и заполнение контекста
        inflation_data = []
        with open('inflation_russia.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                inflation_data.append(''.join(row).split(';'))
        return render(request, self.template_name, {'data': inflation_data})