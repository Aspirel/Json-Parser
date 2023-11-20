import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from src.UI.Python.upload_file import UploadFile


class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.ui = UploadFile()
        self.ui.setup_ui(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = App()
    window.show()

    sys.exit(app.exec())