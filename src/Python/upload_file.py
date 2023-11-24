from PySide6.QtCore import (QCoreApplication, Qt)
from PySide6.QtWidgets import (QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog)

from main_window import MainWindow


class UploadFile(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_window = None
        self.pushButton = None
        self.verticalLayout = None
        self.centralwidget = None

    def setupUi(self, uploadFileWindow):
        if not uploadFileWindow.objectName():
            uploadFileWindow.setObjectName(u"MainWindow")
        uploadFileWindow.resize(400, 66)
        self.centralwidget = QWidget(uploadFileWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")

        # Button
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet("QPushButton {"
                                      "color: white; "
                                      "font-weight: bold;"
                                      "font-size: 15px;"
                                      "width: 150px; "
                                      "height: 25px}")
        self.pushButton.clicked.connect(self.setupFile)
        self.pushButton.clicked.connect(uploadFileWindow.close)

        # General setup
        self.verticalLayout.addWidget(self.pushButton, 0, Qt.AlignHCenter | Qt.AlignVCenter)
        uploadFileWindow.setCentralWidget(self.centralwidget)
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Upload file", None))

    def setupFile(self):
        file_dialog = QFileDialog()
        selected_file = file_dialog.getOpenFileName(None, "Select File")

        if isinstance(selected_file, tuple) and selected_file[0]:
            self.main_window = MainWindow(selected_file)
            self.main_window.show()
