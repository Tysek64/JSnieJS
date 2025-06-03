import abc
from TimeSeries import TimeSeries, readCSVtoTS

class SeriesValidator(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def analyze(self, series: TimeSeries) -> list[str]:
        pass

class OutlierDetector(SeriesValidator):
    k: int = 3

    def analyze(self, series: TimeSeries) -> list[str]:
        avg: None | float = series.mean
        dev: None | float = series.stddev
        if avg is None or dev is None:
            return []

        return [f'On {date} the measured value exceeded the average of {avg} by over {self.k * dev} and was {val}' for date, val in zip(series.dates, series.values) if val is not None and (abs(val - avg) > self.k * dev)]

class ZeroSpikeDetector(SeriesValidator):
    def analyze(self, series: TimeSeries) -> list[str]:
        import datetime

        zeroStreak: int = 0
        currentStreak: list[tuple[datetime.datetime, float | None]] = []
        addStreak: bool = False
        result: list[str] = []
        for date, val in zip(series.dates, series.values):
            if val == 0 or val is None:
                zeroStreak += 1
                currentStreak.append((date, val))
            else:
                if addStreak:
                    result.append(f'In range of dates {currentStreak[0][0]} ~ {currentStreak[-1][0]} the values mesured were: {[val[1] for val in currentStreak]}')
                zeroStreak = 0
                currentStreak = []
                addStreak = False
            if zeroStreak == 3:
                addStreak = True
        return result

class ThresholdDetector(SeriesValidator):
    def __init__(self, threshold: float = 6) -> None:
        self.threshold: float = threshold

    def analyze(self, series: TimeSeries) -> list[str]:
        return [f'On {date} the measured value exceeded the threshold of {self.threshold} and was {val}' for date, val in zip(series.dates, series.values) if val is not None and (val > self.threshold)]

class CompositeValidator(SeriesValidator):
    def __init__(self, validator1: SeriesValidator, validator2: SeriesValidator) -> None:
        self.val1: SeriesValidator = validator1
        self.val2: SeriesValidator = validator2

    def analyze(self, series: TimeSeries) -> list[str]:
        return self.val1.analyze(series) + self.val2.analyze(series)

if __name__ == '__main__':
    import l5.z1
    from pathlib import Path
    testList: list[TimeSeries] = readCSVtoTS(l5.z1.read_data(Path('measurements/2023_C6H6_1g.csv'), header_split=6))
    test: TimeSeries = testList[-1]
    OutlierDetector.k = 5
    for message in CompositeValidator(OutlierDetector(), CompositeValidator(ZeroSpikeDetector(), ThresholdDetector(10))).analyze(test):
        print(message)
