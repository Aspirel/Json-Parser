import time

from PySide6.QtCore import (QCoreApplication, QMetaObject)
from PySide6.QtWidgets import (QGridLayout, QPlainTextEdit,
                               QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
                               QTabWidget, QVBoxLayout, QWidget, QProgressBar)


class MainWindow(object):

    def __init__(self):
        self.progressBar = None
        self.window = None
        self.widget = None
        self.a = None
        self.finished = None
        self.helper = None
        self.fileContent = None
        self.currentWindow = None
        self.verticalSpacer = None
        self.pushButton = None
        self.fileLengthRadioButton = None
        self.removeDuplicatesRadioButton = None
        self.removeEmptyRadioButton = None
        self.removeNullRadioButton = None
        self.verticalLayout_2 = None
        self.plainTextEdit_3 = None
        self.gridLayout_4 = None
        self.plainTextEdit_2 = None
        self.gridLayout_5 = None
        self.originalFileTab = None
        self.optionNegativeTab = None
        self.optionPositiveTab = None
        self.plainTextEdit = None
        self.gridLayout_3 = None
        self.tabWidget = None
        self.gridLayout = None
        self.gridLayout_2 = None
        self.centralwidget = None

    def setup_ui(self, currentWindow, selectedFile):
        self.currentWindow = currentWindow
        if not self.currentWindow.objectName():
            self.currentWindow.setObjectName(u"JSONParser")
        self.currentWindow.resize(1000, 600)
        self.centralwidget = QWidget(self.currentWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        # Main grid
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")

        # Inner grid
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")

        # Tabs
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet("QTabWidget { "
                                     "font-weight: bold;"
                                     "font-size: 12px }")

        # tab 1
        self.originalFileTab = QWidget()
        self.originalFileTab.setObjectName(u"tab")
        self.gridLayout_3 = QGridLayout(self.originalFileTab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.plainTextEdit = QPlainTextEdit(self.originalFileTab)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setReadOnly(True)
        self.gridLayout_3.addWidget(self.plainTextEdit, 0, 0, 1, 1)
        self.tabWidget.addTab(self.originalFileTab, "")

        # tab 2
        self.optionNegativeTab = QWidget()
        self.optionNegativeTab.setObjectName(u"tab_2")
        self.gridLayout_5 = QGridLayout(self.optionNegativeTab)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.plainTextEdit_2 = QPlainTextEdit(self.optionNegativeTab)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setReadOnly(True)
        self.gridLayout_5.addWidget(self.plainTextEdit_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.optionNegativeTab, "")

        # tab 3
        self.optionPositiveTab = QWidget()
        self.optionPositiveTab.setObjectName(u"tab_3")
        self.gridLayout_4 = QGridLayout(self.optionPositiveTab)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.plainTextEdit_3 = QPlainTextEdit(self.optionPositiveTab)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")
        self.plainTextEdit_3.setReadOnly(True)
        self.gridLayout_4.addWidget(self.plainTextEdit_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.optionPositiveTab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)
        # End tabs

        # radio buttons vertical layout
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.fileLengthRadioButton = QRadioButton(self.centralwidget)
        self.fileLengthRadioButton.setObjectName(u"radioButton_5")
        self.fileLengthRadioButton.setAutoExclusive(False)
        self.verticalLayout_2.addWidget(self.fileLengthRadioButton)
        self.removeDuplicatesRadioButton = QRadioButton(self.centralwidget)
        self.removeDuplicatesRadioButton.setObjectName(u"radioButton_6")
        self.removeDuplicatesRadioButton.setAutoExclusive(False)
        self.verticalLayout_2.addWidget(self.removeDuplicatesRadioButton)
        self.removeEmptyRadioButton = QRadioButton(self.centralwidget)
        self.removeEmptyRadioButton.setObjectName(u"radioButton_7")
        self.removeEmptyRadioButton.setAutoExclusive(False)
        self.verticalLayout_2.addWidget(self.removeEmptyRadioButton)
        self.removeNullRadioButton = QRadioButton(self.centralwidget)
        self.removeNullRadioButton.setObjectName(u"radioButton_8")
        self.removeNullRadioButton.setAutoExclusive(False)
        self.verticalLayout_2.addWidget(self.removeNullRadioButton)

        # start parsing button
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet("QPushButton { "
                                      "max-width: 170;"
                                      "font-weight: bold;"
                                      "font-size: 12px }")
        self.verticalLayout_2.addWidget(self.pushButton)

        # Progress bar
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setStyleSheet("QProgressBar { "
                                       "max-width: 170; "
                                       "text-align: center;"
                                       "font-size: 14px;"
                                       "color: white;"
                                       "font-weight: bold;}"

                                       "QProgressBar::chunk"
                                       "{"
                                       "background-color : #2cde85;"
                                       "}")

        self.verticalLayout_2.addWidget(self.progressBar)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(self.verticalSpacer)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        currentWindow.setCentralWidget(self.centralwidget)
        self.translate_ui(currentWindow)
        self.tabWidget.setCurrentIndex(0)
        self.fileContent = selectedFile[0]
        self.plainTextEdit.setPlainText(self.fileContent)
        self.pushButton.clicked.connect(self.start_parse)

        QMetaObject.connectSlotsByName(currentWindow)

    def parse(self, value):
        for i in range(100):
            time.sleep(0.01)
            self.progressBar.setValue(i + 1)

    def start_parse(self):
        self.parse(self.fileContent)
        # self.window = QMainWindow()
        # parsing_progress = ParsingProgress(self.window)
        # self.window.show()
        # parsing_progress.parse(self.fileContent)

    def translate_ui(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("MainWindow", u"JSON Parser", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.originalFileTab),
                                  QCoreApplication.translate("MainWindow", u"Original", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.optionNegativeTab),
                                  QCoreApplication.translate("MainWindow", u"Duplicates", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.optionPositiveTab),
                                  QCoreApplication.translate("MainWindow", u"No Duplicates", None))
        self.fileLengthRadioButton.setText(QCoreApplication.translate("MainWindow", u"Check file length", None))
        self.removeDuplicatesRadioButton.setText(
            QCoreApplication.translate("MainWindow", u"Remove duplicate values", None))
        self.removeEmptyRadioButton.setText(QCoreApplication.translate("MainWindow", u"Remove empty values", None))
        self.removeNullRadioButton.setText(QCoreApplication.translate("MainWindow", u"Remove null values", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Start parse", None))
