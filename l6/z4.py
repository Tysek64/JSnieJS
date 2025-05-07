import abc
import z2

class SeriesValidator(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def analyze(self, series: z2.TimeSeries):
        pass

class OutlierDetector(SeriesValidator):
    k = 3
    def analyze(self, series: z2.TimeSeries):
        avg = series.mean
        dev = series.stddev
        return [f'On {date} the measured value exceeded the average of {avg} by over {self.k * dev} and was {val}' for date, val in zip(series.dates, series.values) if val is not None and (abs(val - avg) > self.k * dev)]

class ZeroSpikeDetector(SeriesValidator):
    def analyze(self, series: z2.TimeSeries):
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
    def analyze(self, series: z2.TimeSeries, threshold: float):
        return [f'On {date} the measured value exceeded the threshold of {threshold} and was {val}' for date, val in zip(series.dates, series.values) if val is not None and (val > threshold)]

if __name__ == '__main__':
    import l5.z1
    testList = z2.readCSVtoTS(l5.z1.read_data('measurements/2023_C6H6_1g.csv', header_split=6))
    test = testList[-1]
    for message in OutlierDetector().analyze(test):
        print(message)
    for message in ZeroSpikeDetector().analyze(test):
        print(message)
    for message in ThresholdDetector().analyze(test, 6):
        print(message)
