import argparse
import datetime
import csv
import random
import math
import z1
import z2
import logging
import pathlib

def logBytesRead (line):
    logger.debug('Read ' + str(len(line)) + ' bytes')
    return line

def getValidCodes (csvFile, startDate, endDate):
    codes = csvFile[1]
    validCodes = {code: False for code in codes}
    for line in csvFile[6:]:
        measurementDate = datetime.datetime.strptime(line[0], '%m/%d/%y %H:%M')
        if measurementDate <= endDate and measurementDate >= startDate:
            for code, value in zip(codes[1:], line[1:]):
                validCodes[code] |= (value != '')
    return validCodes

def getValidFiles (quantity, frequency):
    return [[logBytesRead(line) for line in csv.reader(open(v, mode='r'))] for k, v in z2.group_measurment_files_by_key(pathlib.Path('measurements')).items() if k[1] == quantity and k[2] == frequency]

def randName (args):
    def getName (code):
        for elem in filter(lambda x: x['Kod stacji'] == code, z1.read_metadata(pathlib.Path('stacje.csv'))):
            return (elem['Nazwa stacji'], elem['Adres'])

    validCodes = list()
    for file in getValidFiles(args.quantity, args.frequency):
        validCodes.extend([k for k, v in getValidCodes(file, args.startDate, args.endDate).items() if v])

    print(getName(validCodes[random.randint(0, len(validCodes) - 1)]))

def stats (args):
    series = list()
    for file in getValidFiles(args.quantity, args.frequency):
        validCodes = getValidCodes(file, args.startDate, args.endDate)
        if args.stationName in validCodes:
            index = list(validCodes.keys()).index(args.stationName)
            for line in file[6:]:
                measurementDate = datetime.datetime.strptime(line[0], '%m/%d/%y %H:%M')
                if measurementDate <= args.endDate and measurementDate >= args.startDate:
                    series.append(float(line[index]))

    avg = sum(series) / len(series)
    dev = math.sqrt(sum([((elem - avg) ** 2) for elem in series]) / (len(series) - 1))
    print(avg, dev)

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
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

    args = parser.parse_args()
    args.func(args)
