from PyQt5.QtWidgets import QApplication
from typing import List

from db_utils import ProductDatabase
from frames import HomeScreen


class Application(QApplication):

    def __init__(self, db: str, argv: List[str] = []) -> None:
        super().__init__(argv)
        self.database = ProductDatabase(db)
        self.init_screen = HomeScreen()

    def get_database(self) -> ProductDatabase:
        return self.database
    

import sys
from app import Application


APP = Application("products_ko.txt")


def get_stylesheet(filepath: str):
    with open(filepath, "r") as f:
        _style = f.read()
        return _style


def main():
    from windows import AppWindow
    app_window = AppWindow()
    
    # Fonts setup
    from PyQt5.QtGui import QFontDatabase 
    QFontDatabase.addApplicationFont("fonts/Montserrat-Bold.ttf")
    QFontDatabase.addApplicationFont("fonts/nunito-sans.regular.ttf")

    global APP
    print(APP)
    APP.init_screen.inv_scroll.draw_items(APP.database)

    app_window.setCentralWidget(APP.init_screen)

    # Show the main window then configure app to exit only when main window is closed
    app_window.show()
    APP.setStyleSheet(get_stylesheet("styles.qss"))
    sys.exit(APP.exec_())
    print("Test")


