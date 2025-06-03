import pytest
import Validators
import SimpleReporter

from TimeSeries import TimeSeries
from Measurements import Measurements
from datetime import date
from pathlib import Path

class TestClass:
    Validators.OutlierDetector.k = 1

    @pytest.mark.parametrize('validators, shape', [
        ([SimpleReporter.SimpleReporter()], 
         [1, 1, 1, 1, 1]),
        ([SimpleReporter.SimpleReporter(), Validators.ZeroSpikeDetector()], 
         [1, 1, 2, 2, 1]),
        ([Validators.CompositeValidator(SimpleReporter.SimpleReporter(), Validators.ZeroSpikeDetector())], 
         [1, 1, 2, 2, 1]),
        ([Validators.ThresholdDetector(), Validators.ZeroSpikeDetector()], 
         [0, 0, 1, 2, 2]),
        ([Validators.CompositeValidator(Validators.ThresholdDetector(), Validators.ZeroSpikeDetector())], 
         [0, 0, 1, 2, 2]),
        ([Validators.OutlierDetector()], 
         [2, 2, 3, 1, 2]),
        ([Validators.CompositeValidator(Validators.CompositeValidator(Validators.ThresholdDetector(), Validators.OutlierDetector()), Validators.CompositeValidator(Validators.ZeroSpikeDetector(), SimpleReporter.SimpleReporter()))], 
         [3, 3, 5, 4, 5]),
        ([], 
         [0, 0, 0, 0, 0]),
    ])
    def test_preload(self, validators, shape):
        measurements = Measurements(Path('../measurements/validTests'))
        result = measurements.detect_all_anomalies(validators, True)
        for res, length in zip(result.values(), shape):
            assert len(res) == length

    @pytest.mark.parametrize('validators, shape, nRows', [
        ([SimpleReporter.SimpleReporter()], 
         [1, 1, 1, 1, 1], 0),
        ([SimpleReporter.SimpleReporter(), Validators.ZeroSpikeDetector()], 
         [1, 1, 1, 1, 1], 0),
        ([Validators.CompositeValidator(SimpleReporter.SimpleReporter(), Validators.ZeroSpikeDetector())], 
         [1, 1, 1, 1, 1], 0),
        ([Validators.ThresholdDetector(), Validators.ZeroSpikeDetector()], 
         [0, 0, 0, 0, 0], 0),
        ([Validators.CompositeValidator(Validators.ThresholdDetector(), Validators.ZeroSpikeDetector())], 
         [0, 0, 0, 0, 0], 0),
        ([Validators.OutlierDetector()], 
         [0, 0, 0, 0, 0], 0),
        ([Validators.CompositeValidator(Validators.CompositeValidator(Validators.ThresholdDetector(), Validators.OutlierDetector()), Validators.CompositeValidator(Validators.ZeroSpikeDetector(), SimpleReporter.SimpleReporter()))], 
         [1, 1, 1, 1, 1], 0),
        ([], 
         [0, 0, 0, 0, 0], 0),

        ([SimpleReporter.SimpleReporter()], 
         [1, 1, 1, 1, 1], 1),
        ([SimpleReporter.SimpleReporter(), Validators.ZeroSpikeDetector()], 
         [1, 1, 1, 1, 1], 1),
        ([Validators.CompositeValidator(SimpleReporter.SimpleReporter(), Validators.ZeroSpikeDetector())], 
         [1, 1, 1, 1, 1], 1),
        ([Validators.ThresholdDetector(), Validators.ZeroSpikeDetector()], 
         [0, 0, 0, 0, 1], 1),
        ([Validators.CompositeValidator(Validators.ThresholdDetector(), Validators.ZeroSpikeDetector())], 
         [0, 0, 0, 0, 1], 1),
        ([Validators.OutlierDetector()], 
         [0, 0, 0, 0, 0], 1),
        ([Validators.CompositeValidator(Validators.CompositeValidator(Validators.ThresholdDetector(), Validators.OutlierDetector()), Validators.CompositeValidator(Validators.ZeroSpikeDetector(), SimpleReporter.SimpleReporter()))], 
         [1, 1, 1, 1, 2], 1),
        ([], 
         [0, 0, 0, 0, 0], 1),

        ([SimpleReporter.SimpleReporter()], 
         [1, 1, 1, 1, 1], 5),
        ([SimpleReporter.SimpleReporter(), Validators.ZeroSpikeDetector()], 
         [1, 1, 2, 1, 1], 5),
        ([Validators.CompositeValidator(SimpleReporter.SimpleReporter(), Validators.ZeroSpikeDetector())], 
         [1, 1, 2, 1, 1], 5),
        ([Validators.ThresholdDetector(), Validators.ZeroSpikeDetector()], 
         [0, 0, 1, 0, 1], 5),
        ([Validators.CompositeValidator(Validators.ThresholdDetector(), Validators.ZeroSpikeDetector())], 
         [0, 0, 1, 0, 1], 5),
        ([Validators.OutlierDetector()], 
         [0, 2, 2, 1, 1], 5),
        ([Validators.CompositeValidator(Validators.CompositeValidator(Validators.ThresholdDetector(), Validators.OutlierDetector()), Validators.CompositeValidator(Validators.ZeroSpikeDetector(), SimpleReporter.SimpleReporter()))], 
         [1, 3, 4, 2, 3], 5),
        ([], 
         [0, 0, 0, 0, 0], 5),

        ([SimpleReporter.SimpleReporter()], 
         [1, 1, 1, 1, 1], 8),
        ([SimpleReporter.SimpleReporter(), Validators.ZeroSpikeDetector()], 
         [1, 1, 2, 2, 1], 8),
        ([Validators.CompositeValidator(SimpleReporter.SimpleReporter(), Validators.ZeroSpikeDetector())], 
         [1, 1, 2, 2, 1], 8),
        ([Validators.ThresholdDetector(), Validators.ZeroSpikeDetector()], 
         [0, 0, 1, 2, 2], 8),
        ([Validators.CompositeValidator(Validators.ThresholdDetector(), Validators.ZeroSpikeDetector())], 
         [0, 0, 1, 2, 2], 8),
        ([Validators.OutlierDetector()], 
         [2, 2, 3, 1, 2], 8),
        ([Validators.CompositeValidator(Validators.CompositeValidator(Validators.ThresholdDetector(), Validators.OutlierDetector()), Validators.CompositeValidator(Validators.ZeroSpikeDetector(), SimpleReporter.SimpleReporter()))], 
         [3, 3, 5, 4, 5], 8),
        ([], 
         [0, 0, 0, 0, 0], 8),

        ([SimpleReporter.SimpleReporter()], 
         [1, 1, 1, 1, 1], 10),
        ([SimpleReporter.SimpleReporter(), Validators.ZeroSpikeDetector()], 
         [1, 1, 2, 2, 1], 10),
        ([Validators.CompositeValidator(SimpleReporter.SimpleReporter(), Validators.ZeroSpikeDetector())], 
         [1, 1, 2, 2, 1], 10),
        ([Validators.ThresholdDetector(), Validators.ZeroSpikeDetector()], 
         [0, 0, 1, 2, 2], 10),
        ([Validators.CompositeValidator(Validators.ThresholdDetector(), Validators.ZeroSpikeDetector())], 
         [0, 0, 1, 2, 2], 10),
        ([Validators.OutlierDetector()], 
         [2, 2, 3, 1, 2], 10),
        ([Validators.CompositeValidator(Validators.CompositeValidator(Validators.ThresholdDetector(), Validators.OutlierDetector()), Validators.CompositeValidator(Validators.ZeroSpikeDetector(), SimpleReporter.SimpleReporter()))], 
         [3, 3, 5, 4, 5], 10),
        ([], 
         [0, 0, 0, 0, 0], 10),
    ])
    def test_lazy(self, validators, shape, nRows):
        measurements = Measurements(Path('../measurements/validTests'))
        for _, _ in zip(range(nRows), measurements.merger):
            pass
        result = measurements.detect_all_anomalies(validators, False)
        for res, length in zip(result.values(), shape):
            assert len(res) == length
