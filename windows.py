from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon, QPixmap

from config import WIN_HEIGHT, WIN_SCALE, WIN_WIDTH



class AppWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("ekSPYry")
        self.resize(int(WIN_WIDTH * WIN_SCALE), int(WIN_HEIGHT * WIN_SCALE))

        self.setWindowIcon(QIcon(QPixmap("resources\\icon.png")))

    def switch_to_home(self) -> None:
        import notify
        from app import APP        
        self.setCentralWidget(APP.home_screen)
