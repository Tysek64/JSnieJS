import abc
import z2

class SeriesValidator(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def analyze(self, series: z2.TimeSeries) -> list[str]:
        pass

class OutlierDetector(SeriesValidator):
    k = 3

    def analyze(self, series: z2.TimeSeries) -> list[str]:
        avg, dev = series.mean, series.stddev
        return [f'On {date} the measured value exceeded the average of {avg} by over {self.k * dev} and was {val}' for date, val in zip(series.dates, series.values) if val is not None and (abs(val - avg) > self.k * dev)]

class ZeroSpikeDetector(SeriesValidator):
    def analyze(self, series: z2.TimeSeries) -> list[str]:
        zeroStreak = 0
        currentStreak = []
        addStreak = False
        result = []
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
    def __init__(self, threshold = 6):
        self.threshold = threshold

    def analyze(self, series: z2.TimeSeries) -> list[str]:
        return [f'On {date} the measured value exceeded the threshold of {self.threshold} and was {val}' for date, val in zip(series.dates, series.values) if val is not None and (val > self.threshold)]

class CompositeValidator(SeriesValidator):
    def __init__(self, validator1: SeriesValidator, validator2: SeriesValidator):
        self.val1 = validator1
        self.val2 = validator2

    def analyze(self, series: z2.TimeSeries) -> list[str]:
        return self.val1.analyze(series) + self.val2.analyze(series)

if __name__ == '__main__':
    import l5.z1
    testList = z2.readCSVtoTS(l5.z1.read_data('measurements/2023_C6H6_1g.csv', header_split=6))
    test = testList[-1]
    OutlierDetector.k = 5
    for message in CompositeValidator(OutlierDetector(), CompositeValidator(ZeroSpikeDetector(), ThresholdDetector(10))).analyze(test):
        print(message)
