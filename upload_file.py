from PySide6.QtCore import (QCoreApplication, QMetaObject, Qt)
from PySide6.QtWidgets import (QPushButton, QVBoxLayout, QWidget)


class UploadFile(object):
    def setup_ui(self, upload_file):
        if not upload_file.objectName():
            upload_file.setObjectName(u"MainWindow")
        upload_file.resize(250, 66)
        self.centralwidget = QWidget(upload_file)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton, 0, Qt.AlignHCenter | Qt.AlignVCenter)

        upload_file.setCentralWidget(self.centralwidget)

        self.translate_ui(upload_file)

        QMetaObject.connectSlotsByName(upload_file)

    def translate_ui(self, upload_file):
        upload_file.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Upload file", None))
