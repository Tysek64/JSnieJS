import sqlite3

def get_create_table_queries() -> list[str]:
    return [
        'CREATE TABLE IF NOT EXISTS Stations('
            'station_id INT PRIMARY KEY, '
            'station_name TEXT UNIQUE)',

        'CREATE TABLE IF NOT EXISTS Rentals('
            'rental_id INT PRIMARY KEY, '
            'bike_number INT, '
            'start_time REAL, '
            'end_time REAL, '
            'rental_station INT, '
            'return_station INT, '
            'CONSTRAINT fk_rental_station '
            'FOREIGN KEY (rental_station) REFERENCES Stations(station_id), '
            'CONSTRAINT fk_return_station '
            'FOREIGN KEY (return_station) REFERENCES Stations(station_id)'
            ')'

    ]

def print_query(cursor: sqlite3.Cursor, query: str) -> None:
    cursor.execute(query)
    res = cursor.fetchall()
    for result in res:
        print(result)

def insert_queries(con: sqlite3.Connection, cursor: sqlite3.Cursor,
                   table: str, data: list):
    if len(data) < 0 or len(data[0]) < 1:
        return
    data_scheme = (len(data[0]) - 1) * '?, '
    cursor.executemany(f'INSERT OR IGNORE INTO {table} VALUES({data_scheme} ?)', data)
    con.commit()

if __name__ == '__main__':
    from data_parse import *
    from db_utils import *
    parsedCsv1 = parse_csv('dane/historia_przejazdow_2021-01.csv')
    parsedCsv2 = parse_csv('dane/historia_przejazdow_2021-02.csv')
    station_buffer = {}
    stations1 = parse_stations(parsedCsv1, station_buffer)
    stations2 = parse_stations(parsedCsv2, station_buffer)



    rentals1 = parse_rentals(parsedCsv1, station_buffer)
    rentals2 = parse_rentals(parsedCsv2, station_buffer)
    #print(parse_rentals_sqlite(rentals2))
    # connection
    con = sqlite3.connect('test.db')
    cur = con.cursor()

    # setup
    print('Setting up tables')
    create_queries = get_create_table_queries()
    for query in create_queries:
        cur.execute(query)

    print('Initiating foreign keys')
    cur.execute( 'PRAGMA foreign_keys = ON;') # FK trzeba wlaczyc
    print('key_status: ', end='')
    print_query(cur, 'PRAGMA foreign_keys;')

    print_query(cur, 'PRAGMA foreign_key_list(Rentals);')
    print_query(cur, 'PRAGMA table_info(Rentals);')

    parsed_stations = parse_stations_sqlite(station_buffer)
    #insert_into(con, cur, 'Stations', parsed_stations)

    print_query(cur, 'SELECT * FROM Rentals LIMIT 5')

    con.close()