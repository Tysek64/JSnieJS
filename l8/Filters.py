from PySide6.QtCore import QDate

from LogReader import LogReader


class BaseFilter:
    def __call__(self, line):
        return True

class DateFilter(BaseFilter):
    def __init__(self, begin_date, end_date):
        self.begin_date = begin_date
        self.end_date = end_date

    def __call__(self, line):
        record = LogReader.getDetail(line)
        if self.begin_date <= QDate(record['timestamp']) <= self.end_date:
            return True
        return False