import json

from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QGridLayout, QPlainTextEdit,
                               QTabWidget, QWidget)

jsonFontSize = QFont()
jsonFontSize.setPointSize(12)


def TabLayout(window):
    # Tabs
    window.tabWidget = QTabWidget()
    window.tabWidget.setObjectName(u"tabWidget")
    window.tabWidget.setStyleSheet("QTabWidget { "
                                   "font-weight: bold;"
                                   "font-size: 12px }")

    # tab 1
    window.originalFileTab = QWidget(window.tabWidget)
    window.tab1GridLayout = QGridLayout(window.originalFileTab)
    window.plainTextEdit = QPlainTextEdit(window.originalFileTab)
    window.plainTextEdit.setReadOnly(True)
    window.plainTextEdit.setFont(jsonFontSize)
    window.tab1GridLayout.addWidget(window.plainTextEdit, 0, 0, 1, 1)
    window.tabWidget.addTab(window.originalFileTab, "")
    window.gridLayout.addWidget(window.tabWidget, 0, 1, 1, 1)
    window.tabWidget.setTabText(
        window.tabWidget.indexOf(window.originalFileTab), "File")


def ResultTabs(window, tabName, resultItems, foundItems):
    # tab 2
    window.optionNegativeTab = QWidget(window.tabWidget)
    window.tab3gridLayout = QGridLayout(window.optionNegativeTab)
    window.plainTextEdit2 = QPlainTextEdit(window.optionNegativeTab)
    window.plainTextEdit2.setReadOnly(True)
    window.plainTextEdit2.setFont(jsonFontSize)
    window.plainTextEdit2.setPlainText(json.dumps(
        resultItems, indent=4, ensure_ascii=False))
    window.tab3gridLayout.addWidget(window.plainTextEdit2, 0, 0, 1, 1)
    window.tabWidget.addTab(window.optionNegativeTab, tabName)

    # tab 3
    window.optionPositiveTab = QWidget(window.tabWidget)
    window.tab2gridLayout = QGridLayout(window.optionPositiveTab)
    window.plainTextEdit3 = QPlainTextEdit(window.optionPositiveTab)
    window.plainTextEdit3.setReadOnly(True)
    window.plainTextEdit3.setFont(jsonFontSize)
    window.plainTextEdit3.setPlainText(json.dumps(
        foundItems, indent=4, ensure_ascii=False))
    window.tab2gridLayout.addWidget(window.plainTextEdit3, 0, 0, 1, 1)
    window.tabWidget.addTab(window.optionPositiveTab, "Result")
