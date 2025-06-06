class PositionManager:
    def __init__(self, ctx):
        self.ctx = ctx
        self.row = 0

    def on_previous(self):
        current_row = self.ctx.ui.stationList.currentRow()
        if current_row > 0:
            self.ctx.ui.stationList.setCurrentRow(current_row - 1)
        self.update_stats()

    def on_next(self):
        current_row = self.ctx.ui.stationList.currentRow()
        if current_row < self.ctx.ui.stationList.count() - 1:
            self.ctx.ui.stationList.setCurrentRow(current_row + 1)
        self.update_stats()

    def update_stats(self):
        if self.ctx.ui.stationList.currentItem() is not None:
            current_station = self.ctx.ui.stationList.currentItem().text()
            self.ctx.formatManager.loader.update_stats(current_station)

