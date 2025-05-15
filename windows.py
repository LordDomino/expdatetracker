from PyQt5.QtWidgets import QMainWindow

from config import WIN_HEIGHT, WIN_SCALE, WIN_WIDTH



class AppWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("ekSPYry")
        self.resize(int(WIN_WIDTH * WIN_SCALE), int(WIN_HEIGHT * WIN_SCALE))

