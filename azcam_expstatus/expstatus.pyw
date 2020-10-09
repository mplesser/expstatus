# GUI for exposurestatus process

# Qt4 version

import sys
import time

from PySide2 import QtCore, QtGui
from PySide2.QtWidgets import QMainWindow, QWidget, QApplication

import azcam
import azcam.console
from azcam.sockets import SocketInterface
from expstatus_ui import Ui_ExposureStatus


class ExposureStatus(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()

        MainWindow = QMainWindow()
        self.ui = Ui_ExposureStatus()
        self.ui.setupUi(self)

        self.update_interval = 200  # update time
        self.flags = azcam.db.exposureflags

        # blank text on indicators
        self.ui.label_integrating.setText("")
        self.ui.label_reading.setText("")

        # make a timer
        self.timerID = self.ctimer = QtCore.QTimer()

        # connect timer
        QtCore.QObject.connect(self.ctimer, QtCore.SIGNAL("timeout()"), self.timer_update)

        # start timer
        self.ctimer.start(self.update_interval)

    def timer_update(self):
        """
        Called by timer.
        """

        return self.update()

    def update(self):
        """
        Update GUI indicators.
        """

        # set status text
        status = azcam.console.api.get_par("exposureflag")

        for key in self.flags:
            if self.flags[key] == status:
                if key == "NONE":
                    self.ui.label_status.setText("")
                    self.ui.label_reading.setStyleSheet("background-color: none;")
                    self.ui.label_integrating.setStyleSheet("background-color: none;")
                    self.ui.label_integrating.setText("")
                    self.ui.label_reading.setText("")
                else:
                    # set status text
                    self.ui.label_status.setText(key)
                    # set indicator colors
                    if key == "EXPOSING":
                        self.ui.label_integrating.setStyleSheet("background-color: green;")
                        self.ui.label_reading.setStyleSheet("background-color: none;")
                        self.ui.label_integrating.setText("Exposing")
                        self.ui.label_reading.setText("")
                    elif key == "READOUT":
                        self.ui.label_reading.setStyleSheet("background-color: red;")
                        self.ui.label_integrating.setStyleSheet("background-color: none;")
                        self.ui.label_reading.setText("Reading")
                        self.ui.label_integrating.setText("")
                    else:
                        self.ui.label_reading.setStyleSheet("background-color: none;")
                        self.ui.label_integrating.setStyleSheet("background-color: none;")
                        self.ui.label_integrating.setText("")
                        self.ui.label_reading.setText("")

                break

        return

    def start(self):

        # create
        if getattr(azcam.db, "qtapp", None) is None:
            azcam.db.qtapp = QApplication(["ExpStatus"])

        # set window location
        self.move(50, 50)

        # show GUI
        self.show()

        return


# execute when run directly
if __name__ == "__main__":

    # ****************************************************************
    # parse command line arguments
    # ****************************************************************
    try:
        i = sys.argv.index("-port")
        port = int(sys.argv[i + 1])
    except ValueError:
        port = 2402

    # ****************************************************************
    # create Qt app
    # ****************************************************************
    if azcam.db.get("atapp") is None:
        qtapp = QtCore.QCoreApplication.instance()
        if qtapp is None:
            qtapp = QApplication(sys.argv)
        azcam.db.qtapp = qtapp

    connected = azcam.console.api.connect(port=port)  # default host and port
    if connected:
        print("Connected to azcamserver")
    else:
        print("Not connected to azcamserver")
        time.sleep(2)
        raise azcam.AzcamError("Could not connect to AzCamSever")

    gui = ExposureStatus()
    gui.start()

    # if not running in IPython, wait...
    try:
        get_ipython()
    except Exception as m:
        qtapp.exec_()
