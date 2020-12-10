# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'expstatus.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    Qt,
    QTime,
    QUrl,
)
from PySide2.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QIcon,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
)
from PySide2.QtWidgets import *


class Ui_ExposureStatus(object):
    def setupUi(self, ExposureStatus):
        if not ExposureStatus.objectName():
            ExposureStatus.setObjectName(u"ExposureStatus")
        ExposureStatus.resize(260, 100)
        ExposureStatus.setMinimumSize(QSize(260, 100))
        ExposureStatus.setMaximumSize(QSize(520, 200))
        font = QFont()
        font.setPointSize(8)
        ExposureStatus.setFont(font)
        ExposureStatus.setIconSize(QSize(15, 15))
        self.centralwidget = QWidget(ExposureStatus)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_status = QLabel(self.centralwidget)
        self.label_status.setObjectName(u"label_status")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_status.setFont(font1)
        self.label_status.setFrameShape(QFrame.StyledPanel)
        self.label_status.setFrameShadow(QFrame.Sunken)
        self.label_status.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_status, 0, 0, 1, 1)

        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.label_integrating = QLabel(self.splitter)
        self.label_integrating.setObjectName(u"label_integrating")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setWeight(50)
        self.label_integrating.setFont(font2)
        self.label_integrating.setFrameShape(QFrame.StyledPanel)
        self.label_integrating.setFrameShadow(QFrame.Sunken)
        self.label_integrating.setLineWidth(2)
        self.label_integrating.setAlignment(Qt.AlignCenter)
        self.splitter.addWidget(self.label_integrating)
        self.label_reading = QLabel(self.splitter)
        self.label_reading.setObjectName(u"label_reading")
        self.label_reading.setFont(font2)
        self.label_reading.setFrameShape(QFrame.StyledPanel)
        self.label_reading.setFrameShadow(QFrame.Sunken)
        self.label_reading.setLineWidth(2)
        self.label_reading.setAlignment(Qt.AlignCenter)
        self.splitter.addWidget(self.label_reading)

        self.gridLayout.addWidget(self.splitter, 1, 0, 1, 1)

        ExposureStatus.setCentralWidget(self.centralwidget)

        self.retranslateUi(ExposureStatus)

        QMetaObject.connectSlotsByName(ExposureStatus)

    # setupUi

    def retranslateUi(self, ExposureStatus):
        ExposureStatus.setWindowTitle(
            QCoreApplication.translate("ExposureStatus", u"ExpStatus", None)
        )
        # if QT_CONFIG(tooltip)
        ExposureStatus.setToolTip(
            QCoreApplication.translate("ExposureStatus", u"azcam exposure status", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        ExposureStatus.setWhatsThis("")
        # endif // QT_CONFIG(whatsthis)
        self.label_status.setText("")
        self.label_integrating.setText(
            QCoreApplication.translate("ExposureStatus", u"Exposing", None)
        )
        self.label_reading.setText(
            QCoreApplication.translate("ExposureStatus", u"Reading", None)
        )

    # retranslateUi
