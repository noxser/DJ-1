from django.shortcuts import render
from app.models import Route, Station


def route_views(request):
    routes = sorted([route.name for route in Route.objects.all()])
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
        return render(request, 'stations.html', {
            'routes': routes,
            'center': center,
            'stations': stations,
            'route': current_router,
        })

    # при запуске центр Москвы показываем по умолчанию
    return render(request, 'stations.html', {
        'routes': routes,
        'center': {'x': 37.624427, 'y': 55.749930},
        'stations': '',
    })
