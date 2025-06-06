from PySide6.QtWidgets import QMainWindow, QApplication
import sys
from MainWindow import Ui_MainWindow
from DataLoaders import SQLiteLoader
from FormatManager import FormatManager
from PositionManager import PositionManager


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_listeners()

    def setup_listeners(self):
        self.formatManager = FormatManager(self)
        self.positionManager = PositionManager(self)
        self.ui.stationList.currentRowChanged.connect(self.positionManager.update_stats)
        self.ui.dialectSelector.currentTextChanged.connect(self.formatManager.update_format)
        self.ui.loadButton.clicked.connect(self.formatManager.load_data)



if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())