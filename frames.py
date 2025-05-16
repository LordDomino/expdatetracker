from typing import Dict, Sequence, override
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QFrame, QVBoxLayout, QHBoxLayout,
    QSizePolicy, QScrollArea, QLabel, QPushButton
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSignal

from db_utils import ProductDatabase
from widgets import AddNewButton, Heading1, Item, ItemName, NavButton



class InventoryHeader(QFrame):
    
    def __init__(self) -> None:
        super().__init__()
        self.setObjectName("inventory-header")

        self.setStyleSheet("""
            QFrame#inventory-header {
                padding: 0px 10px;
                background-color: #e16162;
                border-bottom-left-radius: 20px;
                border-bottom-right-radius: 20px; 
            }
        """)

        self.vbox = QVBoxLayout()
        self.setLayout(self.vbox)

        self.header = Heading1("Inventory")

        self.vbox.addWidget(self.header)



class InventoryScroll(QScrollArea):

    def __init__(self) -> None:
        super().__init__()
        self.setObjectName("inventory-scroll")
        # self.items: Dict[int, ItemName] = {}

        self.setStyleSheet("""
            QScrollArea#inventory-scroll {
                background-color: #004643;
                border: none
            }
        """)

        # Container for content
        self.container = QFrame()
        self.container.setObjectName("inv-container")
        self.container.setStyleSheet("""
            QFrame#inv-container {
                margin: 10px;
                background-color: #F5F5DC;
                border-radius: 15px;
            }
        """)
        
        self.vbox = QVBoxLayout()
        self.vbox.setContentsMargins(10, 10, 10, 10)
        self.vbox.setSpacing(10)
        self.container.setLayout(self.vbox)
        self.container.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)

        self.setWidget(self.container)
        self.setWidgetResizable(True)

    def draw_items(self, db: ProductDatabase) -> None:
        if len(db.products) == 0:
            label = QLabel()
            label.setObjectName("no-items-label")
            label.setStyleSheet("""
                QLabel#no-items-label {
                    font-size: 16px;
                    font-family: 'Montserrat';            
                }
            """)
            self.vbox.addWidget(label)
            return
        
        for product in db.products:
            item = Item(product.id, product.name, product.exp_date, product.get_remaining_days(), product.note)
            # self.items[product.id] = item

            self.vbox.addWidget(item)

    def clear_items(self) -> None:
        print(self)
        for i in reversed(range(self.vbox.count())): 
            # self.vbox.itemAt(i).widget().setParent(None)
            self.vbox.itemAt(i).widget().deleteLater() # type: ignore
            self.vbox.itemAt(i).widget().setParent(None) # type: ignore

    def redraw_items(self) -> None:
        from app import APP
        self.clear_items()
        APP.processEvents()
        APP.database.reload()
        self.draw_items(APP.database)



class NavBar(QFrame):

    def __init__(self, buttons: Sequence[NavButton]) -> None:
        super().__init__()
        self.setObjectName("nav-bar")
        self.buttons = buttons

        self.setStyleSheet("""
            QFrame#nav-bar {
                border-top: 3px solid black;
                background-color: #abd1c6;
                border-top-left-radius: 10px;
                border-top-right-radius: 10px;
            }
        """)

        # Setup layout for NavBar
        self.hbox = QHBoxLayout()
        self.hbox.setContentsMargins(0, 0, 0, 0)
        self.hbox.setSpacing(0)
        self.setLayout(self.hbox)
        self.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)

        # Add the different buttons to the navigation bar
        for button in self.buttons:
            self.hbox.addWidget(button)    



class EnterScreen(QFrame):
    clicked = pyqtSignal()

    def __init__(self) -> None:
        super().__init__()

        self.vbox = QVBoxLayout()
        self.vbox.setContentsMargins(0, 0, 0, 0)
        self.vbox.setSpacing(20)
        self.setLayout(self.vbox)

        # Logo setup
        logo = QPixmap("resources\\logo_circle.png").scaledToWidth(200, Qt.TransformationMode.SmoothTransformation)
        self.logo_label = QLabel()
        self.logo_label.setPixmap(logo)
        self.logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Authors label
        self.authors_label = QLabel("""A Python system group project by\nAcuña, Clarence\nAlberto, Neille Arghie\nCallos, Joseph\nGalvez, Khelvin\nNaquita, Loui Dominic\nVigo, Mark John Owen
        """)
        self.authors_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.authors_label.setObjectName("authors")
        self.authors_label.setStyleSheet("""
            QLabel#authors {                               
                font-family: 'Nunito Sans';
                font-size: 16px;  
                color: white;                            
                text-align: center;
                qproperty-alignment: 'AlignCenter';
                line-height: 1;
            }
        """)

        # Button setup
        self.enter_button = QPushButton("Enter")
        self.enter_button.setObjectName("enter-button")
        self.enter_button.setStyleSheet("""
            QPushButton#enter-button {
                font-family: 'Montserrat';
                font-weight: bold;
                font-size: 20px;
                padding: 10px;
                background-color: #f9bc60;
                border-radius: 10px;                        
            }
        """)

        self.enter_button.clicked.connect(self.mousePressed)

        self.vbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.vbox.addWidget(self.logo_label)
        self.vbox.addWidget(self.authors_label)
        self.vbox.addWidget(self.enter_button)

    def mousePressEvent(self, event): # type: ignore
        super().mousePressEvent(event)
        self.clicked.emit()

    def mousePressed(self):
        from app import APP
        APP.app_window.switch_to_home()


class HomeScreen(QFrame):

    def __init__(self) -> None:
        super().__init__()
        
        self.vbox = QVBoxLayout()
        self.vbox.setContentsMargins(0, 0, 0, 0)
        self.vbox.setSpacing(0)
        self.setLayout(self.vbox)

        self.header = InventoryHeader()
        self.inv_scroll = InventoryScroll()

        # Setup nav buttons
        inventory_btn = NavButton("Inventory", QPixmap("resources\\inv.png"))
        settings_btn = NavButton("Settings", QPixmap("resources\\settings.png"))

        inventory_btn.clicked.connect(lambda: self.set_selected(0))
        settings_btn.clicked.connect(lambda: self.set_selected(1))

        self.navbar = NavBar([inventory_btn, settings_btn])
        self.vbox.addWidget(self.header)
        self.vbox.addWidget(self.inv_scroll)
        self.vbox.addWidget(self.navbar)
        self.setObjectName("home-screen")
       
        # Initial selected
        self.set_selected(0)

        # Add button
        self.add_new_button = AddNewButton()
        self.add_new_button.resize(60, 60)
        self.add_new_button.setParent(self)
        self._position_fab()


    def set_selected(self, i: int) -> None:
        for nav_button in self.navbar.buttons:
            nav_button.set_deselected()

        self.navbar.buttons[i].set_selected()

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