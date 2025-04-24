from z1 import read_data
from pathlib import Path
import z7tests as tests

# mozna bylo teoretycznie partialem
class BasicReader:
    def __init__(self, data_path: Path, skipped_lines: list[int], header_split: int):
        self.data_path = data_path
        self.skipped_lines = skipped_lines
        self.header_split = header_split

    def __call__(self):
        metadata, data = read_data(self.data_path, skipped_lines=self.skipped_lines,
                         header_split=self.header_split)
        return data, metadata

# ale nie byloby dziedziczenia
class SelectiveReader(BasicReader):
    def __init__(self, timeframe, station, quantity, frequency, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.date_begin, self.date_end = timeframe
        self.station = station
        self.quantity = quantity
        self.frequency = frequency

    def __call__(self):
        data = super().__call__()
        from z1 import select_from
        data = select_from(data, 'Station',
                                    condition_mdata=(lambda s: s == self.station))

        data = select_from(data, 'Chemical',
                           condition_mdata=(lambda s: s == self.quantity))
        data = select_from(data, 'Frequency',
                           condition_mdata=(lambda f: f == self.frequency))
        return data

# decorator
class test_for(object):
    def __init__(self, *args,  **kwargs):
        self.tests = args

    def __call__(self, f):
        def wrapper(reader, *args, **kwargs):
            try:
                data, metadata = reader()
                from z1 import data_to_human_readable
                for test in self.tests:
                    print(test.__name__, " completed with result:\n", data_to_human_readable(test(data, metadata)
                                                                                             , metadata), sep="")
                print(f"All test have been completed with file {reader.data_path}")
                f(data, *args, **kwargs)
            except OSError as e:
                raise OSError(e.__repr__())

        return wrapper

@test_for(tests.null_test, tests.delta_test(1),
          tests.threshold_test(None, 0.5))
def test_file(data: tuple) -> None:
    pass

from datetime import date
from pathlib import Path
def test_files_by_parameters(measurements_path: Path, station: str, infix: str, frequency: str,
                             year: str, quantity=None) -> None:
    quantity = quantity if quantity is not None else infix
    from z2 import group_measurment_files_by_key
    files = [v for k, v in group_measurment_files_by_key(measurements_path).items()
           if year == k[0] and infix == k[1] and frequency == k[2]]

    for file in files:
        reader = SelectiveReader((None, None), station,
                                 quantity, frequency,
                                 file, skipped_lines=[], header_split=6)
        test_file(reader)



if __name__ == '__main__':
    test_path = Path('./measurements/2023_PrekursoryZielonka_1g.csv')
    #test_path = Path('./measurements/2023_formaldehyd_1g.csv')
    '''
    test_file(SelectiveReader((None, None), 'KpZielBoryTu',
                              '1buten', '1g',
                              test_path, skipped_lines=[], header_split=6))
    '''
    test_files_by_parameters(Path('measurements'), 'KpZielBoryTu', 'PrekursoryZielonka', '1g',
                             '2023', '1buten')

