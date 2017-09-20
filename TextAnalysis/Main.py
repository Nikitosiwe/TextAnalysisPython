import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QFileDialog

from PYModules.AuxiliaryMethods import *


app = QApplication(sys.argv)

MainWindow = uic.loadUi('UIFiles/MainWindow.ui')


#Методы нажатия соответствующих кнопок
def BrowseButton_click():
    pass

def searchButton_click():
    if not checkAnalysisText(MainWindow.plainTextEdit.toPlainText()):
        return

    print('Text')


#Подключение методов к кнопкам
MainWindow.BrowseButton.clicked.connect(BrowseButton_click)
MainWindow.searchButton.clicked.connect(searchButton_click)



#Показ главного окна и старт приложения.
MainWindow.show()
sys.exit(app.exec_())