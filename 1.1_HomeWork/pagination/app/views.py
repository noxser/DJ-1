import csv 
import urllib.parse
from django.shortcuts import render_to_response, redirect
from django.urls import reverse
from django.core.paginator import Paginator 
from app.settings import BUS_STATION_CSV 

# Праивльно ли расположить обработчик файла до функций представления ?
# Ловим ошибку при отсутствии файла
stations = []
try:
	with open(BUS_STATION_CSV, newline='',  encoding='cp1251') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			stations.append({
				'Name': row['Name'], 
				'Street': row['Street'], 
				'District': row['District']
				})
except Exception:
	stations = [{'Name': 'File not found','Street': '','District': ''}]

def index(request):
    return redirect(reverse(bus_stations))

def bus_stations(request):
	page = request.GET.get('page')
	if page == None:
		page = '1'

	paginator = Paginator(stations, 10) # колличество данных для показа на странице
	cur_page = paginator.page(page) # получаем текущюю "страницу"

	# Нашел несколько способов собрать url с get 
	# Также сразу сделал проверку на наличие страниц для перехода
	# Длиновато но вроде по логике понятно что должно получиться
	return render_to_response('index.html', context={
		'bus_stations': cur_page.object_list,
		'current_page': page,
		'prev_page_url': (reverse(bus_stations) + '?' + urllib.parse.urlencode({'page':cur_page.previous_page_number()}))
		 if cur_page.has_previous() else False,
		'next_page_url': (reverse(bus_stations) + '?' + urllib.parse.urlencode({'page':cur_page.next_page_number()}))
		 if cur_page.has_next() else False,
		# 'next_page_url': (f'%s?page={cur_page.next_page_number()}' % reverse(bus_stations)) if cur_page.has_next() else False,
		# 'next_page_url': (reverse(bus_stations) + '?' + f'page={cur_page.next_page_number()}') if cur_page.has_next() else False,
	})


