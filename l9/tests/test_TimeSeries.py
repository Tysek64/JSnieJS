import datetime
from TimeSeries import read_to_ts, TimeSeries
import pytest
from Validators import OutlierDetector

class TestClass:
    test_file = read_to_ts('../measurements/l9Tests/2023_C6H6_1g2.csv')
    test_file_wNone = read_to_ts('../measurements/l9Tests/2023_C6H6_1g2None.csv')
    test_outlier_file = read_to_ts('../measurements/l9Tests/2023_C6H6_1g2Outlier.csv')
    @pytest.mark.parametrize("id, expected_output", [
        (0, (datetime.datetime(2023, 1, 1, 1, 0), 0.14732000000000001)),
        (1, (datetime.datetime(2023, 1, 1, 2, 0), 0.12078)),
        (2, (datetime.datetime(2023, 1, 1, 3, 0), 0.11809)),
        (-1, (datetime.datetime(2023, 1, 1, 3, 0), 0.11809)),
        (-2, (datetime.datetime(2023, 1, 1, 2, 0), 0.12078)),
        (-3, (datetime.datetime(2023, 1, 1, 1, 0), 0.14732000000000001))
    ])
    def test_int_index(self, id, expected_output):
        for ts in self.test_file:
            assert ts[id] == expected_output

    @pytest.mark.parametrize("id", [
        -4,
        4,
        20,
        -20
    ])
    def test_int_index_invalids(self, id):
        with pytest.raises(IndexError):
            for ts in self.test_file:
                print(ts[id])

    @pytest.mark.parametrize("slice, expected_output", [
        (slice(0, 3),
            ([datetime.datetime(2023, 1, 1, 1, 0),
             datetime.datetime(2023, 1, 1, 2, 0),
             datetime.datetime(2023, 1, 1, 3, 0)],
            [0.14732000000000001, 0.12078, 0.11809])),
        (slice(1, 2),
            ([datetime.datetime(2023, 1, 1, 2, 0)], [0.12078])),
        (slice(0, 0),
            ([], [])),
        (slice(-2, -1),
            ([datetime.datetime(2023, 1, 1, 2, 0)], [0.12078])),
        (slice(-10, None),
             ([datetime.datetime(2023, 1, 1, 1, 0),
               datetime.datetime(2023, 1, 1, 2, 0),
               datetime.datetime(2023, 1, 1, 3, 0)],
              [0.14732000000000001, 0.12078, 0.11809])),
        (slice(None, None),
         ([datetime.datetime(2023, 1, 1, 1, 0),
           datetime.datetime(2023, 1, 1, 2, 0),
           datetime.datetime(2023, 1, 1, 3, 0)],
          [0.14732000000000001, 0.12078, 0.11809])),
        (slice(-2, None),
         ([datetime.datetime(2023, 1, 1, 2, 0),
           datetime.datetime(2023, 1, 1, 3, 0)],
          [0.12078, 0.11809]))
        ])
    def test_slice_valids(self, slice, expected_output):
        for ts in self.test_file:
            assert ts[slice] == expected_output

    @pytest.mark.parametrize("date, expected_output", [
        (datetime.date(2023, 1, 1), [0.14732000000000001, 0.12078, 0.11809]),
        (datetime.datetime(2023, 1, 1, 3), [0.11809])
    ])
    def test_datetime_valids(self, date, expected_output):
        for ts in self.test_file:
            assert ts[date] == expected_output

    @pytest.mark.parametrize("date", [
        datetime.date(2023, 1, 4),
        datetime.datetime(2023, 1, 1, 4)
    ])
    def test_datetime_invalids(self, date):
        with pytest.raises(KeyError):
            for ts in self.test_file:
                ts[date]

    def test_stats(self):
        for ts in self.test_file:
            assert (round(ts.mean, 8), round(ts.stddev, 8)) == (0.12873, 0.01319091)

    def test_stats_none(self):
        for ts in self.test_file_wNone:
            assert (round(ts.mean, 8), round(ts.stddev, 8)) == (0.13405, 0.0132700)

    @pytest.mark.parametrize("k, expected_output", [
        (1, ['On 2023-01-01 03:00:00 the measured value exceeded the average '
             'of 0.4620633333333333 by over 0.4640074233841045 and was 1.11809']),
        (2, []),
        (10, [])
    ])
    def test_outlier(self, k, expected_output):
        detector = OutlierDetector()
        detector.k = k
        for ts in self.test_outlier_file:
            assert detector.analyze(ts) == expected_output
