import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QFileDialog
from PyQt5.QtGui import QPalette, QColor, QTextCursor

from PYModules.AuxiliaryMethods import *


app = QApplication(sys.argv)

MainWindow = uic.loadUi('UIFiles/MainWindow.ui')


MainWindow.plainTextEdit.setPlainText('s dfh akjsdhfkajs dhfka sdkjfh aslkjdf hajsdhfkjas asjdkf askd fhak')


#Методы нажатия соответствующих кнопок
def browseButton_click():
    pass

def searchButton_click():
    analysisText = MainWindow.plainTextEdit.toPlainText()
    searchText = MainWindow.searchLineEdit.text()
    if not checkAnalysisText(analysisText):
        return
    if not checkAnalysisText(searchText):
        return

    searchWords = getWordsFromString(searchText)
    if len(searchWords)<1: return

    words = getWordsFromString(analysisText)

    print(searchWord(searchWords[0], analysisText))

    #result = list(set(worlds) & set(searchWorlds))
    #print(result)
    #print(getWorldsFromString(analysisText))



    print('Text')


#Подключение методов к кнопкам
MainWindow.BrowseButton.clicked.connect(browseButton_click)
MainWindow.searchButton.clicked.connect(searchButton_click)

"""
p = MainWindow.plainTextEdit.palette()
p.setColor(QPalette.Highlight, QColor('Red'))
MainWindow.plainTextEdit.setPalette(p)

c = MainWindow.plainTextEdit.textCursor()
c.setPosition(5);
c.setPosition(10, QTextCursor.KeepAnchor)
MainWindow.plainTextEdit.setTextCursor(c);

c = MainWindow.plainTextEdit.textCursor()
c.setPosition(30);
c.setPosition(40, QTextCursor.KeepAnchor)
MainWindow.plainTextEdit.setTextCursor(c);
"""


#Показ главного окна и старт приложения.
MainWindow.show()
sys.exit(app.exec_())