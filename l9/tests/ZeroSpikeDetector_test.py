import pytest
import sys

sys.path.append('..')
sys.path.append('.')

from TimeSeries import TimeSeries
from Validators import ZeroSpikeDetector

def test_normal():
    from datetime import date
    testSeries = TimeSeries('name', 'code', '24g', 'unit', [date(2025, 9, i) for i in range(1, 8)], [
        10.0,
        11.0,
        10.5,
        12.0,
        10.5,
        11.0,
        10.0
    ])

    assert len(ZeroSpikeDetector().analyze(testSeries)) == 0

def test_twoZeros():
    from datetime import date
    testSeries = TimeSeries('name', 'code', '24g', 'unit', [date(2025, 9, i) for i in range(1, 8)], [
        10.0,
        11.0,
        10.5,
        12.0,
        0.0,
        0.0,
        10.0
    ])

    result = ZeroSpikeDetector().analyze(testSeries)
    assert len(result) == 0

def test_threeZeros():
    from datetime import date
    testSeries = TimeSeries('name', 'code', '24g', 'unit', [date(2025, 9, i) for i in range(1, 8)], [
        10.0,
        11.0,
        10.5,
        0.0,
        0.0,
        0.0,
        10.0
    ])

    result = ZeroSpikeDetector().analyze(testSeries)
    assert len(result) == 1
    assert '[0.0, 0.0, 0.0]' in result[0]

def test_threeNCZeros():
    from datetime import date
    testSeries = TimeSeries('name', 'code', '24g', 'unit', [date(2025, 9, i) for i in range(1, 8)], [
        10.0,
        11.0,
        0.0,
        10.5,
        0.0,
        0.0,
        10.0
    ])

    result = ZeroSpikeDetector().analyze(testSeries)
    assert len(result) == 0

def test_fourZeros():
    from datetime import date
    testSeries = TimeSeries('name', 'code', '24g', 'unit', [date(2025, 9, i) for i in range(1, 8)], [
        10.0,
        11.0,
        0.0,
        0.0,
        0.0,
        0.0,
        10.0
    ])

    result = ZeroSpikeDetector().analyze(testSeries)
    assert len(result) == 1
    assert '[0.0, 0.0, 0.0, 0.0]' in result[0]

def test_fourNCZeros():
    from datetime import date
    testSeries = TimeSeries('name', 'code', '24g', 'unit', [date(2025, 9, i) for i in range(1, 8)], [
        10.0,
        0.0,
        0.0,
        10.5,
        0.0,
        0.0,
        10.0
    ])

    result = ZeroSpikeDetector().analyze(testSeries)
    assert len(result) == 0

def test_twoNones():
    from datetime import date
    testSeries = TimeSeries('name', 'code', '24g', 'unit', [date(2025, 9, i) for i in range(1, 8)], [
        10.0,
        11.0,
        10.5,
        12.0,
        None,
        None,
        10.0
    ])

    result = ZeroSpikeDetector().analyze(testSeries)
    assert len(result) == 0

def test_threeNones():
    from datetime import date
    testSeries = TimeSeries('name', 'code', '24g', 'unit', [date(2025, 9, i) for i in range(1, 8)], [
        10.0,
        11.0,
        10.5,
        None,
        None,
        None,
        10.0
    ])

    result = ZeroSpikeDetector().analyze(testSeries)
    assert len(result) == 1
    assert '[None, None, None]' in result[0]

def test_threeNCNones():
    from datetime import date
    testSeries = TimeSeries('name', 'code', '24g', 'unit', [date(2025, 9, i) for i in range(1, 8)], [
        10.0,
        11.0,
        None,
        10.5,
        None,
        None,
        10.0
    ])

    result = ZeroSpikeDetector().analyze(testSeries)
    assert len(result) == 0

def test_fourNones():
    from datetime import date
    testSeries = TimeSeries('name', 'code', '24g', 'unit', [date(2025, 9, i) for i in range(1, 8)], [
        10.0,
        11.0,
        None,
        None,
        None,
        None,
        10.0
    ])

    result = ZeroSpikeDetector().analyze(testSeries)
    assert len(result) == 1
    assert '[None, None, None, None]' in result[0]

def test_fourNCNones():
    from datetime import date
    testSeries = TimeSeries('name', 'code', '24g', 'unit', [date(2025, 9, i) for i in range(1, 8)], [
        10.0,
        None,
        None,
        10.5,
        None,
        None,
        10.0
    ])

    result = ZeroSpikeDetector().analyze(testSeries)
    assert len(result) == 0

def test_zerosAndNones():
    from datetime import date
    testSeries = TimeSeries('name', 'code', '24g', 'unit', [date(2025, 9, i) for i in range(1, 8)], [
        10.0,
        11.0,
        10.5,
        None,
        0.0,
        None,
        10.0
    ])

    result = ZeroSpikeDetector().analyze(testSeries)
    assert len(result) == 1
    assert '[None, 0.0, None]' in result[0]

def test_zerosAndNones2():
    from datetime import date
    testSeries = TimeSeries('name', 'code', '24g', 'unit', [date(2025, 9, i) for i in range(1, 8)], [
        10.0,
        11.0,
        0.0,
        None,
        0.0,
        None,
        10.0
    ])

    result = ZeroSpikeDetector().analyze(testSeries)
    assert len(result) == 1
    assert '[0.0, None, 0.0, None]' in result[0]

