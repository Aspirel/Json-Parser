import sys

from PySide6.QtWidgets import (QApplication, QMainWindow)

from main import MainWindow
from utils import centerWindow


class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.upload_file = MainWindow()
        self.upload_file.setup_ui(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = App()
    window.setWindowTitle("Json Parser")
    # window.setWindowIcon(QtGui.QIcon("./icon.png"))
    centerWindow(window)
    window.show()
    sys.exit(app.exec())
