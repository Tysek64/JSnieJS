import argparse


def main():
    parser = argparse.ArgumentParser(
        description="""
        This is a script that creates an empty DB schema in .db format.
        """,
        usage="python create_database_sqlite.py DATABASE_NAME")
    parser.add_argument('DATABASE_NAME', help='Name of database to be created')
    args = parser.parse_args()

    from db_utils import create_table_schema
    create_table_schema(args.DATABASE_NAME)

if __name__ == '__main__':
    main()