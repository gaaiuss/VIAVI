# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(912, 703)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.mainGrid = QGridLayout()
        self.mainGrid.setObjectName(u"mainGrid")
        self.mainGrid.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.mainGrid.setContentsMargins(0, -1, -1, -1)
        self.buttonsGrid = QGridLayout()
        self.buttonsGrid.setObjectName(u"buttonsGrid")
        self.buttonsGrid.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.buttonsGrid.setHorizontalSpacing(50)
        self.buttonsGrid.setContentsMargins(100, -1, -1, -1)
        self.selectedFilesLabel = QLabel(self.centralwidget)
        self.selectedFilesLabel.setObjectName(u"selectedFilesLabel")

        self.buttonsGrid.addWidget(self.selectedFilesLabel, 0, 1, 1, 1)

        self.selectButton = QPushButton(self.centralwidget)
        self.selectButton.setObjectName(u"selectButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.selectButton.sizePolicy().hasHeightForWidth())
        self.selectButton.setSizePolicy(sizePolicy1)
        self.selectButton.setMinimumSize(QSize(50, 50))
        self.selectButton.setMaximumSize(QSize(200, 16777215))

        self.buttonsGrid.addWidget(self.selectButton, 0, 0, 1, 1)

        self.convertButton = QPushButton(self.centralwidget)
        self.convertButton.setObjectName(u"convertButton")
        self.convertButton.setMinimumSize(QSize(0, 50))
        self.convertButton.setMaximumSize(QSize(130, 16777215))

        self.buttonsGrid.addWidget(self.convertButton, 1, 0, 1, 1)

        self.savedReportPath = QLabel(self.centralwidget)
        self.savedReportPath.setObjectName(u"savedReportPath")

        self.buttonsGrid.addWidget(self.savedReportPath, 1, 1, 1, 1)


        self.mainGrid.addLayout(self.buttonsGrid, 2, 0, 1, 1)

        self.labelsLayout = QHBoxLayout()
        self.labelsLayout.setSpacing(50)
        self.labelsLayout.setObjectName(u"labelsLayout")
        self.labelsLayout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.labelsLayout.setContentsMargins(20, -1, -1, -1)
        self.labelLogo = QLabel(self.centralwidget)
        self.labelLogo.setObjectName(u"labelLogo")
        self.labelLogo.setMaximumSize(QSize(400, 70))
        self.labelLogo.setPixmap(QPixmap(u"../img/ui_icon.png"))
        self.labelLogo.setScaledContents(True)
        self.labelLogo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.labelLogo.setMargin(0)

        self.labelsLayout.addWidget(self.labelLogo)

        self.labelText = QLabel(self.centralwidget)
        self.labelText.setObjectName(u"labelText")
        self.labelText.setMaximumSize(QSize(16777215, 100))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(20)
        self.labelText.setFont(font)
        self.labelText.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.labelsLayout.addWidget(self.labelText)


        self.mainGrid.addLayout(self.labelsLayout, 0, 0, 1, 1)


        self.horizontalLayout.addLayout(self.mainGrid)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 912, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"VIAVI OLP-39 Report Generator", None))
        self.selectedFilesLabel.setText("")
        self.selectButton.setText(QCoreApplication.translate("MainWindow", u"Select Json Files", None))
        self.convertButton.setText(QCoreApplication.translate("MainWindow", u"Generate Report", None))
        self.savedReportPath.setText("")
        self.labelLogo.setText("")
        self.labelText.setText(QCoreApplication.translate("MainWindow", u"OLP-39 Report Generator", None))
    # retranslateUi

