import csv
import re



columns = {'from': 'From', 'to': 'To'}
directional = True

with open('example_flights.csv', 'r') as csvfile:
    flightdata = [{list(columns.keys())[list(columns.values()).index(k)]: v for k, v in r.items() if k in list(columns.values())} for r in csv.DictReader(csvfile, delimiter = ',', skipinitialspace = True)]


for i in range(len(flightdata)):
    for col in columns:
        for x in ['from', 'to']:
            flightdata[i][x] = re.search('(?<![A-Z0-9])([A-Z0-9]){3}(?![A-Z0-9])', flightdata[i][x]).group()


routes = {}
airports = {}

for flight in flightdata:
    if f"{flight['from']}/{flight['to']}" not in routes:
        routes[f"{flight['from']}/{flight['to']}"] = 0
    routes[f"{flight['from']}/{flight['to']}"] += 1
    if not directional:
        if f"{flight['to']}/{flight['from']}" not in routes:
            routes[f"{flight['to']}/{flight['from']}"] = 0
        routes[f"{flight['to']}/{flight['from']}"] += 1
    
    if flight['from'] not in airports:
        airports[flight['from']] = {'routes': {}, 'routes_count': 0, 'flights_count': 0}
    if flight['to'] not in airports[flight['from']]['routes']:
        airports[flight['from']]['routes'][flight['to']] = 0
        airports[flight['from']]['routes_count'] += 1
    airports[flight['from']]['routes'][flight['to']] += 1
    airports[flight['from']]['flights_count'] += 1
    if not directional:
        if flight['to'] not in airports:
            airports[flight['to']] = {'routes': {}, 'routes_count': 0, 'flights_count': 0}
        if flight['from'] not in airports[flight['to']]['routes']:
            airports[flight['to']]['routes'][flight['from']] = 0
            airports[flight['to']]['routes_count'] += 1
        airports[flight['to']]['routes'][flight['from']] += 1
        airports[flight['to']]['flights_count'] += 1


routes = dict(sorted(routes.items()))
airports = dict(sorted(airports.items()))


while True:
    uinput = input('Input Airport (eg. LAX) or Route (eg. JFK/LAX): ').upper()
    if uinput.lower() in ['q', 'quit', 'exit']:
        break
    
    if '/' in uinput:
        if uinput in routes:
            print(f"Found {uinput} in list of routes ({routes[uinput]})")
        else:
            print(f"Did not find {uinput} in list of routes")
    else:
        if uinput in airports:
            print(f"Found {airports[uinput]['routes_count']} routes from {uinput} to {', '.join([f"{airport} ({airport_count})" for airport, airport_count in airports[uinput]['routes'].items()])}")
        else:
            print(f"Did not find {uinput} in list of airports")
