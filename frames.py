from typing import Dict, Sequence
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QFrame, QVBoxLayout, QHBoxLayout,
    QSizePolicy, QScrollArea
)

from db_utils import ProductDatabase
from widgets import Item, ItemExpiryLabel, ItemName, ItemRemainingDaysLabel, NavButton

import mainapp


#HELLO WORLD
# Hello Arghie

class InventoryScroll(QScrollArea):

    def __init__(self) -> None:
        super().__init__()
        self.setObjectName("inventory-scroll")
        self.items: Dict[int, ItemName] = {}

        # Container for content
        self.container = QFrame()

        self.vbox = QVBoxLayout()
        self.vbox.setContentsMargins(0, 0, 0, 0)
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