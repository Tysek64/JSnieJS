import sqlite3

def create_table_queries() -> list[str]:
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

def create_table_schema(name: str) -> None:
    con = sqlite3.connect(f'{name}.db')
    cur = con.cursor()

    print('Setting up tables...')
    create_queries = create_table_queries()
    for query in create_queries:
        cur.execute(query)

    print(f'\033[92mSucessfully created database {name}.db\033[0m')
    con.close()

def insert_into(con: sqlite3.Connection, cursor: sqlite3.Cursor,
                table: str, data: list):
    if len(data) <= 0 or len(data[0]) < 1:
        return
    data_scheme = (len(data[0]) - 1) * '?, '
    cursor.executemany(f'INSERT OR IGNORE INTO {table} VALUES({data_scheme}?)', data)
    con.commit()

def insert_into_db(database: str, stations: list[tuple], rentals: list[tuple]) -> None:
    con = sqlite3.connect(database)
    cur = con.cursor()
    insert_into(con, cur, 'Stations', stations)
    insert_into(con, cur, 'Rentals', rentals)
    con.close()
