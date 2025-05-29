import pytest

from TimeSeries import TimeSeries
from Validators import ZeroSpikeDetector
from datetime import date

class TestClass:
    @pytest.mark.parametrize('contents, resLen', [
        ([10.0, 11.0, 10.5, 12.0, 10.5, 11.0, 10.0], 0),
        ([10.0, 11.0, 10.5, 12.0,  0.0,  0.0, 10.0], 0),
        ([10.0, 11.0, 10.5,  0.0,  0.0,  0.0, 10.0], 1),
        ([10.0, 11.0,  0.0, 10.5,  0.0,  0.0, 10.0], 0),
        ([10.0, 11.0,  0.0,  0.0,  0.0,  0.0, 10.0], 1),
        ([10.0,  0.0,  0.0, 10.5,  0.0,  0.0, 10.0], 0),
        ([10.0, 11.0, 10.5, 12.0, None, None, 10.0], 0),
        ([10.0, 11.0, 10.5, None, None, None, 10.0], 1),
        ([10.0, 11.0, None, 10.5, None, None, 10.0], 0),
        ([10.0, 11.0, None, None, None, None, 10.0], 1),
        ([10.0, None, None, 10.5, None, None, 10.0], 0),
        ([10.0, 11.0, 10.5, None,  0.0, None, 10.0], 1),
        ([10.0, 11.0,  0.0, None,  0.0, None, 10.0], 1),
    ])
    def test(self, contents, resLen):
        testSeries = TimeSeries('name', 'code', '24g', 'unit', [date(2025, 9, i) for i in range(1, 8)], contents)

        result = ZeroSpikeDetector().analyze(testSeries)
        assert len(result) == resLen
        if resLen > 0:
            assert str([x for x in contents if x == 0 or x is None]) in result[0]
