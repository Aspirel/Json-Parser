from PySide6.QtGui import QScreen
from PySide6.QtWidgets import QApplication


def centerWindow(window):
    center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
    geo = window.frameGeometry()
    geo.moveCenter(center)
    window.move(geo.topLeft())
