import csv
import datetime
import math
import pathlib
import random
import z1
import z2
from z5log import get_default_logger

def getValidCodes (csvFile, startDate, endDate):
    try:
        codes = csvFile[1]
        validCodes = {code: False for code in codes}
        for line in csvFile[6:]:
            measurementDate = datetime.datetime.strptime(line[0], '%m/%d/%y %H:%M')
            if measurementDate <= endDate and measurementDate >= startDate:
                for code, value in zip(codes[1:], line[1:]):
                    validCodes[code] |= (value != '')
        return validCodes
    except IndexError:
        get_default_logger().error('Nieprawidlowy format pliku z pomiarami!')
        return {}

def getValidFiles (measurements, quantity, frequency):
    result = list()
    try:
        for k, v in z2.group_measurment_files_by_key(measurements).items():
            if k[1] == quantity and k[2] == frequency:
                singleFile = list()
                file = open(v, mode='r')
                get_default_logger().info('Otwarto plik ' + str(v))
                csvReader = csv.reader(file)
                for line in csvReader:
                    singleFile.append(line)
                    get_default_logger().debug('Odczytano ' + str(sum([len(x) for x in line])) + ' bajtow z pliku ' + str(v))
                result.append(singleFile)
                file.close()
                get_default_logger().info('Zamknieto plik ' + str(v))
        if len(result) == 0:
            
            get_default_logger().warning('Bledne parametry podane! Nie znaleziono pomiarow dla wielkosci ' + quantity + ' i czestotliwosci ' + frequency + '!')
    except OSError:
        get_default_logger().error('Nie znaleziono katalogu z pomiarami w lokalizacji ' + str(measurements) + '!')
    return result

    #return [[line for line in csv.reader(open(v, mode='r'))] for k, v in z2.group_measurment_files_by_key(pathlib.Path('measurements')).items() if k[1] == quantity and k[2] == frequency]

def randName (quantity, frequency, startDate, endDate, measurements, metadata):
    def getName (code):
        get_default_logger().info('Otwarto plik ' + str(metadata))
        for elem in filter(lambda x: x['Kod stacji'] == code, z1.read_metadata(pathlib.Path(metadata))):
            return (elem['Nazwa stacji'], elem['Adres'])

    validCodes = list()
    for file in getValidFiles(measurements, quantity, frequency):
        validCodes.extend([k for k, v in getValidCodes(file, startDate, endDate).items() if v])

    if len(validCodes) == 0:
        get_default_logger().warning('Nie znaleziono pomiarow w przedziale ' + str(startDate) + ' ~ ' + str(endDate) + '!')
    else:
        try:
            print(getName(validCodes[random.randint(0, len(validCodes) - 1)]))
            get_default_logger().info('Zamknieto plik ' + str(metadata))
        except OSError:
            get_default_logger().error('Nie znaleziono pliku z metadanymi w lokalizacji ' + str(metadata) + '!')

def stats (stationName, quantity, frequency, startDate, endDate, measurements, metadata):
    series = list()
    for file in getValidFiles(measurements, quantity, frequency):
        validCodes = getValidCodes(file, startDate, endDate)
        if stationName in validCodes:
            index = list(validCodes.keys()).index(stationName)
            for line in file[6:]:
                measurementDate = datetime.datetime.strptime(line[0], '%m/%d/%y %H:%M')
                if measurementDate <= endDate and measurementDate >= startDate:
                    series.append(float(line[index]))

    if len(series) == 0:
        get_default_logger().warning('Nie znaleziono pomiarow dla stacji ' + stationName + ' w przedziale ' + str(startDate) + ' ~ ' + str(endDate) + '!')
    else:
        avg = sum(series) / len(series)
        dev = math.sqrt(sum([((elem - avg) ** 2) for elem in series]) / (len(series) - 1))
        print(avg, dev)

