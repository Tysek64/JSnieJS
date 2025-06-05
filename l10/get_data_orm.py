import argparse
import peewee
from tables_orm import *
from data_parse import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('baseName', help='Database name')
    args = parser.parse_args()

    db.init(args.baseName + '.db')

    db.connect()

    for station in Station.select():
        print(station.stationID, station.stationName)

    for rental in Rental.select():
        print(rental.rentalID, rental.bikeNumber)
