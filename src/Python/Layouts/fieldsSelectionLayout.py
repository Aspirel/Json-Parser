from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QFormLayout, QWidget, QRadioButton, QVBoxLayout, QPushButton, QListWidgetItem

from src.Python.utils import centerWindow, enableParsingMenus


class FieldsSelection(QWidget):

    def __init__(self, window, radioButtons):
        super(FieldsSelection, self).__init__()
        self.window = window
        self.radioButtonsList = []
        self.initUI(radioButtons)

    def initUI(self, radioButtons):
        mainLayout = QVBoxLayout(self)
        centerLayout = QVBoxLayout()
        centerLayout.setAlignment(Qt.AlignCenter)
        formLayout = QFormLayout()
        formLayout.setAlignment(Qt.AlignCenter)

        fontSize = QFont()
        fontSize.setBold(True)
        fontSize.setPointSize(10)

        centerLayout.addLayout(formLayout)
        mainLayout.addLayout(centerLayout)
        self.setWindowTitle('Fields')
        self.setGeometry(100, 100, 300, 100)
        centerWindow(self)

        # Add radio buttons to the form layout in pairs
        for i in range(0, len(radioButtons), 2):
            radioButton1 = QRadioButton(radioButtons[i])
            radioButton1.setFont(fontSize)
            radioButton1.setAutoExclusive(False)

            radioButton2 = None
            if i + 1 < len(radioButtons):
                radioButton2 = QRadioButton(radioButtons[i + 1])
                radioButton2.setFont(fontSize)
                radioButton2.setAutoExclusive(False)
                formLayout.addRow(radioButton1, radioButton2)
            else:
                formLayout.addRow(radioButton1, None)
            self.radioButtonsList.append(radioButton1)
            if radioButton2:
                self.radioButtonsList.append(radioButton2)

        pushButton = QPushButton(self)
        pushButton.setText("Apply")
        pushButton.clicked.connect(self.applySelections)
        centerLayout.addWidget(pushButton)

    def applySelections(self):
        self.window.selectedFields = []
        self.window.listView.clear()
        self.window.progressBar.setValue(0)
        for r in self.radioButtonsList:
            if r.isChecked():
                self.window.selectedFields.append(r.text())
                listItem = QListWidgetItem(r.text())
                self.window.listView.addItem(listItem)

        self.close()
        enableParsingMenus(self.window)
