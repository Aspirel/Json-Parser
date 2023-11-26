from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QMainWindow, QGridLayout, QRadioButton, QSizePolicy, QSpacerItem,
                               QWidget, QProgressBar, QFileDialog, QListWidget, QLabel)

from Layouts.tabsLayout import TabLayout
from Layouts.uploadFileLayout import *
from parser_UI import *
from Layouts.fieldsSelectionLayout import FieldsSelection
from utils import *


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.workerThread = None
        self.saveFilesButton = None
        self.listViewLabel = None
        self.listView = None
        self.fieldsWindow = None
        self.progressBar = None
        self.window = None
        self.widget = None
        self.finished = None
        self.filePath = None
        self.startParseButton = None
        self.uploadNewButton = None
        self.fileLengthRadioButton = None
        self.removeDuplicatesRadioButton = None
        self.removeEmptyRadioButton = None
        self.removeNullRadioButton = None
        self.plainTextEdit = None
        self.plainTextEdit2 = None
        self.plainTextEdit3 = None
        self.originalFileTab = None
        self.optionNegativeTab = None
        self.optionPositiveTab = None
        self.gridLayout = None
        self.tabWidget = None
        self.tab1GridLayout = None
        self.tab2gridLayout = None
        self.tab3gridLayout = None
        self.fileData = None
        self.selectedFields = []

    def setup_ui(self, window):
        window.resize(1000, 600)
        centerWindow(window)
        self.window = window

        fontSize = QFont()
        fontSize.setBold(True)
        fontSize.setPointSize(10.5)

        centralwidget = QWidget(window)
        window.setCentralWidget(centralwidget)

        # Main grid
        self.gridLayout = QGridLayout(centralwidget)

        # Initial layout for the upload file button
        FileUploadLayout(self)

        # radio buttons vertical layout
        menuVerticalLayout = QVBoxLayout()

        self.fileLengthRadioButton = QRadioButton()
        self.fileLengthRadioButton.setFont(fontSize)
        self.fileLengthRadioButton.setText("Check file length")
        self.fileLengthRadioButton.setAutoExclusive(True)
        menuVerticalLayout.addWidget(self.fileLengthRadioButton)

        self.removeDuplicatesRadioButton = QRadioButton()
        self.removeDuplicatesRadioButton.setFont(fontSize)
        self.removeDuplicatesRadioButton.setText("Remove duplicates")
        self.removeDuplicatesRadioButton.setAutoExclusive(True)
        self.removeDuplicatesRadioButton.clicked.connect(self.fieldWindowSetup)
        menuVerticalLayout.addWidget(self.removeDuplicatesRadioButton)

        self.removeEmptyRadioButton = QRadioButton()
        self.removeEmptyRadioButton.setFont(fontSize)
        self.removeEmptyRadioButton.setText("Remove empty")
        self.removeEmptyRadioButton.setAutoExclusive(True)
        self.removeEmptyRadioButton.clicked.connect(self.fieldWindowSetup)
        menuVerticalLayout.addWidget(self.removeEmptyRadioButton)

        self.removeNullRadioButton = QRadioButton()
        self.removeNullRadioButton.setFont(fontSize)
        self.removeNullRadioButton.setText("Remove null")
        self.removeNullRadioButton.setAutoExclusive(True)
        self.removeNullRadioButton.clicked.connect(self.fieldWindowSetup)
        menuVerticalLayout.addWidget(self.removeNullRadioButton)

        # start parsing button
        self.startParseButton = QPushButton()
        self.startParseButton.setStyleSheet("QPushButton { "
                                            "max-width: 170;"
                                            "font-weight: bold;"
                                            "font-size: 12px }")
        self.startParseButton.setText("Start")
        self.startParseButton.clicked.connect(lambda: parse(self))
        menuVerticalLayout.addWidget(self.startParseButton)

        # Progress bar
        self.progressBar = QProgressBar()
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
        menuVerticalLayout.addWidget(self.progressBar)

        verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        menuVerticalLayout.addItem(verticalSpacer)

        # save files button
        self.saveFilesButton = QPushButton()
        self.saveFilesButton.setStyleSheet("QPushButton { "
                                           "max-width: 170;"
                                           "font-weight: bold;"
                                           "font-size: 12px }")
        self.saveFilesButton.setText("Save files")
        self.saveFilesButton.clicked.connect(lambda: self.saveFiles())
        self.saveFilesButton.setVisible(False)
        menuVerticalLayout.addWidget(self.saveFilesButton)

        # upload new file button
        self.uploadNewButton = QPushButton()
        self.uploadNewButton.setStyleSheet("QPushButton { "
                                           "max-width: 170;"
                                           "font-weight: bold;"
                                           "font-size: 12px }")
        self.uploadNewButton.setText("Upload new file")
        self.uploadNewButton.clicked.connect(lambda: self.uploadNewFile())
        self.uploadNewButton.setVisible(False)
        menuVerticalLayout.addWidget(self.uploadNewButton)

        self.listViewLabel = QLabel()
        self.listViewLabel.setFont(fontSize)
        self.listViewLabel.setText("Selected fields")
        self.listViewLabel.setVisible(False)
        menuVerticalLayout.addWidget(self.listViewLabel)
        self.listView = QListWidget()
        self.listView.setStyleSheet(
            "QListWidget { max-width: 170; max-height: 150}")
        font = self.listView.font()
        font.setPointSize(10.5)
        self.listView.setFont(font)
        self.listView.setSpacing(3)
        self.listView.setVisible(False)
        menuVerticalLayout.addWidget(self.listView)

        self.gridLayout.addLayout(menuVerticalLayout, 0, 0, 1, 1)

    def setupFile(self):
        file_dialog = QFileDialog()
        selected_file = file_dialog.getOpenFileName(None, "Select file")

        if isinstance(selected_file, tuple) and selected_file[0]:
            if validate_file(selected_file[0]):
                fileData = readFile(selected_file[0])
                self.fileData = json.loads(fileData)
                TabLayout(self)
                self.plainTextEdit.setPlainText(self.fileData)

    def fieldWindowSetup(self):
        if self.fileData:
            radioButtons = getAllKeys(json.loads(self.fileData))
            self.fieldsWindow = FieldsSelection(self, radioButtons)
            self.fieldsWindow.show()

    def uploadNewFile(self):
        resetMenus(self)
        self.setupFile()

    def saveFiles(self):
        print("saving")
