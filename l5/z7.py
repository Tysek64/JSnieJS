from z1 import read_data
from pathlib import Path
import z7tests as tests

# decorator
class test_for(object):
    def __init__(self, *args,  **kwargs):
        self.tests = args
        self.skipped_lines = kwargs['skipped_lines']
        self.header_split = kwargs['header_split']

    def __call__(self, f):
        def wrapper(data_path, *args, **kwargs):
            try:
                metadata, data = read_data(data_path,
                                           skipped_lines=self.skipped_lines,
                                           header_split=self.header_split)

                for test in self.tests:
                    print(test.__name__, " completed with result:\n", test(data, metadata), sep="")
                print(f"All test have been completed with file {data_path}")
                f(data, *args, **kwargs)
            except OSError as e:
                raise OSError(e.__repr__())

        return wrapper

@test_for(tests.null_test, tests.delta_test(1),
          tests.threshold_test('acetylen', 4),
          skipped_lines=[], header_split=6)
def test_file(data: tuple) -> None:
    pass



if __name__ == '__main__':
    test_path = Path('./measurements/2023_PrekursoryZielonka_1g.csv')
    #test_path = Path('./measurements/2023_formaldehyd_1g.csv')
    test_file(test_path)

