from typing import Dict, Sequence, override
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QFrame, QVBoxLayout, QHBoxLayout,
    QSizePolicy, QScrollArea
)

from db_utils import ProductDatabase
from widgets import AddNewButton, Item, ItemExpiryLabel, ItemName, ItemRemainingDaysLabel, NavButton

import mainapp


#HELLO WORLD
# Hello Arghie

class InventoryScroll(QScrollArea):

    def __init__(self) -> None:
        super().__init__()
        self.setObjectName("inventory-scroll")
        self.items: Dict[int, ItemName] = {}

        self.setStyleSheet("""
            QScrollArea#inventory-scroll {
                background-color: #004643
            }
        """)

        # Container for content
        self.container = QFrame()

        

        self.vbox = QVBoxLayout()
        self.vbox.setContentsMargins(10, 10, 10, 10)
        self.vbox.setSpacing(10)
        self.container.setLayout(self.vbox)
        self.container.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)

        self.setWidget(self.container)
        self.setWidgetResizable(True)

        # Generates the different items
        self.draw_items(mainapp.APP.get_database())

    def draw_items(self, db: ProductDatabase) -> None:
        for product in db.products:
            item = Item(product.name, product.expiration_date, product.get_remaining_days())
            self.items[product.id] = item

            self.vbox.addWidget(item)

            



class NavBar(QFrame):

    def __init__(self, buttons: Sequence[NavButton]) -> None:
        super().__init__()
        self.setObjectName("nav-bar")
        self.buttons = buttons

        self.setStyleSheet("""
            QFrame#nav-bar  {
                border-top: 1px solid black;
                background-color: #abd1c6;
        }""")

        # Setup layout for NavBar
        self.hbox = QHBoxLayout()
        self.hbox.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.hbox)
        self.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)

       

        # Add the different buttons to the navigation bar
        for button in self.buttons:
            self.hbox.addWidget(button)    



class HomeScreen(QFrame):

    def __init__(self) -> None:
        super().__init__()
        
        self.vbox = QVBoxLayout()
        self.vbox.setContentsMargins(0, 0, 0, 0)
        self.vbox.setSpacing(0)
        self.setLayout(self.vbox)

        self.navbar = NavBar([NavButton("Inventory"), NavButton("Tips"), NavButton("Settings")])
        self.vbox.addWidget(InventoryScroll())
        self.vbox.addWidget(self.navbar)
        self.setObjectName("home-screen")

        self.setStyleSheet("""
            QFrame#home-screen    {
                Font-family: 'Montserrat';
                Font-size: 20px;
        }""")

        self.setStyleSheet("""
            QFrame#home-screen:hover {
                font-weight: bold;
                background-color: red;
        }""")
        # Add button
        self.add_new_button = AddNewButton()
        self.add_new_button.resize(60, 60)
        self.add_new_button.setParent(self)
        self._position_fab()

        

    @override
    def resizeEvent(self, event) -> None: # type: ignore
        super().resizeEvent(event)
        self._position_fab()

    def _position_fab(self) -> None:
        margin = 20  # distance from bottom-right corner
        btn_w = self.add_new_button.width()
        btn_h = self.add_new_button.height()
        x = self.width() - btn_w - margin
        y = self.height() - btn_h - margin - self.navbar.height()
        self.add_new_button.move(x, y)