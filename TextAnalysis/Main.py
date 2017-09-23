import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QFileDialog, QTableWidget, QTableWidgetItem, QGridLayout
from PyQt5.QtGui import QPalette, QColor, QTextCursor, QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt

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
    analysis = analysisText(MainWindow.plainTextEdit.toPlainText())

    table = TextAnalysisWindow.tableWidget  # Создаём таблицу

    table.setColumnCount(2)  # Устанавливаем три колонки
    table.setRowCount(len(analysis))  # и одну строку в таблице

    # Устанавливаем заголовки таблицы
    table.setHorizontalHeaderLabels(["Параметры", "Значения"])

    # заполняем таблицу
    for i,item in enumerate(analysis):
        parametr = QTableWidgetItem(item[0])
        parametr.setFlags(Qt.ItemIsEditable)
        table.setItem(i, 0, parametr)

        value = QTableWidgetItem(str(item[1]))
        value.setFlags(Qt.ItemIsEditable)
        table.setItem(i, 1, value)


    # делаем ресайз колонок по содержимому
    table.resizeColumnsToContents()


    #grid_layout.addWidget(table, 0, 0)  # Добавляем таблицу в сетку

    TextAnalysisWindow.show()


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