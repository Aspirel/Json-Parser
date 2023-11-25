from PySide6.QtCore import Qt
from PySide6.QtWidgets import QVBoxLayout, QPushButton


def FileUploadLayout(window):
    verticalLayout = QVBoxLayout(window.centralwidget)
    verticalLayout.setObjectName(u"verticalLayout")

    # Button
    pushButton = QPushButton(window.centralwidget)
    pushButton.setObjectName(u"pushButton")
    pushButton.setStyleSheet("QPushButton {"
                             "color: white; "
                             "font-weight: bold;"
                             "font-size: 15px;"
                             "width: 250px; "
                             "height: 50px}")
    pushButton.clicked.connect(window.setupFile)
    pushButton.setText("Upload file")
    verticalLayout.addWidget(pushButton, 0, Qt.AlignHCenter | Qt.AlignVCenter)
    window.gridLayout.addLayout(verticalLayout, 0, 1, 1, 1)
