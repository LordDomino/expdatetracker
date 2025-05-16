import sys
from PyQt5.QtWidgets import QApplication
from typing import List

from db_utils import ProductDatabase
from frames import EnterScreen, HomeScreen
from windows import AppWindow



class Application(QApplication):

    def __init__(self, db: str, argv: List[str] = []) -> None:
        super().__init__(argv)
        self.app_window = AppWindow()
        self.database = ProductDatabase(db)
        self.enter_screen = EnterScreen()
        self.home_screen = HomeScreen()


    def get_database(self) -> ProductDatabase:
        return self.database



APP = Application("items.txt")


def get_stylesheet(filepath: str):
    with open(filepath, "r") as f:
        _style = f.read()
        return _style


def main():  
    # Fonts setup
    from PyQt5.QtGui import QFontDatabase 
    QFontDatabase.addApplicationFont("fonts/Montserrat-Bold.ttf")
    QFontDatabase.addApplicationFont("fonts/nunito-sans.regular.ttf")

    global APP
    APP.home_screen.inv_scroll.draw_items(APP.database)

    APP.app_window.setCentralWidget(APP.enter_screen)

    # Show the main window then configure app to exit only when main window is closed
    APP.app_window.show()
    APP.setStyleSheet(get_stylesheet("styles.qss"))
    sys.exit(APP.exec_())
