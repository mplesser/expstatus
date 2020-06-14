# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'exposure_status.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ExposureStatus(object):
    def setupUi(self, ExposureStatus):
        ExposureStatus.setObjectName(_fromUtf8("ExposureStatus"))
        ExposureStatus.resize(260, 100)
        ExposureStatus.setMinimumSize(QtCore.QSize(260, 100))
        ExposureStatus.setMaximumSize(QtCore.QSize(520, 200))
        font = QtGui.QFont()
        font.setPointSize(8)
        ExposureStatus.setFont(font)
        ExposureStatus.setWhatsThis(_fromUtf8(""))
        ExposureStatus.setIconSize(QtCore.QSize(15, 15))
        self.centralwidget = QtGui.QWidget(ExposureStatus)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_status = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_status.setFont(font)
        self.label_status.setFrameShape(QtGui.QFrame.StyledPanel)
        self.label_status.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_status.setText(_fromUtf8(""))
        self.label_status.setAlignment(QtCore.Qt.AlignCenter)
        self.label_status.setObjectName(_fromUtf8("label_status"))
        self.gridLayout.addWidget(self.label_status, 0, 0, 1, 1)
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.label_integrating = QtGui.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_integrating.setFont(font)
        self.label_integrating.setFrameShape(QtGui.QFrame.StyledPanel)
        self.label_integrating.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_integrating.setLineWidth(2)
        self.label_integrating.setAlignment(QtCore.Qt.AlignCenter)
        self.label_integrating.setObjectName(_fromUtf8("label_integrating"))
        self.label_reading = QtGui.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_reading.setFont(font)
        self.label_reading.setFrameShape(QtGui.QFrame.StyledPanel)
        self.label_reading.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_reading.setLineWidth(2)
        self.label_reading.setAlignment(QtCore.Qt.AlignCenter)
        self.label_reading.setObjectName(_fromUtf8("label_reading"))
        self.gridLayout.addWidget(self.splitter, 1, 0, 1, 1)
        ExposureStatus.setCentralWidget(self.centralwidget)

        self.retranslateUi(ExposureStatus)
        QtCore.QMetaObject.connectSlotsByName(ExposureStatus)

    def retranslateUi(self, ExposureStatus):
        ExposureStatus.setWindowTitle(_translate("ExposureStatus", "ExpStatus", None))
        ExposureStatus.setToolTip(_translate("ExposureStatus", "azcam exposure status", None))
        self.label_integrating.setText(_translate("ExposureStatus", "Exposing", None))
        self.label_reading.setText(_translate("ExposureStatus", "Reading", None))

