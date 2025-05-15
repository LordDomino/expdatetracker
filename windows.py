from typing import Dict, Sequence, override
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QMainWindow, QFrame, QVBoxLayout, QHBoxLayout, QPushButton,
    QSizePolicy, QScrollArea
)

from config import WIN_HEIGHT, WIN_SCALE, WIN_WIDTH



class AppWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Expiration Date Tracker")
        self.resize(int(WIN_WIDTH * WIN_SCALE), int(WIN_HEIGHT * WIN_SCALE))
