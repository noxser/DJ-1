import csv
import os
import django

#  определяем настройки для импорта из джанго моделей для работы с ними
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")
django.setup()

from phones.models import Phone

with open('phones.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar=' ')
    for row in reader:
        if row[0] != 'id':
            phone = Phone()
            phone.id = row[0]
            phone.name = row[1]
            phone.image = row[2]
            phone.price = row[3]
            phone.release_date = row[4]
            phone.lte_exists = row[5]
            phone.save()
