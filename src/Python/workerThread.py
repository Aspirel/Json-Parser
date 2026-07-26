class WorkerThread(QThread):
    finished = Signal()

    def __init__(self, task):
        super().__init__()
        self.task = task
        self.result = None

    def run(self):
        self.result = self.task()
        self.finished.emit()
