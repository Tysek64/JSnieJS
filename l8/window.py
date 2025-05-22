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
from PySide6.QtWidgets import (QApplication, QDateEdit, QDateTimeEdit, QGridLayout,
    QHBoxLayout, QLCDNumber, QLabel, QLineEdit,
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
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.splitter_2 = QSplitter(self.centralwidget)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Orientation.Vertical)
        self.layoutWidget = QWidget(self.splitter_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.gridLayout_2 = QGridLayout(self.layoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.filenameLabel = QLabel(self.layoutWidget)
        self.filenameLabel.setObjectName(u"filenameLabel")
        self.filenameLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.filenameLabel, 0, 0, 1, 1)

        self.filenameInput = QLineEdit(self.layoutWidget)
        self.filenameInput.setObjectName(u"filenameInput")

        self.gridLayout_2.addWidget(self.filenameInput, 0, 1, 1, 1)

        self.filenameButton = QPushButton(self.layoutWidget)
        self.filenameButton.setObjectName(u"filenameButton")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentOpen))
        self.filenameButton.setIcon(icon)

        self.gridLayout_2.addWidget(self.filenameButton, 0, 2, 1, 1)

        self.fromLabel = QLabel(self.layoutWidget)
        self.fromLabel.setObjectName(u"fromLabel")
        self.fromLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.fromLabel, 1, 0, 1, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)

        self.dateFrom = QDateTimeEdit(self.layoutWidget)
        self.dateFrom.setObjectName(u"dateFrom")

        self.gridLayout_2.addWidget(self.dateFrom, 1, 1, 1, 1)

        self.dateTo = QDateTimeEdit(self.layoutWidget)
        self.dateTo.setObjectName(u"dateTo")
        self.dateTo.setDateTime(QDateTime(QDate(2000, 12, 31), QTime(22, 0, 0)))

        self.gridLayout_2.addWidget(self.dateTo, 2, 1, 1, 1)

        self.applyDateFilter = QPushButton(self.layoutWidget)
        self.applyDateFilter.setObjectName(u"applyDateFilter")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditFind))
        self.applyDateFilter.setIcon(icon1)

        self.gridLayout_2.addWidget(self.applyDateFilter, 1, 2, 1, 1)

        self.splitter_2.addWidget(self.layoutWidget)
        self.splitter = QSplitter(self.splitter_2)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.masterList = QListWidget(self.splitter)
        self.masterList.setObjectName(u"masterList")
        font = QFont()
        font.setFamilies([u"Cascadia Mono"])
        self.masterList.setFont(font)
        self.splitter.addWidget(self.masterList)
        self.layoutWidget1 = QWidget(self.splitter)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.localHostLabel = QLabel(self.layoutWidget1)
        self.localHostLabel.setObjectName(u"localHostLabel")
        self.localHostLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.localHostLabel, 0, 0, 1, 1)

        self.localHostDisplay = QLineEdit(self.layoutWidget1)
        self.localHostDisplay.setObjectName(u"localHostDisplay")
        self.localHostDisplay.setFont(font)
        self.localHostDisplay.setFrame(False)
        self.localHostDisplay.setReadOnly(True)

        self.gridLayout.addWidget(self.localHostDisplay, 0, 1, 1, 1)

        self.remoteHostLabel = QLabel(self.layoutWidget1)
        self.remoteHostLabel.setObjectName(u"remoteHostLabel")
        self.remoteHostLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.remoteHostLabel, 0, 2, 1, 1)

        self.remoteHostDisplay = QLineEdit(self.layoutWidget1)
        self.remoteHostDisplay.setObjectName(u"remoteHostDisplay")
        self.remoteHostDisplay.setFont(font)
        self.remoteHostDisplay.setFrame(False)
        self.remoteHostDisplay.setReadOnly(True)

        self.gridLayout.addWidget(self.remoteHostDisplay, 0, 3, 1, 1)

        self.dateLabel = QLabel(self.layoutWidget1)
        self.dateLabel.setObjectName(u"dateLabel")
        self.dateLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.dateLabel, 1, 0, 1, 1)

        self.dateDisplay = QDateEdit(self.layoutWidget1)
        self.dateDisplay.setObjectName(u"dateDisplay")
        self.dateDisplay.setEnabled(True)
        self.dateDisplay.setFont(font)
        self.dateDisplay.setReadOnly(True)
        self.dateDisplay.setAccelerated(True)

        self.gridLayout.addWidget(self.dateDisplay, 1, 1, 1, 1)

        self.timeLabel = QLabel(self.layoutWidget1)
        self.timeLabel.setObjectName(u"timeLabel")
        self.timeLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.timeLabel, 2, 0, 1, 1)

        self.timeDisplay = QTimeEdit(self.layoutWidget1)
        self.timeDisplay.setObjectName(u"timeDisplay")
        self.timeDisplay.setFont(font)
        self.timeDisplay.setReadOnly(True)
        self.timeDisplay.setAccelerated(True)

        self.gridLayout.addWidget(self.timeDisplay, 2, 1, 1, 1)

        self.statusCodeLabel = QLabel(self.layoutWidget1)
        self.statusCodeLabel.setObjectName(u"statusCodeLabel")
        self.statusCodeLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.statusCodeLabel, 3, 0, 1, 1)

        self.statusCodeDisplay = QLCDNumber(self.layoutWidget1)
        self.statusCodeDisplay.setObjectName(u"statusCodeDisplay")
        self.statusCodeDisplay.setLineWidth(0)
        self.statusCodeDisplay.setDigitCount(3)
        self.statusCodeDisplay.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout.addWidget(self.statusCodeDisplay, 3, 1, 1, 1)

        self.methodLabel = QLabel(self.layoutWidget1)
        self.methodLabel.setObjectName(u"methodLabel")
        self.methodLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.methodLabel, 3, 2, 1, 1)

        self.methodDisplay = QLineEdit(self.layoutWidget1)
        self.methodDisplay.setObjectName(u"methodDisplay")
        self.methodDisplay.setFont(font)
        self.methodDisplay.setFrame(False)
        self.methodDisplay.setReadOnly(True)

        self.gridLayout.addWidget(self.methodDisplay, 3, 3, 1, 1)

        self.resourceLabel = QLabel(self.layoutWidget1)
        self.resourceLabel.setObjectName(u"resourceLabel")
        self.resourceLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.resourceLabel, 4, 0, 1, 1)

        self.sizeLabel = QLabel(self.layoutWidget1)
        self.sizeLabel.setObjectName(u"sizeLabel")
        self.sizeLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.sizeLabel, 5, 0, 1, 1)

        self.sizeDisplay = QLCDNumber(self.layoutWidget1)
        self.sizeDisplay.setObjectName(u"sizeDisplay")
        self.sizeDisplay.setLineWidth(0)
        self.sizeDisplay.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout.addWidget(self.sizeDisplay, 5, 1, 1, 1)

        self.hostnameLabel = QLabel(self.layoutWidget1)
        self.hostnameLabel.setObjectName(u"hostnameLabel")
        self.hostnameLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.hostnameLabel, 5, 2, 1, 1)

        self.hostnameDisplay = QLineEdit(self.layoutWidget1)
        self.hostnameDisplay.setObjectName(u"hostnameDisplay")
        self.hostnameDisplay.setFont(font)
        self.hostnameDisplay.setFrame(False)
        self.hostnameDisplay.setReadOnly(True)

        self.gridLayout.addWidget(self.hostnameDisplay, 5, 3, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 6, 0, 1, 1)

        self.resourceDisplay = QLineEdit(self.layoutWidget1)
        self.resourceDisplay.setObjectName(u"resourceDisplay")
        self.resourceDisplay.setFont(font)
        self.resourceDisplay.setFrame(False)
        self.resourceDisplay.setReadOnly(True)

        self.gridLayout.addWidget(self.resourceDisplay, 4, 1, 1, 3)


        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.prevButton = QPushButton(self.layoutWidget1)
        self.prevButton.setObjectName(u"prevButton")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoPrevious))
        self.prevButton.setIcon(icon2)

        self.horizontalLayout.addWidget(self.prevButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.nextButton = QPushButton(self.layoutWidget1)
        self.nextButton.setObjectName(u"nextButton")
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoNext))
        self.nextButton.setIcon(icon3)

        self.horizontalLayout.addWidget(self.nextButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.splitter.addWidget(self.layoutWidget1)
        self.splitter_2.addWidget(self.splitter)

        self.gridLayout_3.addWidget(self.splitter_2, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.filenameLabel.setText(QCoreApplication.translate("MainWindow", u"Filename:", None))
        self.filenameButton.setText(QCoreApplication.translate("MainWindow", u"Load data", None))
#if QT_CONFIG(shortcut)
        self.filenameButton.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.fromLabel.setText(QCoreApplication.translate("MainWindow", u"From time:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"To time:", None))
        self.dateFrom.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy/MM/dd hh:mm:ss.zzz", None))
        self.dateTo.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy/MM/dd hh:mm:ss.zzz", None))
        self.applyDateFilter.setText(QCoreApplication.translate("MainWindow", u"Apply filter", None))
#if QT_CONFIG(shortcut)
        self.applyDateFilter.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+A", None))
#endif // QT_CONFIG(shortcut)
        self.localHostLabel.setText(QCoreApplication.translate("MainWindow", u"Local IP address", None))
        self.remoteHostLabel.setText(QCoreApplication.translate("MainWindow", u"Remote IP address", None))
        self.dateLabel.setText(QCoreApplication.translate("MainWindow", u"Date", None))
        self.timeLabel.setText(QCoreApplication.translate("MainWindow", u"Time", None))
        self.timeDisplay.setDisplayFormat(QCoreApplication.translate("MainWindow", u"hh:mm:ss.zzz", None))
        self.statusCodeLabel.setText(QCoreApplication.translate("MainWindow", u"Status code", None))
        self.methodLabel.setText(QCoreApplication.translate("MainWindow", u"Method", None))
        self.resourceLabel.setText(QCoreApplication.translate("MainWindow", u"Resource", None))
        self.sizeLabel.setText(QCoreApplication.translate("MainWindow", u"Size", None))
        self.hostnameLabel.setText(QCoreApplication.translate("MainWindow", u"Hostname", None))
        self.prevButton.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
#if QT_CONFIG(shortcut)
        self.prevButton.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+P", None))
#endif // QT_CONFIG(shortcut)
        self.nextButton.setText(QCoreApplication.translate("MainWindow", u"Next", None))
#if QT_CONFIG(shortcut)
        self.nextButton.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

