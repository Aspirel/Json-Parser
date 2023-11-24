import sys
from PySide6.QtWidgets import (QApplication, QMainWindow)
from PySide6 import QtGui
from UI.Python.upload_file import UploadFile


class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.upload_file = UploadFile()
        self.upload_file.setup_ui(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = App()
    window.setWindowTitle("Json Parser")
    # window.setWindowIcon(QtGui.QIcon("./icon.png"))
    window.show()
    sys.exit(app.exec())
