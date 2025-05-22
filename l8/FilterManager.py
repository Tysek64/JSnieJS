from PySide6.QtWidgets import QMessageBox

import Filters


class FilterManager:
    def __init__(self, ctx):
        self.ctx = ctx
        self.filters = []

    def reset(self):
        self.filters = []

    def refresh(self):
        self.filters = []

        # Date filtering
        b_date, e_date = self.ctx.contents.dateFrom.date(), self.ctx.contents.dateTo.date()
        if b_date <= e_date:
            self.filters.append(Filters.DateFilter(b_date, e_date))
        else:
            QMessageBox.critical(None, 'Warning', f'Begin date is later than end date, date filter not applied')

    def __call__(self, line):
        for f in self.filters:
            if not f(line):
                return False
        return True


