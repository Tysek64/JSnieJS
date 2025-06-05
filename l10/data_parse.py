import csv
import datetime
import copy
import peewee

def parse_csv(filename):
    conversions = [int, int, lambda d: datetime.datetime.strptime(d, '%Y-%m-%d %H:%M:%S'), lambda d: datetime.datetime.strptime(d, '%Y-%m-%d %H:%M:%S'), str, str, int]
    with open(filename, mode='r', encoding='utf8') as file: # bez encodingu mi nie dziala
        csvReader = csv.DictReader(file)
        return [{k: conv(v) for (k, v), conv in zip(line.items(), conversions)} for line in csvReader]

# stations - slownik {nazwa stacji: id stacji} stacji, ktore juz sa w bazie
def parse_stations(rawData, stations=None):
    if stations is None:
        stations = {}

    result = []
    UID = 0 if len(stations.values()) == 0 else max(stations.values()) + 1
    for line in rawData:
        if line['Stacja wynajmu'] not in stations.keys():
            stations[line['Stacja wynajmu']] = UID
            result.append({'stationID': UID, 'stationName': line['Stacja wynajmu']})
            UID += 1

        if line['Stacja zwrotu'] not in stations.keys():
            stations[line['Stacja zwrotu']] = UID
            result.append({'stationID': UID, 'stationName': line['Stacja zwrotu']})
            UID += 1

    return result

# stations - slownik {nazwa stacji: id stacji} stacji, ktore juz sa w bazie
# rentals  - lista id wypozyczen, ktore juz sa w bazie
def parse_rentals(rawData, stations=None, rentals=None):

    if stations is None:
        stations = {}
    if rentals is None:
        rentals = {}

    result = []
    nameTranslation = {
        'UID wynajmu': 'rentalID',
        'Numer roweru': 'bikeNumber',
        'Data wynajmu': 'startTime',
        'Data zwrotu': 'endTime',
        'Stacja wynajmu': 'rentalStation',
        'Stacja zwrotu': 'returnStation'
    }

    for line in rawData:
        parsedLine = {}

        for k, v in line.items():
            try:
                parsedLine[nameTranslation[k]] = v
            except KeyError:
                pass

        try:
            parsedLine['rentalStation'] = stations[line['Stacja wynajmu']]
        except KeyError:
            #print(f'Nie znaleziono stacji {line['Stacja wynajmu']}!')
            continue

        try:
            parsedLine['returnStation'] = stations[line['Stacja zwrotu']]
        except KeyError:
            #print(f'Nie znaleziono stacji {line['Stacja zwrotu']}!')
            continue

        if parsedLine['rentalID'] not in rentals:
            result.append(parsedLine)
    return result

def parse_stations_sqlite(stations: dict) -> list:
    return [(v, k) for k, v in stations.items()]

def parse_rentals_sqlite(rentals: dict) -> list:
    for i, row in enumerate(rentals):
        rentals[i]['startTime'] = row['startTime'].timestamp()
        rentals[i]['endTime'] = row['endTime'].timestamp()

    return [tuple(v for v in row.values()) for row in rentals]


if __name__ == '__main__':
    parsedCsv1 = parse_csv('dane/historia_przejazdow_2021-01.csv')
    parsedCsv2 = parse_csv('dane/historia_przejazdow_2021-02.csv')

    stations1 = parse_stations(parsedCsv1)
    stations2 = parse_stations(parsedCsv2, stations1)

    rentals1 = parse_rentals(parsedCsv1, stations2)
    rentals2 = parse_rentals(parsedCsv2, stations2)

    print(len(parsedCsv1), len(parsedCsv2))
    print(len(stations1), len(stations2))

    for line in rentals1:
        print(line)
