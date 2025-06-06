# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QGridLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 781, 551))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)

        self.databaseSelector = QLineEdit(self.layoutWidget)
        self.databaseSelector.setObjectName(u"databaseSelector")

        self.gridLayout.addWidget(self.databaseSelector, 1, 0, 1, 2)

        self.dialectSelector = QComboBox(self.layoutWidget)
        self.dialectSelector.addItem("")
        self.dialectSelector.addItem("")
        self.dialectSelector.setObjectName(u"dialectSelector")

        self.gridLayout.addWidget(self.dialectSelector, 1, 2, 1, 1)

        self.loadButton = QPushButton(self.layoutWidget)
        self.loadButton.setObjectName(u"loadButton")

        self.gridLayout.addWidget(self.loadButton, 1, 3, 1, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 1, 1, 1)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 3, 1, 1, 1)

        self.avgTimeStart = QLineEdit(self.layoutWidget)
        self.avgTimeStart.setObjectName(u"avgTimeStart")
        self.avgTimeStart.setReadOnly(True)

        self.gridLayout.addWidget(self.avgTimeStart, 4, 1, 1, 1)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 5, 1, 1, 1)

        self.avgEndTime = QLineEdit(self.layoutWidget)
        self.avgEndTime.setObjectName(u"avgEndTime")
        self.avgEndTime.setReadOnly(True)

        self.gridLayout.addWidget(self.avgEndTime, 6, 1, 1, 1)

        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 7, 1, 1, 1)

        self.differentBikes = QLineEdit(self.layoutWidget)
        self.differentBikes.setObjectName(u"differentBikes")
        self.differentBikes.setReadOnly(True)

        self.gridLayout.addWidget(self.differentBikes, 8, 1, 1, 1)

        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 9, 1, 1, 1)

        self.stationList = QListWidget(self.layoutWidget)
        self.stationList.setObjectName(u"stationList")
        self.stationList.setProperty(u"isWrapping", True)

        self.gridLayout.addWidget(self.stationList, 3, 0, 8, 1)

        self.exampleRentals = QListWidget(self.layoutWidget)
        self.exampleRentals.setObjectName(u"exampleRentals")
        self.exampleRentals.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.exampleRentals.setProperty(u"isWrapping", True)
        self.exampleRentals.setUniformItemSizes(False)
        self.exampleRentals.setItemAlignment(Qt.AlignmentFlag.AlignLeading)

        self.gridLayout.addWidget(self.exampleRentals, 10, 1, 1, 3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Database path", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Dialect", None))
        self.dialectSelector.setItemText(0, QCoreApplication.translate("MainWindow", u"Sqlite", None))
        self.dialectSelector.setItemText(1, QCoreApplication.translate("MainWindow", u"Peewee", None))

        self.loadButton.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Stations", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Overview", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Average time as start", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Average time at end", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Diffrent bikes", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Example rentals", None))
    # retranslateUi

