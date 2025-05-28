from pathlib import Path
from LazyRead import LazyMerger, LazyReader
from types import TracebackType

class Measurements:
    from TimeSeries import TimeSeries
    from Validators import SeriesValidator
    def __init__(self, data_path: Path) -> None:
        files: list[Path] = list(data_path.glob('*.csv'))
        readers: list[LazyReader] = [LazyReader(f, header_split=6) for f in files]
        self.merger: LazyMerger = LazyMerger(readers)
        self.merger.open()

    def __contains__(self, parameter_name: str) -> bool:
        return self.merger.__contains__(parameter_name)

    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> None:
        self.merger.close()

    def __len__(self) -> int:
        return len(self.merger)

    def get_by_parameter(self, param_name: str) -> list[TimeSeries]:
        return self.merger.get_by_param(param_name)

    def get_by_station(self, station_code: str) -> list[TimeSeries]:
        return self.merger.get_by_code(station_code)

    def detect_all_anomalies(self, validators: list[SeriesValidator], preload: bool = False) -> dict:
        if preload:
            for i, _ in enumerate(self.merger):
                pass

        return {series: sum([validator.analyze(series) for validator in validators], []) for series in self.merger.get_series()}



if __name__ == '__main__':
    data_path: Path = Path('./measurements/l5Tests')
    m: Measurements = Measurements(data_path)
    print(len(m))
    for _, _ in zip(range(1000), m.merger):
        pass

        '''
    print(m.merger)
    print('BaA(PM10)' in m)
    print(m.get_by_parameter('Hg(TGM)'))
    print(m.get_by_station('WmPuszczaBor'))
            '''
    import Validators, SimpleReporter
    validators: list[Validators.SeriesValidator] = [Validators.CompositeValidator(Validators.CompositeValidator(Validators.OutlierDetector(), Validators.ThresholdDetector()), Validators.CompositeValidator(Validators.ZeroSpikeDetector(), SimpleReporter.SimpleReporter()))]
    for k, v in m.detect_all_anomalies(validators, preload=False).items():
        print(k, ": ", v)
