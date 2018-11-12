import csv
from app.models import Route, Station
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Create Superuser users'

    def handle(self, *args, **options):

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
