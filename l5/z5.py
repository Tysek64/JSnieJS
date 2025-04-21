import argparse
import csv
import datetime
import logging
import math
import pathlib
import random
import sys
import z1
import z2

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

logger = logging.getLogger(__name__)

class LevelFilter (logging.Filter):
    def __init__ (self, low, high):
        self._low = low
        self._high = high
        logging.Filter.__init__(self)
    def filter (self, record):
        return self._low <= record.levelno <= self._high

def configureLogging ():
    logging.basicConfig(filename='/dev/null', level=logging.DEBUG)
    formatter = logging.Formatter('%(levelname)s\t- %(message)s')

    stderrHandler = logging.StreamHandler(sys.stderr)
    stderrHandler.setLevel(logging.ERROR)
    stderrHandler.setFormatter(formatter)

    stdoutHandler = logging.StreamHandler(sys.stdout)
    stdoutHandler.setLevel(logging.DEBUG)
    stdoutHandler.addFilter(LevelFilter(logging.DEBUG, logging.WARNING))
    stdoutHandler.setFormatter(formatter)

    logger.addHandler(stdoutHandler)
    logger.addHandler(stderrHandler)

if __name__ == '__main__':
    configureLogging()

    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(required=True)

    randParser = subparsers.add_parser('randStation')
    randParser.set_defaults(func=randName)

    statParser = subparsers.add_parser('stats')
    statParser.add_argument('stationName', help='Name of station')
    statParser.set_defaults(func=stats)

    parser.add_argument('quantity', help='Measures quantity')
    parser.add_argument('frequency', help='Frequency of measurements', choices=['1g', '24g'])
    parser.add_argument('startDate', help='Measurements\' start date', type=lambda d: datetime.datetime.strptime(d, '%Y-%m-%d'))
    parser.add_argument('endDate', help='Measurements\' end date', type=lambda d: datetime.datetime.strptime(d, '%Y-%m-%d'))

    parser.add_argument('--metadata', '-m', help='Path to file containing metadata', type=pathlib.Path, default='stacje.csv', required=False)
    parser.add_argument('--measurements', '-M', help='Path to folder containing files with measurements', type=pathlib.Path, default='measurements', required=False)

    args = parser.parse_args()
    args.func(args)
