from z6 import log
import logging

def configureLogging(logger):
    import sys

    logging.basicConfig(filename='/dev/null', level=logging.INFO)
    formatter = logging.Formatter('%(levelname)s\t- %(message)s')

    logFile = open('python.log', mode='w')
    handler = logging.StreamHandler(logFile)
    handler.setLevel(logging.INFO)
    handler.setFormatter(formatter)

    logger.addHandler(handler)

def get_default_logger(name: str = __name__):
    return logging.getLogger(name)

@log(logging.INFO, get_default_logger())
def test():
    for i in range(100000):
        pass
    print('Hello, world!')

@log(logging.INFO, get_default_logger())
def testAdd(a, b, c = 0):
    return a + b + c

@log(logging.INFO, get_default_logger())
class testCls:
    def __init__(self):
        pass

    def testMethod(self, arg):
        return None

    def __str__(self):
        return 'Obiekt klasy testowej'

@log(logging.INFO, get_default_logger())
class testCls2:
    def __new__(cls, arg1):
        cls.arg1 = arg1
        return super().__new__(cls)

    def __str__(self):
        return str(self.arg1)

if __name__ == '__main__':
    configureLogging(get_default_logger())
    test()
    print(testAdd(2, 3, c=4) + 5)
    print(test.__name__)
    print(testCls())
    obj = testCls()
    print(obj.testMethod(1))
    obj = testCls2('a')
    print(obj)
    print(log(logging.INFO, get_default_logger())(lambda x: x + 2)(2))
