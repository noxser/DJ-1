import csv
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from app.models import Route, Station

with open('moscow_bus_stations.csv', newline='', encoding='cp1251') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        station = Station()
        station.id = row['ID']
        station.name = row['Name']
        station.latitude = row['Latitude_WGS84']
        station.longitude = row['Longitude_WGS84']
        station.save()
        for route in row['RouteNumbers'].split('; '):
            obj, created = Route.objects.get_or_create(name=route)
            station.routes.add(obj)
    print('All done')