# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
    QLineEdit, QListView, QListWidget, QListWidgetItem,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSplitter, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.splitter_2 = QSplitter(self.centralwidget)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Orientation.Vertical)
        self.layoutWidget = QWidget(self.splitter_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)

        self.databasePath = QLineEdit(self.layoutWidget)
        self.databasePath.setObjectName(u"databasePath")

        self.gridLayout.addWidget(self.databasePath, 1, 0, 1, 1)

        self.dialectBox = QComboBox(self.layoutWidget)
        self.dialectBox.addItem("")
        self.dialectBox.addItem("")
        self.dialectBox.setObjectName(u"dialectBox")

        self.gridLayout.addWidget(self.dialectBox, 1, 1, 1, 1)

        self.loadButton = QPushButton(self.layoutWidget)
        self.loadButton.setObjectName(u"loadButton")

        self.gridLayout.addWidget(self.loadButton, 1, 2, 1, 1)

        self.splitter_2.addWidget(self.layoutWidget)
        self.splitter = QSplitter(self.splitter_2)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.layoutWidget1 = QWidget(self.splitter)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget1)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.stationList = QListWidget(self.layoutWidget1)
        self.stationList.setObjectName(u"stationList")
        self.stationList.setProperty(u"isWrapping", True)

        self.verticalLayout_2.addWidget(self.stationList)

        self.splitter.addWidget(self.layoutWidget1)
        self.layoutWidget2 = QWidget(self.splitter)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.verticalLayout = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.layoutWidget2)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.label_5 = QLabel(self.layoutWidget2)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.avgTimeStart = QLineEdit(self.layoutWidget2)
        self.avgTimeStart.setObjectName(u"avgTimeStart")
        self.avgTimeStart.setReadOnly(True)

        self.verticalLayout.addWidget(self.avgTimeStart)

        self.label_6 = QLabel(self.layoutWidget2)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.avgTimeEnd = QLineEdit(self.layoutWidget2)
        self.avgTimeEnd.setObjectName(u"avgTimeEnd")
        self.avgTimeEnd.setReadOnly(True)

        self.verticalLayout.addWidget(self.avgTimeEnd)

        self.label_7 = QLabel(self.layoutWidget2)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout.addWidget(self.label_7)

        self.diffBikes = QLineEdit(self.layoutWidget2)
        self.diffBikes.setObjectName(u"diffBikes")
        self.diffBikes.setReadOnly(True)

        self.verticalLayout.addWidget(self.diffBikes)

        self.label_9 = QLabel(self.layoutWidget2)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout.addWidget(self.label_9)

        self.popDest = QLineEdit(self.layoutWidget2)
        self.popDest.setObjectName(u"popDest")
        self.popDest.setReadOnly(True)

        self.verticalLayout.addWidget(self.popDest)

        self.label_8 = QLabel(self.layoutWidget2)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout.addWidget(self.label_8)

        self.rentalsList = QListWidget(self.layoutWidget2)
        self.rentalsList.setObjectName(u"rentalsList")
        self.rentalsList.setProperty(u"isWrapping", False)
        self.rentalsList.setLayoutMode(QListView.LayoutMode.Batched)

        self.verticalLayout.addWidget(self.rentalsList)

        self.splitter.addWidget(self.layoutWidget2)
        self.splitter_2.addWidget(self.splitter)

        self.gridLayout_2.addWidget(self.splitter_2, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 27))
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
        self.dialectBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Sqlite", None))
        self.dialectBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Peewee", None))

        self.loadButton.setText(QCoreApplication.translate("MainWindow", u"Load", None))
#if QT_CONFIG(shortcut)
        self.loadButton.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Stations", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Overview", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Average time as start", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Average time at end", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Diffrent bikes", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Most popular destination", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Example rentals", None))
    # retranslateUi

