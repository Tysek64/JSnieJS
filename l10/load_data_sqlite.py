import argparse

from data_parse import *
from db_utils import insert_into_db
from copy import deepcopy

def main():
    parser = argparse.ArgumentParser(
        description="""
           This is a script that inserts data into databases table from .csv file.
           """,
        usage="python load_data_sqlite.py FILENAME DATABASE")
    parser.add_argument('FILENAME', help='Name of file to be load')
    parser.add_argument('DATABASE', help='Name of the database to insert into')
    args = parser.parse_args()

    parsed_csv = parse_csv(args.FILENAME)
    stations = {}
    parse_stations(parsed_csv, stations)
    rentals = parse_rentals_sqlite(parse_rentals(parsed_csv, stations))
    stations = parse_stations_sqlite(stations)
    insert_into_db(args.DATABASE + '.db', stations, rentals)


if __name__ == '__main__':
    main()