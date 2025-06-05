import peewee

db = peewee.SqliteDatabase(None)

class Station(peewee.Model):
    stationID = peewee.IntegerField(primary_key=True)
    stationName = peewee.CharField()

    class Meta:
        database = db

class Rental(peewee.Model):
    rentalID = peewee.IntegerField(primary_key=True)
    bikeNumber = peewee.IntegerField()
    startTime = peewee.DateTimeField()
    endTime = peewee.DateTimeField()
    rentalStation = peewee.ForeignKeyField(Station, backref='rentals')
    returnStation = peewee.ForeignKeyField(Station, backref='rentals')

    class Meta:
        database = db
