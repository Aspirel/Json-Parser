from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QGridLayout, QPlainTextEdit,
                               QTabWidget, QWidget)


def TabLayout(window):
    # Tabs
    window.tabWidget = QTabWidget(window.centralwidget)
    window.tabWidget.setObjectName(u"tabWidget")
    window.tabWidget.setStyleSheet("QTabWidget { "
                                   "font-weight: bold;"
                                   "font-size: 12px }")
    jsonFontSize = QFont()
    jsonFontSize.setPointSize(12)

    # tab 1
    window.originalFileTab = QWidget()
    window.originalFileTab.setObjectName(u"tab")
    window.gridLayout_3 = QGridLayout(window.originalFileTab)
    window.gridLayout_3.setObjectName(u"gridLayout_3")
    window.plainTextEdit = QPlainTextEdit(window.originalFileTab)
    window.plainTextEdit.setObjectName(u"plainTextEdit")
    window.plainTextEdit.setReadOnly(True)
    window.plainTextEdit.setFont(jsonFontSize)
    window.gridLayout_3.addWidget(window.plainTextEdit, 0, 0, 1, 1)
    window.tabWidget.addTab(window.originalFileTab, "")

    # tab 2
    window.optionNegativeTab = QWidget()
    window.optionNegativeTab.setObjectName(u"tab_2")
    window.gridLayout_5 = QGridLayout(window.optionNegativeTab)
    window.gridLayout_5.setObjectName(u"gridLayout_5")
    window.plainTextEdit2 = QPlainTextEdit(window.optionNegativeTab)
    window.plainTextEdit2.setObjectName(u"plainTextEdit_2")
    window.plainTextEdit2.setReadOnly(True)
    window.plainTextEdit2.setFont(jsonFontSize)
    window.gridLayout_5.addWidget(window.plainTextEdit2, 0, 0, 1, 1)
    window.tabWidget.addTab(window.optionNegativeTab, "")

    # tab 3
    window.optionPositiveTab = QWidget()
    window.optionPositiveTab.setObjectName(u"tab_3")
    window.gridLayout_4 = QGridLayout(window.optionPositiveTab)
    window.gridLayout_4.setObjectName(u"gridLayout_4")
    window.plainTextEdit3 = QPlainTextEdit(window.optionPositiveTab)
    window.plainTextEdit3.setObjectName(u"plainTextEdit_3")
    window.plainTextEdit3.setReadOnly(True)
    window.gridLayout_4.addWidget(window.plainTextEdit3, 0, 0, 1, 1)
    window.tabWidget.addTab(window.optionPositiveTab, "")
    window.gridLayout.addWidget(window.tabWidget, 0, 1, 1, 1)
    window.tabWidget.setCurrentIndex(0)

    window.tabWidget.setTabText(window.tabWidget.indexOf(window.originalFileTab), "Original")
    window.tabWidget.setTabText(window.tabWidget.indexOf(window.optionNegativeTab), "Duplicates")
    window.tabWidget.setTabText(window.tabWidget.indexOf(window.optionPositiveTab), "No Duplicates")
