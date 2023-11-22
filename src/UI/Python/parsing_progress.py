import time

from PySide6.QtCore import (QCoreApplication, QMetaObject)
from PySide6.QtWidgets import (QLabel, QProgressBar, QVBoxLayout, QWidget, QMainWindow)


class ParsingProgress(QMainWindow):
    def __init__(self, parsing_progress):
        super().__init__()
        self.progressBar = None
        self.label = None
        self.verticalLayout = None
        self.centralwidget = None
        self.setup_ui(parsing_progress)

    def setup_ui(self, parsing_progress):
        if not parsing_progress.objectName():
            parsing_progress.setObjectName(u"ParsingProgress")
        parsing_progress.resize(200, 66)
        self.centralwidget = QWidget(parsing_progress)
        self.centralwidget.setObjectName(u"centralwidget")

        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.verticalLayout.addWidget(self.label)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.verticalLayout.addWidget(self.progressBar)
        parsing_progress.setCentralWidget(self.centralwidget)

        self.translate_ui(parsing_progress)
        QMetaObject.connectSlotsByName(parsing_progress)

    def parse(self, value):
        for i in range(100):
            time.sleep(0.01)
            self.progressBar.setValue(i + 1)

    def translate_ui(self, parsing_progress):
        parsing_progress.setWindowTitle(QCoreApplication.translate("MainWindow", u"JSON Parser", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Parsing", None))