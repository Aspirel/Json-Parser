from PySide6.QtCore import (QCoreApplication, QMetaObject, Qt)
from PySide6.QtGui import (QPalette)
from PySide6.QtWidgets import (QApplication, QPushButton, QVBoxLayout, QWidget, QFileDialog)

from .main_window import MainWindow


class UploadFile(object):
    def __init__(self):
        self.main_window = None
        self.pushButton = None
        self.verticalLayout = None
        self.centralwidget = None
        self.current_window = None
        system_palette = QApplication.palette()
        QApplication.setStyle("Fusion")
        self.window_color = system_palette.color(QPalette.Window)

    def setup_ui(self, upload_file):
        self.current_window = upload_file
        if not self.current_window.objectName():
            self.current_window.setObjectName(u"MainWindow")
        self.current_window.setPalette(QPalette(self.window_color))
        self.current_window.resize(400, 66)
        self.centralwidget = QWidget(self.current_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet("QWidget {background-color: #181a1b}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")

        # Button
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet("QPushButton {background-color: #2cde85; color: black; font-weight: bold}")
        self.pushButton.clicked.connect(self.upload_file)

        # General setup
        self.verticalLayout.addWidget(self.pushButton, 0, Qt.AlignHCenter | Qt.AlignVCenter)
        self.current_window.setCentralWidget(self.centralwidget)
        upload_file.setWindowTitle(QCoreApplication.translate("MainWindow", u"JSON Parser", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Upload file", None))
        QMetaObject.connectSlotsByName(self.current_window)

    def upload_file(self):
        file_dialog = QFileDialog()
        selected_file = file_dialog.getOpenFileName(None, "Select File")

        if isinstance(selected_file, tuple) and selected_file[0]:
            self.main_window = MainWindow()
            self.main_window.setup_ui(self.current_window, selected_file)
