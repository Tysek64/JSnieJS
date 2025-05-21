import sys
import LogReader
import window
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import QThread, Signal, Qt
import time

class MainApp:
    reader = LogReader.LogReader('smalllog')

    class DataLoader(QThread):
        resultSignal = Signal(list)
        statusSignal = Signal(int)

        def __init__(self, parent=None):
            QThread.__init__(self, None)
            self.parent = parent

        def run(self):
            result = []
            for i, line in enumerate(self.parent.reader.readMasterRecord(), start=1):
                result.append(line)
                self.statusSignal.emit(i)
            self.resultSignal.emit(result)

    def openFile(self):
        def updateMaster(data):
            self.contents.masterList.addItems(data)

        def updateStatusBar(data):
            self.contents.statusBar.showMessage(str(data) + '/' + totalLines)

        try:
            self.reader = LogReader.LogReader(self.contents.filenameInput.text())
            totalLines = str(self.reader.getTotalRecords())
            self.contents.masterList.clear()
            self.loaderThread = self.DataLoader(self)
            self.loaderThread.statusSignal.connect(updateStatusBar)
            self.loaderThread.resultSignal.connect(updateMaster)
            self.loaderThread.start()
        except FileNotFoundError as e:
            messageBox = QMessageBox.critical(None, 'Error!', f'File named \'{self.contents.filenameInput.text()}\' does not exist or could not be read!')

    def showDetails(self):
        details = self.reader.getDetails(self.contents.masterList.currentRow())
        self.contents.remoteHostDisplay.setText(str(details['remote IP']))
        self.contents.methodDisplay.setText(details['method'])
        palette = self.contents.statusCodeDisplay.palette()
        if details['code'] in range(200, 299):
            palette.setColor(self.contents.statusCodeDisplay.backgroundRole(), '#00FF00')
        elif details['code'] in range(400, 599):
            palette.setColor(self.contents.statusCodeDisplay.backgroundRole(), '#FF0000')
        self.contents.statusCodeDisplay.setAutoFillBackground(True)
        self.contents.statusCodeDisplay.setPalette(palette)
        self.contents.statusCodeDisplay.display(details['code'])
        self.contents.sizeDisplay.display(details['size'])
        self.contents.resourceDisplay.setText(details['URI'])
        self.contents.dateDisplay.setDate(details['timestamp'].date())
        self.contents.timeDisplay.setTime(details['timestamp'].time())
        self.contents.localHostDisplay.setText(str(details['local IP']))
        self.contents.hostnameDisplay.setText(details['hostname'])

    def __init__(self):
        self.app = QApplication(sys.argv)
        self.mainWindow = QMainWindow()
        self.contents = window.Ui_MainWindow()
        self.contents.setupUi(self.mainWindow)
        self.contents.filenameButton.clicked.connect(self.openFile)
        self.contents.masterList.currentRowChanged.connect(self.showDetails)
        self.mainWindow.show()

        sys.exit(self.app.exec())

if __name__ == '__main__':
    app = MainApp()
