from PySide6.QtGui import QScreen
from PySide6.QtWidgets import QApplication


def centerWindow(window):
    center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
    geo = window.frameGeometry()
    geo.moveCenter(center)
    window.move(geo.topLeft())


def enableMenus(window):
    window.startParseButton.setEnabled(True)
    window.fileLengthRadioButton.setEnabled(True)
    window.removeEmptyRadioButton.setEnabled(True)
    window.removeNullRadioButton.setEnabled(True)
    window.removeDuplicatesRadioButton.setEnabled(True)


def resetMenus(window):
    window.startParseButton.setEnabled(True)
    window.fileLengthRadioButton.setAutoExclusive(False)
    window.fileLengthRadioButton.setChecked(False)
    window.fileLengthRadioButton.setAutoExclusive(True)

    window.removeEmptyRadioButton.setAutoExclusive(False)
    window.removeEmptyRadioButton.setChecked(False)
    window.removeEmptyRadioButton.setAutoExclusive(True)

    window.removeNullRadioButton.setAutoExclusive(False)
    window.removeNullRadioButton.setChecked(False)
    window.removeNullRadioButton.setAutoExclusive(True)

    window.removeDuplicatesRadioButton.setAutoExclusive(False)
    window.removeDuplicatesRadioButton.setChecked(False)
    window.removeDuplicatesRadioButton.setAutoExclusive(True)
    window.progressBar.setValue(0)
    window.tabWidget.removeTab(1)
    window.tabWidget.removeTab(1)
