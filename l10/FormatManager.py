from DataLoaders import SQLiteLoader


class FormatManager:
    def __init__(self, ctx):
        self.ctx = ctx
        self.current_format = 'Sqlite'
        self.loader = SQLiteLoader(self.ctx)

    def update_format(self):
        self.ctx.ui.stationList.clear()
        self.current_format = self.ctx.ui.dialectBox.currentText()
        # tutaj nadpisz
        print(self.current_format)
        self.loader = SQLiteLoader(self.ctx) if self.current_format == 'Sqlite' else None

    def load_data(self):
        self.loader.load_data()