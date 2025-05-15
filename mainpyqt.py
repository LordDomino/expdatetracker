import sys
from typing import List
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow
)



class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()


def main():
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()