import sys
import window
from PySide6.QtWidgets import QApplication, QMainWindow

from ReadManager import ReadManager
from DetailManager import DetailManager
from FilterManager import FilterManager
from PositionManager import PositionManager


class MainApp:

    def __init__(self):
        self.createApp()

    def createApp(self):
        self.app = QApplication(sys.argv)
        self.mainWindow = QMainWindow()
        self.contents = window.Ui_MainWindow()
        self.contents.setupUi(self.mainWindow)
        self.createManagers()
        self.attachListeners()
        self.mainWindow.show()
        sys.exit(self.app.exec())

    def createManagers(self):
        self.readMan = ReadManager(self)
        self.detailMan = DetailManager(self, self.readMan)
        self.filterMan = FilterManager(self)
        self.positionMan = PositionManager(self)


    def attachListeners(self):
        self.contents.filenameButton.clicked.connect(self.filterMan.reset)
        self.contents.filenameButton.clicked.connect(self.readMan.__call__)
        self.contents.masterList.currentRowChanged.connect(self.detailMan.__call__)
        self.contents.applyDateFilter.clicked.connect(self.filterMan.refresh)
        self.contents.applyDateFilter.clicked.connect(self.readMan.__call__)
        self.contents.nextButton.clicked.connect(self.positionMan.on_next)
        self.contents.prevButton.clicked.connect(self.positionMan.on_previous)

if __name__ == '__main__':
    app = MainApp()
