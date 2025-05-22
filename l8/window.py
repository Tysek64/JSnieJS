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
from PySide6.QtWidgets import (QApplication, QDateEdit, QGridLayout, QHBoxLayout,
    QLCDNumber, QLabel, QLayout, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QSplitter, QStatusBar,
    QTimeEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.fileSelectLayout = QHBoxLayout()
        self.fileSelectLayout.setObjectName(u"fileSelectLayout")
        self.fileSelectLayout.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.filenameInput = QLineEdit(self.centralwidget)
        self.filenameInput.setObjectName(u"filenameInput")

        self.fileSelectLayout.addWidget(self.filenameInput)

        self.filenameButton = QPushButton(self.centralwidget)
        self.filenameButton.setObjectName(u"filenameButton")

        self.fileSelectLayout.addWidget(self.filenameButton)


        self.verticalLayout.addLayout(self.fileSelectLayout)

        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.masterList = QListWidget(self.splitter)
        self.masterList.setObjectName(u"masterList")
        font = QFont()
        font.setFamilies([u"Cascadia Mono"])
        self.masterList.setFont(font)
        self.splitter.addWidget(self.masterList)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.detailsLayout = QGridLayout(self.layoutWidget)
        self.detailsLayout.setSpacing(6)
        self.detailsLayout.setObjectName(u"detailsLayout")
        self.detailsLayout.setContentsMargins(0, 0, 0, 0)
        self.resourceDisplay = QLineEdit(self.layoutWidget)
        self.resourceDisplay.setObjectName(u"resourceDisplay")
        self.resourceDisplay.setFont(font)
        self.resourceDisplay.setFrame(False)
        self.resourceDisplay.setReadOnly(True)

        self.detailsLayout.addWidget(self.resourceDisplay, 4, 1, 1, 3)

        self.timeDisplay = QTimeEdit(self.layoutWidget)
        self.timeDisplay.setObjectName(u"timeDisplay")
        self.timeDisplay.setFont(font)
        self.timeDisplay.setReadOnly(True)
        self.timeDisplay.setAccelerated(True)

        self.detailsLayout.addWidget(self.timeDisplay, 2, 1, 1, 1)

        self.resourceLabel = QLabel(self.layoutWidget)
        self.resourceLabel.setObjectName(u"resourceLabel")
        self.resourceLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.detailsLayout.addWidget(self.resourceLabel, 4, 0, 1, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.detailsLayout.addWidget(self.label_2, 6, 2, 1, 1)

        self.dateFrom = QDateEdit(self.layoutWidget)
        self.dateFrom.setObjectName(u"dateFrom")

        self.detailsLayout.addWidget(self.dateFrom, 7, 1, 1, 1)

        self.remoteHostDisplay = QLineEdit(self.layoutWidget)
        self.remoteHostDisplay.setObjectName(u"remoteHostDisplay")
        self.remoteHostDisplay.setFont(font)
        self.remoteHostDisplay.setFrame(False)
        self.remoteHostDisplay.setReadOnly(True)

        self.detailsLayout.addWidget(self.remoteHostDisplay, 0, 3, 1, 1)

        self.timeLabel = QLabel(self.layoutWidget)
        self.timeLabel.setObjectName(u"timeLabel")
        self.timeLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.detailsLayout.addWidget(self.timeLabel, 2, 0, 1, 1)

        self.applyDateFilter = QPushButton(self.layoutWidget)
        self.applyDateFilter.setObjectName(u"applyDateFilter")

        self.detailsLayout.addWidget(self.applyDateFilter, 7, 3, 1, 1)

        self.localHostDisplay = QLineEdit(self.layoutWidget)
        self.localHostDisplay.setObjectName(u"localHostDisplay")
        self.localHostDisplay.setFont(font)
        self.localHostDisplay.setFrame(False)
        self.localHostDisplay.setReadOnly(True)

        self.detailsLayout.addWidget(self.localHostDisplay, 0, 1, 1, 1)

        self.statusCodeLabel = QLabel(self.layoutWidget)
        self.statusCodeLabel.setObjectName(u"statusCodeLabel")
        self.statusCodeLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.detailsLayout.addWidget(self.statusCodeLabel, 3, 0, 1, 1)

        self.statusCodeDisplay = QLCDNumber(self.layoutWidget)
        self.statusCodeDisplay.setObjectName(u"statusCodeDisplay")
        self.statusCodeDisplay.setLineWidth(0)
        self.statusCodeDisplay.setDigitCount(3)
        self.statusCodeDisplay.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.detailsLayout.addWidget(self.statusCodeDisplay, 3, 1, 1, 1)

        self.localHostLabel = QLabel(self.layoutWidget)
        self.localHostLabel.setObjectName(u"localHostLabel")
        self.localHostLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.detailsLayout.addWidget(self.localHostLabel, 0, 0, 1, 1)

        self.dateLabel = QLabel(self.layoutWidget)
        self.dateLabel.setObjectName(u"dateLabel")
        self.dateLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.detailsLayout.addWidget(self.dateLabel, 1, 0, 1, 1)

        self.methodLabel = QLabel(self.layoutWidget)
        self.methodLabel.setObjectName(u"methodLabel")
        self.methodLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.detailsLayout.addWidget(self.methodLabel, 3, 2, 1, 1)

        self.hostnameDisplay = QLineEdit(self.layoutWidget)
        self.hostnameDisplay.setObjectName(u"hostnameDisplay")
        self.hostnameDisplay.setFont(font)
        self.hostnameDisplay.setFrame(False)
        self.hostnameDisplay.setReadOnly(True)

        self.detailsLayout.addWidget(self.hostnameDisplay, 5, 3, 1, 1)

        self.hostnameLabel = QLabel(self.layoutWidget)
        self.hostnameLabel.setObjectName(u"hostnameLabel")
        self.hostnameLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.detailsLayout.addWidget(self.hostnameLabel, 5, 2, 1, 1)

        self.remoteHostLabel = QLabel(self.layoutWidget)
        self.remoteHostLabel.setObjectName(u"remoteHostLabel")
        self.remoteHostLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.detailsLayout.addWidget(self.remoteHostLabel, 0, 2, 1, 1)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.detailsLayout.addWidget(self.label, 6, 1, 1, 1)

        self.sizeLabel = QLabel(self.layoutWidget)
        self.sizeLabel.setObjectName(u"sizeLabel")
        self.sizeLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.detailsLayout.addWidget(self.sizeLabel, 5, 0, 1, 1)

        self.dateDisplay = QDateEdit(self.layoutWidget)
        self.dateDisplay.setObjectName(u"dateDisplay")
        self.dateDisplay.setEnabled(True)
        self.dateDisplay.setFont(font)
        self.dateDisplay.setReadOnly(True)
        self.dateDisplay.setAccelerated(True)

        self.detailsLayout.addWidget(self.dateDisplay, 1, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.detailsLayout.addItem(self.verticalSpacer, 9, 0, 1, 1)

        self.dateTo = QDateEdit(self.layoutWidget)
        self.dateTo.setObjectName(u"dateTo")
        self.dateTo.setDateTime(QDateTime(QDate(2000, 12, 31), QTime(22, 0, 0)))

        self.detailsLayout.addWidget(self.dateTo, 7, 2, 1, 1)

        self.methodDisplay = QLineEdit(self.layoutWidget)
        self.methodDisplay.setObjectName(u"methodDisplay")
        self.methodDisplay.setFont(font)
        self.methodDisplay.setFrame(False)
        self.methodDisplay.setReadOnly(True)

        self.detailsLayout.addWidget(self.methodDisplay, 3, 3, 1, 1)

        self.sizeDisplay = QLCDNumber(self.layoutWidget)
        self.sizeDisplay.setObjectName(u"sizeDisplay")
        self.sizeDisplay.setLineWidth(0)
        self.sizeDisplay.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.detailsLayout.addWidget(self.sizeDisplay, 5, 1, 1, 1)

        self.nextButton = QPushButton(self.layoutWidget)
        self.nextButton.setObjectName(u"nextButton")

        self.detailsLayout.addWidget(self.nextButton, 10, 3, 1, 1)

        self.prevButton = QPushButton(self.layoutWidget)
        self.prevButton.setObjectName(u"prevButton")

        self.detailsLayout.addWidget(self.prevButton, 10, 0, 1, 1)

        self.splitter.addWidget(self.layoutWidget)

        self.verticalLayout.addWidget(self.splitter)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.filenameButton.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.timeDisplay.setDisplayFormat(QCoreApplication.translate("MainWindow", u"hh:mm:ss.zzz", None))
        self.resourceLabel.setText(QCoreApplication.translate("MainWindow", u"Resource", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"To", None))
        self.timeLabel.setText(QCoreApplication.translate("MainWindow", u"Time", None))
        self.applyDateFilter.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.statusCodeLabel.setText(QCoreApplication.translate("MainWindow", u"Status code", None))
        self.localHostLabel.setText(QCoreApplication.translate("MainWindow", u"Local IP address", None))
        self.dateLabel.setText(QCoreApplication.translate("MainWindow", u"Date", None))
        self.methodLabel.setText(QCoreApplication.translate("MainWindow", u"Method", None))
        self.hostnameLabel.setText(QCoreApplication.translate("MainWindow", u"Hostname", None))
        self.remoteHostLabel.setText(QCoreApplication.translate("MainWindow", u"Remote IP address", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"From", None))
        self.sizeLabel.setText(QCoreApplication.translate("MainWindow", u"Size", None))
        self.nextButton.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.prevButton.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
    # retranslateUi

