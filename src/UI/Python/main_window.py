from PySide6.QtCore import (QCoreApplication, QMetaObject)
from PySide6.QtWidgets import (QGridLayout, QPlainTextEdit,
                               QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
                               QTabWidget, QVBoxLayout, QWidget)


class MainWindow(object):
    def setup_ui(self, currentWindow, selected_file):
        if not currentWindow.objectName():
            currentWindow.setObjectName(u"JSONParser")
        currentWindow.resize(800, 609)
        self.centralwidget = QWidget(currentWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()

        # Tabs
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")

        # tab 1
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_3 = QGridLayout(self.tab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.plainTextEdit = QPlainTextEdit(self.tab)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.gridLayout_3.addWidget(self.plainTextEdit, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")

        # tab 2
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_5 = QGridLayout(self.tab_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.plainTextEdit_2 = QPlainTextEdit(self.tab_2)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setToolTipDuration(0)
        self.plainTextEdit_2.setReadOnly(False)
        self.plainTextEdit_2.setBackgroundVisible(False)
        self.gridLayout_5.addWidget(self.plainTextEdit_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")

        # tab 3
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_4 = QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.plainTextEdit_3 = QPlainTextEdit(self.tab_3)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")
        self.plainTextEdit_3.setToolTipDuration(0)
        self.plainTextEdit_3.setReadOnly(False)
        self.plainTextEdit_3.setBackgroundVisible(False)
        self.gridLayout_4.addWidget(self.plainTextEdit_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)
        # End tabs

        # radio buttons vertical layout
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.radioButton_5 = QRadioButton(self.centralwidget)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setAutoExclusive(False)
        self.verticalLayout_2.addWidget(self.radioButton_5)
        self.radioButton_6 = QRadioButton(self.centralwidget)
        self.radioButton_6.setObjectName(u"radioButton_6")
        self.radioButton_6.setAutoExclusive(False)
        self.verticalLayout_2.addWidget(self.radioButton_6)
        self.radioButton_7 = QRadioButton(self.centralwidget)
        self.radioButton_7.setObjectName(u"radioButton_7")
        self.radioButton_7.setAutoExclusive(False)
        self.verticalLayout_2.addWidget(self.radioButton_7)
        self.radioButton_8 = QRadioButton(self.centralwidget)
        self.radioButton_8.setObjectName(u"radioButton_8")
        self.radioButton_8.setAutoExclusive(False)
        self.verticalLayout_2.addWidget(self.radioButton_8)

        # start parsing button
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(self.verticalSpacer)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        currentWindow.setCentralWidget(self.centralwidget)
        self.translate_ui(currentWindow)
        self.tabWidget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(currentWindow)

        self.plainTextEdit.setPlainText(selected_file[0])

    def translate_ui(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("MainWindow", u"JSON Parser", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab),
                                  QCoreApplication.translate("MainWindow", u"Original", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2),
                                  QCoreApplication.translate("MainWindow", u"Duplicates", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3),
                                  QCoreApplication.translate("MainWindow", u"No Duplicates", None))
        self.radioButton_5.setText(QCoreApplication.translate("MainWindow", u"Check file length", None))
        self.radioButton_6.setText(QCoreApplication.translate("MainWindow", u"Remove duplicate values", None))
        self.radioButton_7.setText(QCoreApplication.translate("MainWindow", u"Remove empty values", None))
        self.radioButton_8.setText(QCoreApplication.translate("MainWindow", u"Remove null values", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Start parse", None))
