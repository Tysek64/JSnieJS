from PySide6.QtCore import QThread, Signal, Qt
from PySide6.QtWidgets import QMessageBox


class DataLoader(QThread):
    resultSignal = Signal(list)
    statusSignal = Signal(int)

    def __init__(self, readManager, filterManager):
        QThread.__init__(self, None)  # ?
        self.readManager = readManager
        self.filterManager = filterManager

    def run(self):
        result = []
        for i, line in enumerate(self.readManager.reader.readMasterRecord(), start=1):
            result.append(line)
            self.statusSignal.emit(i)
        self.resultSignal.emit(result)