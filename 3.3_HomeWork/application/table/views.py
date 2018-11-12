import csv
from operator import itemgetter

from django.shortcuts import render
from django.views import View

from .models import Field, CsvPath

from django.http import Http404

# CSV_FILENAME = 'phones.csv'
# COLUMNS = [
#     {'name': 'id', 'width': 1},
#     {'name': 'name', 'width': 3},
#     {'name': 'price', 'width': 2},
#     {'name': 'release_date', 'width': 2},
#     {'name': 'lte_exists', 'width': 1},
# ]


CSV_FILENAME = CsvPath.objects.get(pk=1)
# сортируем колонки по полю sort_number )
COLUMNS = sorted(Field.objects.values(), key=itemgetter('sort_number'))


class TableView(View):
    def get(self, request):
        try:
            with open(CSV_FILENAME.get_path(), 'rt') as csv_file:
                header = []
                table = []
                table_reader = csv.reader(csv_file, delimiter=';')
                for table_row in table_reader:
                    if not header:
                        header = {idx: value for idx, value in enumerate(table_row)}
                    else:
                        row = {header.get(idx) or 'col{:03d}'.format(idx): value
                               for idx, value in enumerate(table_row)}
                        table.append(row)

                result = render(request, 'table.html', {'columns': COLUMNS, 'table': table, 'csv_file': CSV_FILENAME})
            return result
        except FileNotFoundError:
            raise Http404("We can't find source file.")
