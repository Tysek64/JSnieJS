class PositionManager:
    def __init__(self, ctx):
        self.ctx = ctx
        self.row = 0

    def on_previous(self):
        current_row = self.ctx.contents.masterList.currentRow()
        if current_row > 0:
            self.ctx.contents.masterList.setCurrentRow(current_row - 1)

    def on_next(self):
        current_row = self.ctx.contents.masterList.currentRow()
        if current_row < self.ctx.contents.masterList.count() - 1:
            self.ctx.contents.masterList.setCurrentRow(current_row + 1)
