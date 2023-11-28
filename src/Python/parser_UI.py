import json
import os

from PySide6.QtWidgets import QFileDialog, QApplication

from Layouts.tabsLayout import ResultTabs, updatePlainTextTabs
from utils import alertDialog, resetRadioButtonsMenus
from workerThread import WorkerThread

resultItems = []
foundItems = []


# reads files
def readFile(fileName):
    file = open(fileName, 'r', encoding="utf8")
    fileData = file.read()
    file.close()
    return json.dumps(fileData, indent=4, sort_keys=True, ensure_ascii=False)


# writes data into a give file
def write_file(path, data, file_name):
    with open(os.path.join(path, file_name), 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    f.close()


# Checks if the file exists and is valid
def validate_file(file_name):
    try:
        readFile(file_name)
        return True
    except Exception as e:
        print(
            '\nFile is invalid or not found. Error: {error} \n'.format(error=e))
        return False


# Gets all the keys in the file
def getAllKeys(jsonData):
    keys = set()

    def getKeys(data):
        if isinstance(data, dict):
            for key, value in data.items():
                keys.add(key)
                getKeys(value)
        elif isinstance(data, list):
            for item in data:
                getKeys(item)

    getKeys(jsonData)
    return list(keys)


# checks a json file for duplicates and creates a new output file without them
def parseDuplicates(window, jsonData, fields):
    checkedObjects = []

    def is_duplicate(json_data, target_field):
        if isinstance(json_data, dict):
            for key, value in json_data.items():
                if key == target_field:
                    item_object = {key: value}
                    if len(resultItems) == 0 or (
                            item_object not in checkedObjects and value):
                        if item not in resultItems:
                            resultItems.append(item)
                        checkedObjects.append(item_object)
                    elif value and item not in foundItems:
                        foundItems.append(item)
                elif isinstance(value, (dict, list)):
                    is_duplicate(value, target_field)
            if item not in foundItems and item not in resultItems:
                resultItems.append(item)
        elif isinstance(json_data, list):
            for list_item in json_data:
                is_duplicate(list_item, target_field)

    total_items = len(fields) * len(jsonData)
    overall_progress = 0
    window.parsingProgressLabel.setText("Parsing...")
    for field in fields:
        for i, item in enumerate(jsonData):
            is_duplicate(item, field)
            overall_progress += 1
            window.progressBar.setValue(int((overall_progress / total_items) * 100))


# Removes empty objects from the file based on empty fields
def parseEmpty(window, jsonData, fields):
    def is_empty(json_data, target_field):
        if isinstance(json_data, dict):
            for key, value in json_data.items():
                if key == target_field:
                    if value == "":
                        if item not in foundItems:
                            foundItems.append(item)
                    else:
                        if item not in resultItems:
                            resultItems.append(item)
                elif isinstance(value, (dict, list)):
                    is_empty(value, target_field)
            if item not in foundItems and item not in resultItems:
                resultItems.append(item)
        elif isinstance(json_data, list):
            for list_item in json_data:
                is_empty(list_item, target_field)

    total_items = len(fields) * len(jsonData)
    overall_progress = 0
    window.parsingProgressLabel.setText("Parsing...")
    for field in fields:
        for i, item in enumerate(jsonData):
            is_empty(item, field)
            overall_progress += 1
            window.progressBar.setValue(int((overall_progress / total_items) * 100))


def parseNull(window, jsonData, fields):
    def isNull(json_data, target_field):
        if isinstance(json_data, dict):
            for key, value in json_data.items():
                if key == target_field:
                    if value is None:
                        if item not in foundItems:
                            foundItems.append(item)
                    else:
                        if item not in resultItems:
                            resultItems.append(item)
                elif isinstance(value, (dict, list)):
                    isNull(value, target_field)
            if item not in foundItems and item not in resultItems:
                resultItems.append(item)
        elif isinstance(json_data, list):
            for list_item in json_data:
                isNull(list_item, target_field)

    total_items = len(fields) * len(jsonData)
    overall_progress = 0
    window.parsingProgressLabel.setText("Parsing...")
    for field in fields:
        for i, item in enumerate(jsonData):
            isNull(item, field)
            overall_progress += 1
            window.progressBar.setValue(int((overall_progress / total_items) * 100))


def resetResults():
    global resultItems
    resultItems = []
    global foundItems
    foundItems = []


def parse(window):
    resetResults()

    if window.fileData:
        window.startParseButton.setEnabled(False)
        jsonData = json.loads(window.fileData)
        if window.removeDuplicatesRadioButton.isChecked():
            window.workerThread = WorkerThread(
                lambda: parseDuplicates(window, jsonData, window.selectedFields))
            window.workerThread.finished.connect(
                lambda: setResultTabs(window, "Duplicates"))
            window.workerThread.start()
        elif window.removeEmptyRadioButton.isChecked():
            window.workerThread = WorkerThread(lambda: parseEmpty(
                window, jsonData, window.selectedFields))
            window.workerThread.finished.connect(
                lambda: setResultTabs(window, "Empty"))
            window.workerThread.start()
        elif window.removeNullRadioButton.isChecked():
            window.workerThread = WorkerThread(lambda: parseNull(
                window, jsonData, window.selectedFields))
            window.workerThread.finished.connect(
                lambda: setResultTabs(window, "Null"))
            window.workerThread.start()

        window.parsingProgressLabel.setVisible(True)


def setResultTabs(window, tabName):
    window.parsingProgressLabel.setText("Finishing up...")
    QApplication.processEvents()
    if not window.optionPositiveTab and not window.optionNegativeTab:
        ResultTabs(window, tabName, resultItems, foundItems)
    else:
        updatePlainTextTabs(window, tabName, resultItems, foundItems)
    window.saveFilesButton.setVisible(True)
    window.uploadNewButton.setVisible(True)
    window.startParseButton.setEnabled(False)
    resetRadioButtonsMenus(window)
    window.progressBar.setValue(100)
    window.parsingProgressLabel.setText("Done!")


def saveFiles(window):
    currentTabName = window.tabWidget.tabBar().tabText(1).lower()
    fileDialog = QFileDialog()
    path = fileDialog.getExistingDirectory(window, "Save files")
    if path:
        message = ""
        errorMessage = ""
        try:
            write_file(path, resultItems, 'result.json')
            write_file(path, foundItems, currentTabName + '.json')
            message = "Files saved successfully"
        except Exception as e:
            errorMessage = "Failed saving files"
            print('\n{errorMessage}. Error: {error} \n'.format(error=e, errorMessage=errorMessage))

        alertDialog(window, errorMessage, False) if errorMessage else alertDialog(window, message, True)
