from PySide6.QtCore import QThread, Signal


class WorkerThread(QThread):
    finished = Signal()

    def __init__(self, parse_method):
        super().__init__()
        self.parse_method = parse_method

    def run(self):
        # Call the provided parse method in the threaded context
        self.parse_method()

        # Emit the finished signal when the long operation is completed
        self.finished.emit()
