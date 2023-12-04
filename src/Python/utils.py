from PySide6.QtGui import QScreen
from PySide6.QtWidgets import QApplication, QMessageBox


def centerWindow(window):
    center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
    geo = window.frameGeometry()
    geo.moveCenter(center)
    window.move(geo.topLeft())


def enableDisableRadioButtonsMenus(window, enable):
    window.removeEmptyRadioButton.setEnabled(enable)
    window.removeNullRadioButton.setEnabled(enable)
    window.removeDuplicatesRadioButton.setEnabled(enable)


def resetRadioButtonsMenus(window):
    window.removeEmptyRadioButton.setAutoExclusive(False)
    window.removeEmptyRadioButton.setChecked(False)
    window.removeEmptyRadioButton.setAutoExclusive(True)

    window.removeNullRadioButton.setAutoExclusive(False)
    window.removeNullRadioButton.setChecked(False)
    window.removeNullRadioButton.setAutoExclusive(True)

    window.removeDuplicatesRadioButton.setAutoExclusive(False)
    window.removeDuplicatesRadioButton.setChecked(False)
    window.removeDuplicatesRadioButton.setAutoExclusive(True)
    enableDisableRadioButtonsMenus(window, True)

def enableParsingMenus(window):
    window.listViewLabel.setVisible(True)
    window.listView.setVisible(True)
    window.startParseButton.setEnabled(True)
    window.parsingProgressLabel.clear()


def resetMenus(window):
    window.startParseButton.setEnabled(False)

    resetRadioButtonsMenus(window)

    window.progressBar.setValue(0)
    window.optionPositiveTab = None
    window.optionNegativeTab = None
    window.tabWidget.removeTab(1)
    window.tabWidget.removeTab(1)
    window.listView.clear()
    window.saveFilesButton.setVisible(False)
    window.parsingProgressLabel.clear()


def alertDialog(window, message, success):
    dialogMessage = QMessageBox(window)
    dialogMessage.setWindowTitle("Saving files")
    dialogMessage.setIcon(QMessageBox.Information if success else QMessageBox.Critical)
    dialogMessage.setText(message)
    dialogMessage.setStyleSheet("QMessageBox {font: bold 12pt Segoe UI;}")
    dialogMessage.exec_()
