import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QFileDialog
from PyQt5.QtGui import QPalette, QColor, QTextCursor, QStandardItemModel, QStandardItem

from PYModules.AuxiliaryMethods import *


app = QApplication(sys.argv)

MainWindow = uic.loadUi('UIFiles/MainWindow.ui')
TextAnalysisWindow = uic.loadUi('UIFiles/TextAnalysisWindow.ui')


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

    #Слова которые ищут
    searchWords = getWordsFromString(searchText)
    if len(searchWords)<1: return

    #Все слова текста
    words = getWordsFromString(analysisText)


    #Найденные слова
    detectedWords = {k:words[k] for k in searchWords.keys() if k in words.keys() }

def textAnalysisButton_click():
    print(analysisText(MainWindow.plainTextEdit.toPlainText()))

    print('kykyk')
    TextAnalysisWindow.show()
    view = TextAnalysisWindow.columnView

    model = QStandardItemModel()

    try:
        for groupnum in range(3):
            group = QStandardItem("Group %s" %(groupnum))

            for personnum in range(5):
                child = QStandardItem("Person %s (group %s)"% (personnum, groupnum))

                group.appendRow(child)

            model.appendRow(group);

        view.setModel(model)
    except Exception as ex:
        print(ex)


#Подключение методов к кнопкам
MainWindow.BrowseButton.clicked.connect(browseButton_click)
MainWindow.searchButton.clicked.connect(searchButton_click)
MainWindow.textAnalysisButton.clicked.connect(textAnalysisButton_click)

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