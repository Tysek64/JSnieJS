import peewee
import argparse
from tables_orm import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('baseName', help='Database name')
    args = parser.parse_args()

    db.init(args.baseName + '.db')

    db.connect()
    db.create_tables([Station, Rental])