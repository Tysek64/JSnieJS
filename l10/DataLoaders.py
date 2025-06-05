import sqlite3
from abc import abstractmethod


class DataLoader:
    @abstractmethod
    def load_data(self):
        pass

class SQLiteLoader(DataLoader):
    def __init__(self, ctx):
        self.ctx = ctx
        self.connection = None

    def load_data(self):
        from pathlib import Path
        path = Path(self.ctx.ui.databasePath.text())
        self.connection = sqlite3.connect(path)
        self.cursor = self.connection.cursor()
        stations = self.cursor.execute('SELECT station_name FROM Stations ORDER BY station_name')
        for station in stations:
            self.ctx.ui.stationList.addItem(str(station[0]))

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection is not None:
            self.connection.close()

# tu dopisz
class ORMLoader(DataLoader):
    pass