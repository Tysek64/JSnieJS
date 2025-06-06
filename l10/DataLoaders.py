import sqlite3
from abc import abstractmethod
import datetime

class DataLoader:
    @abstractmethod
    def load_data(self):
        pass

    @abstractmethod
    def update_stats(self, station_name):
        pass

class SQLiteLoader(DataLoader):
    def __init__(self, ctx):
        self.ctx = ctx
        self.connection = None
        self.cursor = None

    def load_data(self):
        from pathlib import Path
        path = Path(self.ctx.ui.databaseSelector.text())
        self.connection = sqlite3.connect(path)
        self.cursor = self.connection.cursor()
        stations = self.cursor.execute('SELECT station_name FROM Stations ORDER BY station_name')
        for station in stations:
            self.ctx.ui.stationList.addItem(str(station[0]))

    def update_stats(self, station_name):
        # SQL injection?

        if self.cursor is None:
            return

        self.ctx.ui.exampleRentals.clear()
        #print('updating')
        self.cursor.execute(f"SELECT AVG(end_time - start_time) FROM Rentals RIGHT JOIN "
                            f"Stations ON Rentals.rental_station = Stations.station_id WHERE station_name='{station_name}'")
        avg_time_begin = self.cursor.fetchone()
        if avg_time_begin != (None,):
            self.ctx.ui.avgTimeStart.setText(str(round(avg_time_begin[0])))

        self.cursor.execute(
            f"SELECT AVG(end_time - start_time) FROM Rentals RIGHT JOIN "
                            f"Stations ON Rentals.return_station = Stations.station_id WHERE station_name='{station_name}'")
        avg_time_end = self.cursor.fetchone()
        if avg_time_end != (None,):
            self.ctx.ui.avgEndTime.setText(str(round(avg_time_end[0])))
        self.cursor.execute(f"SELECT COUNT(*) FROM ("
                            f"SELECT COUNT(bike_number) FROM "
                            f"(Rentals RIGHT JOIN Stations AS BeginStations "
                            f"ON Rentals.rental_station = BeginStations.station_id) "
                            f"RIGHT JOIN Stations AS EndStations "
                            f"ON Rentals.return_station = EndStations.station_id "
                            f"WHERE EndStations.station_name='{station_name}' "
                            f"OR BeginStations.station_name='{station_name}' "
                            f"GROUP BY bike_number)")
        distinct_bikes = self.cursor.fetchone()
        if distinct_bikes != (None,):
            #print(distinct_bikes)
            self.ctx.ui.differentBikes.setText(str(distinct_bikes[0]))

        self.cursor.execute(f"SELECT rental_id, bike_number, start_time, end_time, BeginStations.station_name, EndStations.station_name "
                            f"FROM (Rentals RIGHT JOIN Stations AS BeginStations ON Rentals.rental_station = BeginStations.station_id) "
                            f"RIGHT JOIN Stations AS EndStations ON Rentals.return_station=EndStations.station_id "
                            f"WHERE EndStations.station_name='{station_name}' OR BeginStations.station_name='{station_name}' "
                            f"LIMIT 15")
        results = self.cursor.fetchall()

        for row in results:
            buff = f"{row[0]}\t{row[1]}\t{datetime.date.fromtimestamp(row[2])}\t{datetime.date.fromtimestamp(row[3])}\t{row[4]}\t{row[5]}"
            self.ctx.ui.exampleRentals.addItem(buff)


    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection is not None:
            self.connection.close()

# tu dopisz
class ORMLoader(DataLoader):
    pass