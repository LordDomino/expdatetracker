from typing import Dict, Sequence, override
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QMainWindow, QDialog, QGridLayout, QLabel, QPushButton
)

from config import WIN_HEIGHT, WIN_SCALE, WIN_WIDTH
from widgets import Field, FieldLabel, Heading1



class AppWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Expiration Date Tracker")
        self.resize(int(WIN_WIDTH * WIN_SCALE), int(WIN_HEIGHT * WIN_SCALE))

