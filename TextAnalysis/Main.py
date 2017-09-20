from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

import sys



app = QApplication(sys.argv)

MainWindow = uic.loadUi('UIFiles/MainWindow.ui')


MainWindow.show()
sys.exit(app.exec_())