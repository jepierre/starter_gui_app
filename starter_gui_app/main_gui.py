# -*- coding: utf-8 -*-
""" 
    Starter App
"""

import logging
import os
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from starter_gui_app.utils import create_logger, excepthook

logger = logging.getLogger("main-gui")


class MainGui(QMainWindow):
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        self.init_ui()

        self.show()

    def init_ui(self):
        logger.debug("test logger")

    def exit_app(self):
        logger.debug("Exiting")
        sys.exit(0)


def main():

    create_logger()

    # Set global exception handler.
    sys.excepthook = excepthook

    # Open the app
    app = QApplication(sys.argv)
    App = MainGui()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
