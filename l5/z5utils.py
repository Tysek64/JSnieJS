import csv
import datetime
import math
import pathlib
import random
import z1
import z2
import z5log

logger = z5log.logger

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
        logger.error('Nieprawidlowy format pliku z pomiarami!')
        return {}

def getValidFiles (measurements, quantity, frequency):
    result = list()
    try:
        for k, v in z2.group_measurment_files_by_key(measurements).items():
            if k[1] == quantity and k[2] == frequency:
                singleFile = list()
                file = open(v, mode='r')
                logger.info('Otwarto plik ' + str(v))
                csvReader = csv.reader(file)
                for line in csvReader:
                    singleFile.append(line)
                    logger.debug('Odczytano ' + str(sum([len(x) for x in line])) + ' bajtow z pliku ' + str(v))
                result.append(singleFile)
                file.close()
                logger.info('Zamknieto plik ' + str(v))
        if len(result) == 0:
            
            logger.warning('Bledne parametry podane! Nie znaleziono pomiarow dla wielkosci ' + quantity + ' i czestotliwosci ' + frequency + '!')
    except OSError:
        logger.error('Nie znaleziono katalogu z pomiarami w lokalizacji ' + str(measurements) + '!')
    return result

    #return [[line for line in csv.reader(open(v, mode='r'))] for k, v in z2.group_measurment_files_by_key(pathlib.Path('measurements')).items() if k[1] == quantity and k[2] == frequency]

def randName (args):
    def getName (code):
        logger.info('Otwarto plik ' + str(args.metadata))
        for elem in filter(lambda x: x['Kod stacji'] == code, z1.read_metadata(pathlib.Path(args.metadata))):
            return (elem['Nazwa stacji'], elem['Adres'])

    validCodes = list()
    for file in getValidFiles(args.measurements, args.quantity, args.frequency):
        validCodes.extend([k for k, v in getValidCodes(file, args.startDate, args.endDate).items() if v])

    if len(validCodes) == 0:
        logger.warning('Nie znaleziono pomiarow w przedziale ' + str(args.startDate) + ' ~ ' + str(args.endDate) + '!')
    else:
        try:
            print(getName(validCodes[random.randint(0, len(validCodes) - 1)]))
            logger.info('Zamknieto plik ' + str(args.metadata))
        except OSError:
            logger.error('Nie znaleziono pliku z metadanymi w lokalizacji ' + str(args.metadata) + '!')

def stats (args):
    series = list()
    for file in getValidFiles(args.measurements, args.quantity, args.frequency):
        validCodes = getValidCodes(file, args.startDate, args.endDate)
        if args.stationName in validCodes:
            index = list(validCodes.keys()).index(args.stationName)
            for line in file[6:]:
                measurementDate = datetime.datetime.strptime(line[0], '%m/%d/%y %H:%M')
                if measurementDate <= args.endDate and measurementDate >= args.startDate:
                    series.append(float(line[index]))

    if len(series) == 0:
        logger.warning('Nie znaleziono pomiarow dla stacji ' + args.stationName + ' w przedziale ' + str(args.startDate) + ' ~ ' + str(args.endDate) + '!')
    else:
        avg = sum(series) / len(series)
        dev = math.sqrt(sum([((elem - avg) ** 2) for elem in series]) / (len(series) - 1))
        print(avg, dev)

