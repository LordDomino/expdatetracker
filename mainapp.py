import sys
from typing import List
from PyQt5.QtWidgets import (
    QApplication,
)

from db_utils import ProductDatabase




def get_stylesheet(filepath: str):
    with open(filepath, "r") as f:
        _style = f.read()
        return _style



class Application(QApplication):

    def __init__(self, db: str, argv: List[str] = []) -> None:
        super().__init__(argv)
        self.database = ProductDatabase(db)

    def get_database(self) -> ProductDatabase:
        return self.database



APP = Application("products_ko.txt")



def main():
    from windows import AppWindow
    app_window = AppWindow()
    from PyQt5.QtGui import QFontDatabase 
    QFontDatabase.addApplicationFont("fonts/Montserrat-Bold.ttf")
    QFontDatabase.addApplicationFont("fonts/nunito-sans.regular.ttf")
    from frames import HomeScreen
    init_screen = HomeScreen()
    app_window.setCentralWidget(init_screen)

    # Show the main window then configure app to exit only when main window is closed
    app_window.show()
    APP.setStyleSheet(get_stylesheet("styles.qss"))
    sys.exit(APP.exec_())


if __name__ == "__main__":
    main()

