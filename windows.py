from typing import Dict, Sequence, override
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QMainWindow, QDialog, QVBoxLayout, QLabel, QPushButton
)

from config import WIN_HEIGHT, WIN_SCALE, WIN_WIDTH



class AppWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Expiration Date Tracker")
        self.resize(int(WIN_WIDTH * WIN_SCALE), int(WIN_HEIGHT * WIN_SCALE))



class PopupDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Popup Window")
        layout = QVBoxLayout()
        self.label = QLabel("This is a pop-up!")
        layout.addWidget(self.label)
        self.button = QPushButton("Close")
        self.button.clicked.connect(self.accept) # Close dialog
        layout.addWidget(self.button)
        self.setLayout(layout)