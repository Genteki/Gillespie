import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import numpy as np
import json

config = json.load(open('config.json'))
projPath = config["projectPath"]
sys.path.append(projPath)

from algorithm.simulator import gillespieSystem

class mainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.system = None
        self.initMenu()
        self.initUI()

    def initMenu(self):
        pass

    def initUI(self):
        pass



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    gui = mainWindow()
    gui.show()
    sys.exit(app.exec_())

