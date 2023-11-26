import json
import os
import sys

from Layouts.tabsLayout import ResultTabs
from workerThread import WorkerThread


# reads files
def readFile(fileName):
    file = open(fileName, 'r', encoding="utf8")
    fileData = file.read()
    file.close()
    return json.dumps(fileData, indent=4, sort_keys=True)


# writes data into a give file
def write_file(data, file_name):
    application_path = get_os_file_path()
    with open(os.path.join(application_path, file_name), 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    f.close()


# method that takes json files and returns their lengths
def filesLength(file):
    return len(file)


# gets the current location of the program in the os
def get_os_file_path():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    elif __file__:
        return os.path.dirname(__file__)


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
    result_items = []
    duplicates = []
    checked_objects = []

    def is_duplicate(json_data, target_field):
        if isinstance(json_data, dict):
            for key, value in json_data.items():
                if key == target_field:
                    item_object = {key: value}
                    if len(result_items) == 0 or (
                            item_object not in checked_objects and value):
                        if item not in result_items:
                            result_items.append(item)
                        checked_objects.append(item_object)
                    # TODO when a UI is made, include option to include empty/null values
                    elif value and item not in duplicates:
                        duplicates.append(item)
                elif isinstance(value, (dict, list)):
                    is_duplicate(value, target_field)
            if item not in duplicates and item not in result_items:
                result_items.append(item)
        elif isinstance(json_data, list):
            for list_item in json_data:
                is_duplicate(list_item, target_field)

    for i, item in enumerate(jsonData):
        if isinstance(fields, str):
            is_duplicate(item, fields)
        else:
            for field in fields:
                is_duplicate(item, field)
        window.progressBar.setValue(int((i / len(jsonData)) * 100))
    window.progressBar.setValue(100)
    write_file(result_items, 'no_duplicates.json')
    write_file(duplicates, 'duplicates.json')


# Removes empty objects from the file based on empty fields
def parseEmpty(window, jsonData, fields):
    result_items = []
    empty_items = []

    def is_empty(json_data, target_field):
        if isinstance(json_data, dict):
            for key, value in json_data.items():
                if key == target_field:
                    if value.strip() == "":
                        if item not in empty_items:
                            empty_items.append(item)
                    else:
                        if item not in result_items:
                            result_items.append(item)
                elif isinstance(value, (dict, list)):
                    is_empty(value, target_field)
            if item not in empty_items and item not in result_items:
                result_items.append(item)
        elif isinstance(json_data, list):
            for list_item in json_data:
                is_empty(list_item, target_field)

    for i, item in enumerate(jsonData):
        if isinstance(fields, str):
            is_empty(item, fields)
        else:
            for field in fields:
                is_empty(item, field)
        window.progressBar.setValue(int((i / len(jsonData)) * 100))
    window.progressBar.setValue(100)

    write_file(result_items, 'no_empty.json')
    write_file(empty_items, 'empty.json')


def parseNull(window, jsonData, fields):
    result_items = []
    empty_items = []

    def isNull(json_data, target_field):
        if isinstance(json_data, dict):
            for key, value in json_data.items():
                if key == target_field:
                    if value is None:
                        if item not in empty_items:
                            empty_items.append(item)
                    else:
                        if item not in result_items:
                            result_items.append(item)
                elif isinstance(value, (dict, list)):
                    isNull(value, target_field)
            if item not in empty_items and item not in result_items:
                result_items.append(item)
        elif isinstance(json_data, list):
            for list_item in json_data:
                isNull(list_item, target_field)

    for i, item in enumerate(jsonData):
        if isinstance(fields, str):
            isNull(item, fields)
        else:
            for field in fields:
                isNull(item, field)
        window.progressBar.setValue(int((i / len(jsonData)) * 100))
    window.progressBar.setValue(100)

    write_file(result_items, 'no_null.json')
    write_file(empty_items, 'null.json')


def parse(window):
    if window.fileData:
        jsonData = json.loads(window.fileData)
        if window.fileLengthRadioButton.isChecked():
            print(filesLength(jsonData))
        elif window.removeDuplicatesRadioButton.isChecked():
            workerThread = WorkerThread(lambda: parseDuplicates(window, jsonData, window.selectedFields))
            workerThread.finished.connect(lambda: setResultTabs(window, "Duplicates", "No duplicates"))
            workerThread.start()
        elif window.removeEmptyRadioButton.isChecked():
            workerThread = WorkerThread(lambda: parseEmpty(window, jsonData, window.selectedFields))
            workerThread.finished.connect(lambda: setResultTabs(window, "Empty", "No empty"))
            workerThread.start()
        elif window.removeNullRadioButton.isChecked():
            workerThread = WorkerThread(lambda: parseNull(window, jsonData, window.selectedFields))
            workerThread.finished.connect(lambda: setResultTabs(window, "Null", "No null"))
            workerThread.start()


def setResultTabs(window, tab1, tab2):
    if not window.optionPositiveTab and not window.optionNegativeTab:
        ResultTabs(window, tab1, tab2)
