# parser_controller.py
import json
from PySide6.QtWidgets import QApplication, QFileDialog

from json_parser import (
    parse_duplicates,
    parse_empty,
    parse_null,
    write_json_file,
    get_all_keys,
    read_json_file
)

from workerThread import WorkerThread
from Layouts.tabsLayout import ResultTabs, updatePlainTextTabs
from utils import alertDialog, resetRadioButtonsMenus, enableDisableRadioButtonsMenus


def validate_file(path: str) -> bool:
    try:
        read_json_file(path)
        return True
    except Exception as e:
        print("Invalid JSON:", e)
        return False


def load_file(path: str):
    """Return parsed JSON."""
    return read_json_file(path)


def parse(window):
    if not window.fileData:
        return

    enableDisableRadioButtonsMenus(window, False)
    window.startParseButton.setEnabled(False)
    window.saveFilesButton.setVisible(False)
    window.uploadNewButton.setVisible(False)
    window.parsingProgressLabel.setVisible(True)
    window.parsingProgressLabel.setText("Parsing...")

    json_data = window.fileData

    def update_progress(p):
        window.progressBar.setValue(p)
        QApplication.processEvents()

    if window.removeDuplicatesRadioButton.isChecked():
        fn = lambda: parse_duplicates(json_data, window.selectedFields, update_progress)
        tab_name = "Duplicates"

    elif window.removeEmptyRadioButton.isChecked():
        fn = lambda: parse_empty(json_data, window.selectedFields, update_progress)
        tab_name = "Empty"

    elif window.removeNullRadioButton.isChecked():
        fn = lambda: parse_null(json_data, window.selectedFields, update_progress)
        tab_name = "Null"

    else:
        return

    window.workerThread = WorkerThread(fn)
    window.workerThread.finished.connect(lambda: setResultTabs(window, tab_name))
    window.workerThread.start()


def setResultTabs(window, tabName):
    window.parsingProgressLabel.setText("Finishing up...")
    QApplication.processEvents()

    result_items, found_items = window.workerThread.result

    if not window.optionPositiveTab and not window.optionNegativeTab:
        ResultTabs(window, tabName, result_items, found_items)
    else:
        updatePlainTextTabs(window, tabName, result_items, found_items)

    window.lastResultItems = result_items
    window.lastFoundItems = found_items

    window.saveFilesButton.setVisible(True)
    window.uploadNewButton.setVisible(True)
    resetRadioButtonsMenus(window)
    window.progressBar.setValue(100)
    window.parsingProgressLabel.setText("Done!")


def saveFiles(window):
    currentTabName = window.tabWidget.tabBar().tabText(1).lower()
    path = QFileDialog().getExistingDirectory(window, "Save files")

    if not path:
        return

    try:
        write_json_file(f"{path}/result.json", window.lastResultItems)
        write_json_file(f"{path}/{currentTabName}.json", window.lastFoundItems)
        alertDialog(window, "Files saved successfully", True)
    except Exception as e:
        print("Error saving files:", e)
        alertDialog(window, "Failed saving files", False)
