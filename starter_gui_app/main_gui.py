# -*- coding: utf-8 -*-
""" 
    Starter App
"""

import logging
import os
import sys
from PyQt5 import uic
from PyQt5.QtCore import QCoreApplication, Qt
from starter_gui_app.utils.utils import __appname__
from starter_gui_app.version import __version__

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QTableWidgetItem,
    QFileDialog,
    QMessageBox,
)
from starter_gui_app.utils.utils import create_logger, excepthook

logger = logging.getLogger("main-gui")


class MainGui(QMainWindow):
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)

        self.init_ui()

        self.show()

    def init_ui(self):
        uic.loadUi(r"ui_files\main.ui", self)
        logger.debug("loading main.ui")
        self.setWindowTitle(__appname__)
        logger.debug("test logger")

    def exit_app(self):
        logger.debug("Exiting")
        sys.exit(0)


def main():

    os.chdir(os.path.dirname(__file__))
    QCoreApplication.setApplicationName(__appname__)
    QCoreApplication.setApplicationVersion(__version__)
    QCoreApplication.setOrganizationName(__appname__)
    QCoreApplication.setOrganizationDomain(__appname__)

    create_logger()

    # Set global exception handler.
    sys.excepthook = excepthook

    # Open the app
    app = QApplication(sys.argv)
    App = MainGui()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
