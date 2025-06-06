import argparse
import peewee
from tables_orm import *
from data_parse import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='Path to file containing record data')
    parser.add_argument('baseName', help='Database name')
    args = parser.parse_args()

    db.init(args.baseName + '.db')

    db.connect()

    parsedCsv = parse_csv(args.filename)

    stations = parse_stations(parsedCsv, {station.stationName: station.stationID for station in Station.select()})

    Station.insert_many(stations).execute()

    stations = {station.stationName: station.stationID for station in Station.select()}
    rentals = parse_rentals(parsedCsv, stations, [rental.rentalID for rental in Rental.select()])

    Rental.insert_many(rentals).execute()
