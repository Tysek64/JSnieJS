import pytest

from TimeSeries import TimeSeries
from Validators import ThresholdDetector
from datetime import date

class TestClass:
    @pytest.mark.parametrize('contents, resLen', [
        ([ 5.0,  4.0,  4.5,  3.0,  4.0,  3.3,  5.6], 0),
        ([ 5.9,  6.0,  6.1,  5.8,  6.5,  5.5,  4.0], 2),
        ([10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0], 7),
        ([-1.0, -2.0, -3.0, -4.0, -5.0, -6.0, -7.0], 0),
        ([ 0.0, None,  6.0, -6.1,  0.1, -0.1,  6.1], 1)
    ])
    def test_default(self, contents, resLen):
        testSeries = TimeSeries('name', 'code', '24g', 'unit', [date(2025, 9, i) for i, _ in enumerate(contents, start=1)], contents)

        result = ThresholdDetector().analyze(testSeries)
        assert len(result) == resLen
        if resLen > 0:
            msg = result.__iter__()
            for i in contents:
                if i is not None and i > 6.0:
                    assert str(i) in msg.__next__()

    @pytest.mark.parametrize('threshold, contents, resLen', [
        (-1.0, [ 5.0,  4.0,  4.5,  3.0,  4.0,  3.3,  5.6], 7),
        (-1.0, [ 5.9,  6.0,  6.1,  5.8,  6.5,  5.5,  4.0], 7),
        (-1.0, [10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0], 7),
        (-1.0, [-1.0, -2.0, -3.0, -4.0, -5.0, -6.0, -7.0], 0),
        (-1.0, [ 0.0, None,  6.0, -6.1,  0.1, -0.1,  6.1], 5),
        ( 0.0, [ 5.0,  4.0,  4.5,  3.0,  4.0,  3.3,  5.6], 7),
        ( 0.0, [ 5.9,  6.0,  6.1,  5.8,  6.5,  5.5,  4.0], 7),
        ( 0.0, [10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0], 7),
        ( 0.0, [-1.0, -2.0, -3.0, -4.0, -5.0, -6.0, -7.0], 0),
        ( 0.0, [ 0.0, None,  6.0, -6.1,  0.1, -0.1,  6.1], 3),
        ( 1.0, [ 5.0,  4.0,  4.5,  3.0,  4.0,  3.3,  5.6], 7),
        ( 1.0, [ 5.9,  6.0,  6.1,  5.8,  6.5,  5.5,  4.0], 7),
        ( 1.0, [10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0], 7),
        ( 1.0, [-1.0, -2.0, -3.0, -4.0, -5.0, -6.0, -7.0], 0),
        ( 1.0, [ 0.0, None,  6.0, -6.1,  0.1, -0.1,  6.1], 2),
        (10.0, [ 5.0,  4.0,  4.5,  3.0,  4.0,  3.3,  5.6], 0),
        (10.0, [ 5.9,  6.0,  6.1,  5.8,  6.5,  5.5,  4.0], 0),
        (10.0, [10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0], 6),
        (10.0, [-1.0, -2.0, -3.0, -4.0, -5.0, -6.0, -7.0], 0),
        (10.0, [ 0.0, None,  6.0, -6.1,  0.1, -0.1,  6.1], 0)
    ])
    def test_param(self, threshold, contents, resLen):
        testSeries = TimeSeries('name', 'code', '24g', 'unit', [date(2025, 9, i) for i, _ in enumerate(contents, start=1)], contents)

        result = ThresholdDetector(threshold).analyze(testSeries)
        assert len(result) == resLen
        if resLen > 0:
            msg = result.__iter__()
            for i in contents:
                if i is not None and i > threshold:
                    assert str(i) in msg.__next__()
