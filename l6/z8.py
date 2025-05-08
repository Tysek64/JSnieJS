from z2 import TimeSeries

class SimpleReporter:
    def analyze(self, series: TimeSeries) -> list[str]:
        return [f"Info: {series.name} at {series.code} has mean = {series.mean}"]