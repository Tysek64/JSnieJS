import sqlite3
import peewee
from tables_orm import *
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
        self.ctx.ui.stationList.clear()
        path = Path(self.ctx.ui.databasePath.text())
        self.connection = sqlite3.connect(path)
        self.cursor = self.connection.cursor()
        stations = self.cursor.execute('SELECT station_name FROM Stations ORDER BY station_name')
        for station in stations:
            self.ctx.ui.stationList.addItem(str(station[0]))

    def update_stats(self, station_name):
        # SQL injection?

        if self.cursor is None:
            return

        self.ctx.ui.rentalsList.clear()
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
            self.ctx.ui.avgTimeEnd.setText(str(round(avg_time_end[0])))

        self.cursor.execute(f'''
            SELECT COUNT(rental_id), BeginStations.station_name, EndStations.station_name 
            FROM (Rentals RIGHT JOIN Stations AS BeginStations ON Rentals.rental_station = BeginStations.station_id) 
            RIGHT JOIN Stations AS EndStations ON Rentals.return_station=EndStations.station_id 
            WHERE BeginStations.station_name='{station_name}'
            GROUP BY EndStations.station_name
            ORDER BY COUNT(rental_id) DESC
            LIMIT 1
            ''')
        popular_destination = self.cursor.fetchone()
        if avg_time_end != (None,):
            self.ctx.ui.popDest.setText(popular_destination[2])

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
            self.ctx.ui.diffBikes.setText(str(distinct_bikes[0]))

        self.cursor.execute(f"SELECT rental_id, bike_number, start_time, end_time, BeginStations.station_name, EndStations.station_name "
                            f"FROM (Rentals RIGHT JOIN Stations AS BeginStations ON Rentals.rental_station = BeginStations.station_id) "
                            f"RIGHT JOIN Stations AS EndStations ON Rentals.return_station=EndStations.station_id "
                            f"WHERE EndStations.station_name='{station_name}' OR BeginStations.station_name='{station_name}' "
                            f"LIMIT 15")
        results = self.cursor.fetchall()

        for row in results:
            buff = f"{row[0]}\t{row[1]}\t{datetime.date.fromtimestamp(row[2])}\t{datetime.date.fromtimestamp(row[3])}\t{row[4]}\t{row[5]}"
            self.ctx.ui.rentalsList.addItem(buff)


    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection is not None:
            self.connection.close()

# tu dopisz
class ORMLoader(DataLoader):
    def __init__(self, ctx):
        self.ctx = ctx

    def load_data(self):
        from pathlib import Path
        self.ctx.ui.stationList.clear()
        path = Path(self.ctx.ui.databasePath.text())
        db.init(path)
        stations = sorted([station.stationName for station in Station.select()])
        for station in stations:
            self.ctx.ui.stationList.addItem(str(station))

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection is not None:
            self.connection.close()

    def update_stats(self, station_name):
        self.ctx.ui.rentalsList.clear()
        currentStation = Station.get(Station.stationName == station_name).stationID

        query = Rental.select().where(Rental.rentalStation == currentStation)
        avg = sum([row.endTime - row.startTime for row in query], datetime.timedelta(0)) / len(query)
        self.ctx.ui.avgTimeStart.setText(str(avg))

        query = Rental.select().where(Rental.returnStation == currentStation)
        avg = sum([row.endTime - row.startTime for row in query], datetime.timedelta(0)) / len(query)
        self.ctx.ui.avgTimeEnd.setText(str(avg))

        query = len(Rental.select(Rental.bikeNumber).where((Rental.rentalStation == currentStation) | (Rental.returnStation == currentStation)).distinct())
        self.ctx.ui.diffBikes.setText(str(query))

        query = Station.get(Station.stationID == Rental.select(Rental.rentalStation, Rental.returnStation, peewee.fn.Count(Rental.rentalID).alias('count')).where(Rental.rentalStation == currentStation).group_by(Rental.returnStation).order_by(peewee.fn.Count(Rental.rentalID))[-1].returnStation).stationName
        self.ctx.ui.popDest.setText(query)
    
        results = Rental.select().where((Rental.rentalStation == currentStation) | (Rental.returnStation == currentStation))

        for _, row in zip(range(15), results):
            buff = f"{row.rentalID}\t{row.bikeNumber}\t{row.startTime}\t{row.endTime}\t{Station.get(Station.stationID == row.rentalStation).stationName}\t{Station.get(Station.stationID == row.returnStation).stationName}"
            self.ctx.ui.rentalsList.addItem(buff)
