import sys
import matplotlib.pyplot as plt
import numpy as np

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
    stopText = MainWindow.stopWordLineEdit.text()
    print(stopText)
    if not checkAnalysisText(analysisText):
        return
    if not checkAnalysisText(searchText):
        return

    #Слова которые ищут
    searchWords = getWordsFromString(searchText)
    if len(searchWords)<1: return

    #Все слова текста
    words = getWordsFromString(analysisText)

    #Стоп слова
    #print()

    #Найденные слова
    detectedWords = {k:words[k] for k in searchWords.keys() if k in words.keys() }
    print(detectedWords)

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

    TextAnalysisWindow.show()


def graphicsTextAnalysisButton_click():
    analysisText = MainWindow.plainTextEdit.toPlainText()
    stopText = MainWindow.stopWordLineEdit.text()
    words = getWordsFromString(analysisText)
    stopWords = getWordsFromString(stopText)
    morphWords = getMorphWords(words)
    segnifikentWords = list(set(morphWords[0])-set(stopWords.keys()))

    #print(segnifikentWords)
    #print(list(set(segnifikentWords)-set(stopWords.keys())))
    t = sorted([(x,len(words[x])) for x in segnifikentWords], key=lambda x: x[1], reverse=True)
    tmp = t[:5]

    plt.close('all')

    ax1 = plt.subplot2grid((2, 2), (0, 0))
    ax2 = plt.subplot2grid((2, 2), (0, 1))
    ax3 = plt.subplot2grid((2, 2), (1, 0))
    ax4 = plt.subplot2grid((2, 2), (1, 1))

    if len(tmp)>0:

        ax1.bar(range(len(tmp)), [x[1] for x in tmp], width=0.5, tick_label=[x[0] for x in tmp])

        x = np.arange(tmp[0][1], 0, 0.01)

        ax2.pie([x[1] for x in tmp], labels=[x[0] for x in tmp], autopct='%1.1f%%')

        ax3.plot(range(len(tmp)), [x[1] for x in tmp], range(len(tmp)),[x[1] for x in tmp], 'ro')

        ax4.plot(x, x**2)

    plt.tight_layout()

    plt.show()

#Подключение методов к кнопкам
MainWindow.BrowseButton.clicked.connect(browseButton_click)
MainWindow.searchButton.clicked.connect(searchButton_click)
MainWindow.textAnalysisButton.clicked.connect(textAnalysisButton_click)
MainWindow.graphicsTextAnalysisButton.clicked.connect(graphicsTextAnalysisButton_click)


#Показ главного окна и старт приложения.
MainWindow.show()
sys.exit(app.exec_())