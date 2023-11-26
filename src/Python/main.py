from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QMainWindow, QGridLayout, QRadioButton, QSizePolicy, QSpacerItem,
                               QWidget, QProgressBar, QFileDialog, QListWidget, QLabel)

from Layouts.tabsLayout import TabLayout
from Layouts.uploadFileLayout import *
from parser_UI import *
from utils import *
from src.Python.Layouts.fieldsSelectionLayout import FieldsSelection


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.listViewLabel = None
        self.listView = None
        self.fieldsWindow = None
        self.progressBar = None
        self.window = None
        self.widget = None
        self.a = None
        self.finished = None
        self.helper = None
        self.filePath = None
        self.verticalSpacer = None
        self.pushButton = None
        self.fileLengthRadioButton = None
        self.removeDuplicatesRadioButton = None
        self.removeEmptyRadioButton = None
        self.removeNullRadioButton = None
        self.menuVerticalLayout = None
        self.plainTextEdit = None
        self.plainTextEdit2 = None
        self.plainTextEdit3 = None
        self.gridLayout_4 = None
        self.gridLayout_5 = None
        self.originalFileTab = None
        self.optionNegativeTab = None
        self.optionPositiveTab = None
        self.gridLayout_3 = None
        self.tabWidget = None
        self.gridLayout = None
        self.gridLayout_2 = None
        self.centralwidget = None
        self.fileData = None
        self.option = None
        self.selectedFields = []

    def setup_ui(self, window):
        if not window.objectName():
            window.setObjectName(u"JSONParser")
        window.resize(1000, 600)
        centerWindow(window)
        self.window = window

        fontSize = QFont()
        fontSize.setBold(True)
        fontSize.setPointSize(10.5)

        self.centralwidget = QWidget(window)
        self.centralwidget.setObjectName(u"centralwidget")
        window.setCentralWidget(self.centralwidget)

        # Main grid
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")

        # Inner grid
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")

        # Initial layout for the upload file button
        FileUploadLayout(self)

        # radio buttons vertical layout
        self.menuVerticalLayout = QVBoxLayout()
        self.menuVerticalLayout.setObjectName(u"verticalLayout_2")

        self.fileLengthRadioButton = QRadioButton(self.centralwidget)
        self.fileLengthRadioButton.setObjectName(u"radioButton_5")
        self.fileLengthRadioButton.setFont(fontSize)
        self.fileLengthRadioButton.setText("Check file length")
        self.fileLengthRadioButton.setAutoExclusive(True)
        self.menuVerticalLayout.addWidget(self.fileLengthRadioButton)

        self.removeDuplicatesRadioButton = QRadioButton(self.centralwidget)
        self.removeDuplicatesRadioButton.setObjectName(u"radioButton_6")
        self.removeDuplicatesRadioButton.setFont(fontSize)
        self.removeDuplicatesRadioButton.setText("Remove duplicates")
        self.removeDuplicatesRadioButton.setAutoExclusive(True)
        self.removeDuplicatesRadioButton.clicked.connect(self.fieldWindowSetup)
        self.menuVerticalLayout.addWidget(self.removeDuplicatesRadioButton)

        self.removeEmptyRadioButton = QRadioButton(self.centralwidget)
        self.removeEmptyRadioButton.setObjectName(u"radioButton_7")
        self.removeEmptyRadioButton.setFont(fontSize)
        self.removeEmptyRadioButton.setText("Remove empty")
        self.removeEmptyRadioButton.setAutoExclusive(True)
        self.removeEmptyRadioButton.clicked.connect(self.fieldWindowSetup)
        self.menuVerticalLayout.addWidget(self.removeEmptyRadioButton)

        self.removeNullRadioButton = QRadioButton(self.centralwidget)
        self.removeNullRadioButton.setObjectName(u"radioButton_8")
        self.removeNullRadioButton.setFont(fontSize)
        self.removeNullRadioButton.setText("Remove null")
        self.removeNullRadioButton.setAutoExclusive(True)
        self.removeNullRadioButton.clicked.connect(self.fieldWindowSetup)
        self.menuVerticalLayout.addWidget(self.removeNullRadioButton)

        # start parsing button
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet("QPushButton { "
                                      "max-width: 170;"
                                      "font-weight: bold;"
                                      "font-size: 12px }")
        self.pushButton.setText("Start ")
        self.pushButton.clicked.connect(self.parse)
        self.menuVerticalLayout.addWidget(self.pushButton)

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
        self.menuVerticalLayout.addWidget(self.progressBar)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.menuVerticalLayout.addItem(self.verticalSpacer)
        self.gridLayout.addLayout(self.menuVerticalLayout, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.listViewLabel = QLabel(self.centralwidget)
        self.listViewLabel.setFont(fontSize)
        self.listViewLabel.setText("Selected fields")
        self.listViewLabel.setVisible(False)
        self.menuVerticalLayout.addWidget(self.listViewLabel)
        self.listView = QListWidget(self.centralwidget)
        self.listView.setStyleSheet("QListWidget { max-width: 170;}")
        font = self.listView.font()
        font.setPointSize(10.5)
        self.listView.setFont(font)
        self.listView.setSpacing(3)
        self.listView.setVisible(False)
        self.menuVerticalLayout.addWidget(self.listView)

    def setupFile(self):
        file_dialog = QFileDialog()
        selected_file = file_dialog.getOpenFileName(None, "Select file")

        if isinstance(selected_file, tuple) and selected_file[0]:
            if validate_file(selected_file[0]):
                fileData = readFile(selected_file[0])
                self.fileData = json.loads(fileData)
                TabLayout(self)
                self.plainTextEdit.setPlainText(self.fileData)

    def parse(self):
        parse(self)

    def fieldWindowSetup(self):
        if self.fileData:
            radioButtons = getAllKeys(json.loads(self.fileData))
            self.fieldsWindow = FieldsSelection(self, radioButtons)
            self.fieldsWindow.show()
