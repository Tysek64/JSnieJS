from PySide6.QtWidgets import QMessageBox

from DataLoader import DataLoader
import LogReader


class ReadManager:
    def __init__(self, ctx):
        self.ctx = ctx

    def __call__(self):
        def updateMaster(data):
            self.ctx.contents.masterList.addItems(data)

        def updateStatusBar(data):
            self.ctx.contents.statusBar.showMessage(str(data) + '/' + totalLines)

        try:
            self.reader = LogReader.LogReader(self.ctx.contents.filenameInput.text(), self.ctx.filterMan.filters)
            totalLines = str(self.reader.getTotalRecords())
            self.ctx.contents.masterList.clear()
            self.loaderThread = DataLoader(self, self.ctx.filterMan)
            self.loaderThread.statusSignal.connect(updateStatusBar)
            self.loaderThread.resultSignal.connect(updateMaster)
            self.loaderThread.start()
        except FileNotFoundError as e:
            messageBox = QMessageBox.critical(None, 'Error!', f'File named \'{self.ctx.contents.filenameInput.text()}\' does not exist or could not be read!')