# workerThread.py
from PySide6.QtCore import QThread, Signal


class WorkerThread(QThread):
    finished = Signal()

    def __init__(self, fn):
        super().__init__()
        self.fn = fn
        self.result = None

    def run(self):
        self.result = self.fn()
        self.finished.emit()
