import logging
import sys

class LevelFilter (logging.Filter):
    def __init__ (self, low, high):
        self._low = low
        self._high = high
        logging.Filter.__init__(self)
    def filter (self, record):
        return self._low <= record.levelno <= self._high

def configureLogging(logger):
    logging.basicConfig(filename='/dev/null', level=logging.DEBUG)
    formatter = logging.Formatter('%(levelname)s\t- %(message)s')

    stderrHandler = logging.StreamHandler(sys.stderr)
    stderrHandler.setLevel(logging.ERROR)
    stderrHandler.setFormatter(formatter)

    stdoutHandler = logging.StreamHandler(sys.stdout)
    stdoutHandler.setLevel(logging.DEBUG)
    stdoutHandler.addFilter(LevelFilter(logging.DEBUG, logging.WARNING))
    stdoutHandler.setFormatter(formatter)

    logger.addHandler(stdoutHandler)
    logger.addHandler(stderrHandler)

def get_default_logger(name: str = __name__):
    return logging.getLogger(name)