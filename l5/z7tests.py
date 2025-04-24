

'''
DATA FOR TESTS MUST BE IN FORMAT
{
    'date1': measurement11, measurement12, measurement13, ...
    'date2': measurement21, measurement22, measurement23, ...
    ...
}
'''

def test_for_condition(data_: dict, dict_: dict, condition_: callable,
                       hook: callable = lambda k, v: None):
    for k, v in data_.items():
        for index, measurement in enumerate(v):
                res_ = 1 if condition_(index, measurement) else 0
                try:
                    dict_[index] += res_
                except KeyError:
                    dict_[index] = res_
        hook(k, v)

# Panie, a jakie ladne domkniecia i referencje!
def null_test(data: dict, *args) -> dict:
    import collections
    nulls = collections.OrderedDict()

    rows = 1
    def increment_rows(*args):
        nonlocal rows
        rows += 1

    test_for_condition(data, nulls, (lambda _, m: m is None), increment_rows)

    return {k: round(v/rows, 2) for k,v in nulls.items()}

def delta_test(delta: float) -> callable:
    def test_(data: dict, *args) -> dict:
        import collections
        results = collections.OrderedDict()

        prev_measurements = None
        def modify_measurements(k, v):
            nonlocal prev_measurements
            prev_measurements = v

        def condition(i, m):
            nonlocal prev_measurements
            return 0 if (prev_measurements is None or
                         prev_measurements[i] is None or
                         m is None or
                         abs(prev_measurements[i] - m) < delta) else 1

        test_for_condition(data, results, condition, modify_measurements)
        return dict(results)

    test_.__name__ = f'delta_test__delta={delta}'
    return test_

def threshold_test(chemical: str, threshold: float) -> callable:
    def test_(data: dict, meta_data, *args) -> dict:
        from z1 import select_from
        data, cols = select_from((data, meta_data), 'Chemical', (lambda chemical: chemical == 'acetylen'))
        import collections
        results = collections.OrderedDict()

        test_for_condition(data, results, (lambda _, m: m is not None and m > threshold))
        return {col: v for col, (k, v) in zip(cols, results.items())}

    test_.__name__ = f'delta_test__chemical={chemical}_threshold={threshold}'
    return test_