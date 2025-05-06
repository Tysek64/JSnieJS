import datetime

class TimeSeries:
    def __init__ (self, name, code, avgTime, unit, dates: list[datetime], values: list[float | None]):
        self.name = name
        self.code = code
        self.avgTime = avgTime
        self.unit = unit
        self.dates = dates
        self.values = values

    def __repr__ (self):
        return '''TimeSeries {
    name = ''' + self.name + '''
    code = ''' + self.code + '''
    avgTime = ''' + self.avgTime + '''
    unit = ''' + self.unit + '''
    dates = ''' + str(self.dates) + '''
    values = ''' + str(self.values) + '''
}'''
    def __getitem__ (self, key):
        if isinstance(key, int) or isinstance(key, slice):
            return (self.dates[key], self.values[key])
        elif isinstance(key, datetime.datetime):
            if key not in self.dates:
                raise ValueError('No measurements for datetime ' + str(key))
            return [val for date, val in zip(self.dates, self.values) if date == key]
        elif isinstance(key, datetime.date):
            if key not in [date.date() for date in self.dates]:
                raise ValueError('No measurements for date ' + str(key))
            return [val for date, val in zip(self.dates, self.values) if date.date() == key]

    @property
    def mean (self):
        goodValues = [val for val in self.values if val is not None]
        return None if len(goodValues) == 0 else (sum(goodValues) / len(goodValues))

    @property
    def stddev (self):
        import math
        goodValues = [val for val in self.values if val is not None]
        avg = self.mean
        return None if len(goodValues) == 0 else (math.sqrt(sum([((elem - avg) ** 2) for elem in goodValues]) / (len(goodValues) - 1)))

def readCSVtoTS (data):
    result = list()
    for station in data[0].values():
        result.append(TimeSeries(station[1], station[0], station[2], station[3], [], []))
    for date, measurements in data[1].items():
        for index, m in enumerate(measurements):
            result[index].dates.append(datetime.datetime.strptime(date, '%m/%d/%y %H:%M'))
            result[index].values.append(m)

    return result

if __name__ == '__main__':
    import l5.z1
    testList = readCSVtoTS(l5.z1.read_data('measurements/2023_C6H6_1g.csv', header_split=6))
    test = testList[-1]
    print(test[0:2])
    print(test[datetime.date(2023, 1, 1)])
    print(test[datetime.datetime(2023, 1, 1, hour=1, minute=0)])
    try:
        print(test[datetime.date(2023, 1, 2)])
    except Exception as e:
        print(type(e), e)
    try:
        print(test[datetime.datetime(2023, 1, 1, hour=1, minute=30)])
    except Exception as e:
        print(type(e), e)
    print(test.mean)
    print(test.stddev)
