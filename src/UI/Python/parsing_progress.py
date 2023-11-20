from PySide6.QtCore import (QCoreApplication, QMetaObject)
from PySide6.QtWidgets import (QGridLayout, QLabel, QProgressBar, QVBoxLayout, QWidget)


class ParsingProgress(object):
    def setup_ui(self, parsing_progress):
        if not parsing_progress.objectName():
            parsing_progress.setObjectName(u"MainWindow")
        parsing_progress.resize(286, 66)
        self.centralwidget = QWidget(parsing_progress)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.verticalLayout.addWidget(self.progressBar)

        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        parsing_progress.setCentralWidget(self.centralwidget)

        self.translate_ui(parsing_progress)

        QMetaObject.connectSlotsByName(parsing_progress)

    def translate_ui(self, parsing_progress):
        parsing_progress.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Parsing", None))
