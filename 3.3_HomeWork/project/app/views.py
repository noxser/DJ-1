from django.shortcuts import render
from django.views.generic import TemplateView
from app.models import Route, Station
from django.core.cache import cache


def route_views(request):
    routes_list = cache.get_or_set('routes_list', sorted([route.name for route in Route.objects.all()]))

    if request.GET.get('route'):
        current_router = request.GET.get('route')
        route = Route.objects.get(name=current_router)
        stations = Station.objects.filter(routes__name__contains=route)
        stations_coordinates = stations.values('longitude', 'latitude')
        longitude_srednee = 0
        latitude_srednee = 0
        num_stations = len(stations_coordinates)
        for coordinates in stations_coordinates:
            longitude_srednee += coordinates['longitude']
            latitude_srednee += coordinates['latitude']
        center = {
            'x': longitude_srednee / num_stations,
            'y': latitude_srednee / num_stations
        }
        return render(request, 'app/stations.html', {
            'routes': routes_list,
            'center': center,
            'stations': stations,
            'route': current_router,
        })

    # при запуске центр Москвы показываем по умолчанию
    return render(request, 'app/stations.html', {
        'routes': routes_list,
        'center': {'x': 37.624427, 'y': 55.749930},
        'stations': '',
    })


class RouteViews(TemplateView):
    template_name = 'app/stations_2.html'
    routes_list = cache.get_or_set('routes_list', sorted([route.name for route in Route.objects.all()]))

    def get(self, request, *args, **kwargs):
        if request.GET.get('route'):
            current_router = request.GET.get('route')
            route = Route.objects.get(name=current_router)
            stations = Station.objects.filter(routes__name__contains=route)
            stations_coordinates = stations.values('longitude', 'latitude')
            longitude_srednee = 0
            latitude_srednee = 0
            num_stations = len(stations_coordinates)
            for coordinates in stations_coordinates:
                longitude_srednee += coordinates['longitude']
                latitude_srednee += coordinates['latitude']
            center = {
                'x': longitude_srednee / num_stations,
                'y': latitude_srednee / num_stations
            }
            return render(request, self.template_name, {
                'routes': self.routes_list,
                'center': center,
                'stations': stations,
                'route': current_router,
            })
        # при запуске центр Москвы показываем по умолчанию
        return render(request, self.template_name, {
            'routes': self.routes_list,
            'center': {'x': 37.624427, 'y': 55.749930},
            'stations': '',
        })
