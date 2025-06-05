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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

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
        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 7, 1, 1, 1)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 1, 1, 1)

        self.avgTimeStart = QLineEdit(self.layoutWidget)
        self.avgTimeStart.setObjectName(u"avgTimeStart")
        self.avgTimeStart.setReadOnly(True)

        self.gridLayout.addWidget(self.avgTimeStart, 4, 1, 1, 1)

        self.avgTimeEnd = QLineEdit(self.layoutWidget)
        self.avgTimeEnd.setObjectName(u"avgTimeEnd")
        self.avgTimeEnd.setReadOnly(True)

        self.gridLayout.addWidget(self.avgTimeEnd, 6, 1, 1, 1)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 3, 1, 1, 1)

        self.loadButton = QPushButton(self.layoutWidget)
        self.loadButton.setObjectName(u"loadButton")

        self.gridLayout.addWidget(self.loadButton, 1, 3, 1, 1)

        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 9, 1, 1, 1)

        self.databasePath = QLineEdit(self.layoutWidget)
        self.databasePath.setObjectName(u"databasePath")

        self.gridLayout.addWidget(self.databasePath, 1, 0, 1, 2)

        self.diffBikes = QLineEdit(self.layoutWidget)
        self.diffBikes.setObjectName(u"diffBikes")
        self.diffBikes.setReadOnly(True)

        self.gridLayout.addWidget(self.diffBikes, 8, 1, 1, 1)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 5, 1, 1, 1)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.dialectBox = QComboBox(self.layoutWidget)
        self.dialectBox.addItem("")
        self.dialectBox.addItem("")
        self.dialectBox.setObjectName(u"dialectBox")

        self.gridLayout.addWidget(self.dialectBox, 1, 2, 1, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.stationList = QListWidget(self.layoutWidget)
        self.stationList.setObjectName(u"stationList")
        self.stationList.setProperty(u"isWrapping", True)

        self.gridLayout.addWidget(self.stationList, 3, 0, 8, 1)

        self.rentalsList = QListWidget(self.layoutWidget)
        self.rentalsList.setObjectName(u"rentalsList")
        self.rentalsList.setProperty(u"isWrapping", True)

        self.gridLayout.addWidget(self.rentalsList, 10, 1, 1, 3)

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
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Diffrent bikes", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Overview", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Dialect", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Average time as start", None))
        self.loadButton.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Example rentals", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Average time at end", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Database path", None))
        self.dialectBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Sqlite", None))
        self.dialectBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Peewee", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Stations", None))
    # retranslateUi

