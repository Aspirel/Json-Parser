import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from main_window import MainWindow
from upload_file import UploadFile
from parsing_progress import ParsingProgress

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