import csv
import re



columns = {'from': 'From', 'to': 'To'}
directional = False

with open('flights.csv', 'r') as csvfile:
    flightdata = [{list(columns.keys())[list(columns.values()).index(k)]: v for k, v in r.items() if k in list(columns.values())} for r in csv.DictReader(csvfile, delimiter = ',', skipinitialspace = True)]


for i in range(len(flightdata)):
    for col in columns:
        for x in ['from', 'to']:
            flightdata[i][x] = re.search('(?<![A-Z0-9])([A-Z0-9]){3}(?![A-Z0-9])', flightdata[i][x]).group()


routes = []
airports = {}

for flight in flightdata:
    if '{}/{}'.format(flight['from'], flight['to']) not in routes:
        routes.append('{}/{}'.format(flight['from'], flight['to']))
    if not directional:
        if '{}/{}'.format(flight['to'], flight['from']) not in routes:
            routes.append('{}/{}'.format(flight['to'], flight['from']))
    
    if flight['from'] not in airports:
        airports[flight['from']] = []
    if flight['to'] not in airports[flight['from']]:
        airports[flight['from']].append(flight['to'])
    if not directional:
        if flight['to'] not in airports:
            airports[flight['to']] = []
        if flight['from'] not in airports[flight['to']]:
            airports[flight['to']].append(flight['from'])


routes.sort()
airports = {k: sorted(airports[k]) for k in sorted(airports) }


while True:
    uinput = input('Input Airport (eg. LAX) or Route (eg. JFK/LAX): ').upper()
    if uinput.lower() in ['q', 'quit', 'exit']:
        break
    
    if '/' in uinput:
        if uinput in routes:
            print('Found {} in list of routes'.format(uinput))
        else:
            print('Did not find {} in list of routes'.format(uinput))
    else:
        if uinput in airports:
            print('Found {} in list of airports'.format(uinput))
            print('Found routes from {} to {}'.format(uinput, ', '.join(airports[uinput])))
        else:
            print('Did not find {} in list of airports'.format(uinput))
