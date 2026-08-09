import logging

from PySide6.QtWidgets import (
    QMainWindow,
    QLabel,
)

logger = logging.getLogger(__name__)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        logger.info("Main window initialized")

        self.setWindowTitle("Video Transcriber")
        self.resize(800, 600)

        self.label = QLabel("Video Transcriber")
        self.setCentralWidget(self.label)