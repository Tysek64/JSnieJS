import datetime

class TimeSeries:
    def __init__ (self, name: str, code: str, avgTime: str, unit: str, dates: list[datetime.datetime], values: list[float | None]) -> None:
        self.name: str = name
        self.code: str = code
        self.avgTime: str = avgTime
        self.unit: str = unit
        self.dates: list[datetime.datetime] = dates
        self.values: list[float | None] = values

    def __repr__ (self) -> str:
        return f'''TimeSeries {{
    name = {self.name}
    code = {self.code}
    avgTime = {self.avgTime}
    unit = {self.unit}
    dates = {str(self.dates)}
    values = {str(self.values)}
}}'''

    def __str__(self) -> str:
        return f'''TimeSeries {{
    name = {self.name}
    code = {self.code}
    avgTime = {self.avgTime}
    unit = {self.unit}
    dates = {str(len(self.dates))} record(s)
    values = {str(len(self.values))} record(s)
}}'''


    def __getitem__ (self, key: int | slice | datetime.date | datetime.datetime) \
            -> (tuple[datetime.datetime | list[datetime.datetime], float | list[float | None] | None]
                                                 | tuple[list[datetime.datetime], list[float | None]]
                                                 | list[float | None]):
        if isinstance(key, int) or isinstance(key, slice):
            return self.dates[key], self.values[key]
        elif isinstance(key, datetime.datetime):
            if key not in self.dates:
                raise KeyError(f'No measurements for datetime {key}')
            return [val for date, val in zip(self.dates, self.values) if date == key]
        elif isinstance(key, datetime.date):
            if key not in [date.date() for date in self.dates]:
                raise KeyError(f'No measurements for date {key}')
            return [val for date, val in zip(self.dates, self.values) if date.date() == key]
        raise TypeError(f'TimeSeries indices must be integers, slices, date or datetimes, not {type(key)}')

    @property
    def mean (self) -> None | float:
        goodValues: list[float] = [val for val in self.values if val is not None]
        return None if len(goodValues) == 0 else (sum(goodValues) / len(goodValues))

    @property
    def stddev (self) -> None | float:
        import math
        goodValues: list[float] = [val for val in self.values if val is not None]
        avg: float | None = self.mean
        if avg is None:
            return None
        return None if len(goodValues) <= 1 else (math.sqrt(sum([((elem - avg) ** 2) for elem in goodValues]) / len(goodValues)))

    def append(self, date: datetime.datetime, measurement: None | float):
        self.dates.append(date)
        self.values.append(measurement)

def readMetadata(buffer: list, metadata: dict) -> None:
    for station in metadata.values():
        buffer.append(TimeSeries(station[1], station[0], station[2], station[3], [], []))

def readCSVtoTS (data: tuple) -> list[TimeSeries]:
    result: list = list()
    readMetadata(result, data[0])
    for date, measurements in data[1].items():
        for index, m in enumerate(measurements):
            result[index].append(datetime.datetime.strptime(date, '%m/%d/%y %H:%M'), m)

    return result

def read_to_ts(path: str) -> list[TimeSeries]:
    from l5.z1 import read_data
    from pathlib import Path
    return readCSVtoTS(read_data(Path(path), header_split=6))

if __name__ == '__main__':
    testList: list[TimeSeries] = read_to_ts('measurements/l9Tests/2023_C6H6_1g2.csv')
    test: TimeSeries = testList[-1]
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
