import logging

def log(level, logger):
    def wrapper1(func):
        def wrapper2(*args, **kwargs):
            import time
            import datetime

            startTime = time.perf_counter()
            logger.log(level, ('Utworzono instancje klasy ' if isinstance(func, type) else 'Uruchomiono ') + f'\'{func.__name__}\' o czasie {datetime.datetime.now()} ' + ('bez argumentow' if len(args) + len(kwargs) == 0 else 'z argumentami:'))

            for arg in args:
                logger.log(level, f'  {arg}')
            for k, v in kwargs.items():
                logger.log(level, f'  {k}: {v}')

            retVal = func(*args, **kwargs)
            if not isinstance(func, type):
                logger.log(level, f'Zakonczono \'{func.__name__}\' po {(1000 * (time.perf_counter() - startTime)):.3f}ms i otrzymano wartosc: {retVal}')

            return retVal
        wrapper2.__name__ = func.__name__
        wrapper2.__doc__ = func.__doc__
        return wrapper2
    return wrapper1
