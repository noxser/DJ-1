import csv 
import pprint

stations = []

# stations = [{'Name': 'название1', 'Street': 'улица1', 'District': 'район1'},
# 			{'Name': 'название2', 'Street': 'улица2', 'District': 'район2'},
# 			{'Name': 'название3', 'Street': 'улица3', 'District': 'район3'},
# 			{'Name': 'название4', 'Street': 'улица4', 'District': 'район4'},
# 			{'Name': 'название5', 'Street': 'улица5', 'District': 'район5'},
# 			{'Name': 'название6', 'Street': 'улица6', 'District': 'район6'}
# 			]


with open('data-398-2018-08-30.csv', newline='') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		x = {'Name': row['Name'], 'Street': row['Street'], 'District': row['District']}
		stations.append(x)
		# print(row['Name'], row['Street'], row['District'])

pprint.pprint(stations)

# import urllib.request
# import urllib.parse
# params = urllib.parse.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
# url = "http://www.musi-cal.com/cgi-bin/query?%s" % params
# with urllib.request.urlopen(url) as f:
#      print(f.read().decode('utf-8'))


# from datetime import datetime, date, time

# print(datetime.now())
