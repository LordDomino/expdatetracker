from typing import override
from PyQt5.QtWidgets import (
    QFrame,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit,
    QDialog,
    QGridLayout
)
from PyQt5.QtCore import Qt
import re


class NavButton(QFrame):

    def __init__(self, label: str, image = None) -> None:
        super().__init__()
        self.setObjectName("nav-button")

        # Set layout for NavButton
        self.vbox = QVBoxLayout()
        self.setLayout(self.vbox)
        self.vbox.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label = QLabel(label, self)
        self.label.setObjectName("nav-button")
        self.label.setStyleSheet(""" 
            QLabel#nav-button{
                Font-family: 'Montserrat';
                Font-size: 20px;
            }
        """)
        self.setObjectName("nav-button")
        self.setStyleSheet("""   
             QFrame#nav-button:hover {
                font-weight: bold;
                background-color: red;
                }
            """)
        self.vbox.addWidget(self.label)

        # Interaction styling

    
    def mousePressEvent(self, event): # type: ignore
        print(f"Button {self.label.text()} is clicked")
        super().mousePressEvent(event)

    

class ItemName(QLabel):
    def __init__(self, text: str) -> None:
        super().__init__(text=text)
        self.setObjectName("item-name")

        self.setStyleSheet("""
            QLabel#item-name {
                font-size: 18px;
                font-weight: bold;
                font-family: 'Roboto Regular';
            }
        """)



class ItemExpiryLabel(QLabel):
    def __init__(self, text: str) -> None:
        super().__init__(text=text)
        self.setObjectName("item-expiry-label")
        self.setStyleSheet("""
            QLabel#item-expiry-label {
                font-size: 14px;
                font-family: 'Nunito Sans';
            }
        """)



class ItemRemainingDaysLabel(QLabel):
    def __init__(self, val: int) -> None:
        super().__init__(text=self._generate_label_text(val))
        self.rem_days = val
        self.setObjectName("item-remaining-days-label")
        self._auto_set_font_color()

    def _generate_label_text(self, rem_days: int) -> str:
        if rem_days <= 0:
            return "Expired"
        elif rem_days == 1:
            return f"Expires in {rem_days} day"
        else:
            return f"Expires in {rem_days} days"

    def _auto_set_font_color(self) -> None:
        if self.rem_days < 0:
            self.setStyleSheet("""
                QLabel#item-remaining-days-label {
                    font-size: 14px;
                    font-weight: bold;
                    font-family: 'Nunito Sans';
                    color: red;
                }
            """)
        elif self.rem_days <= 7:
            self.setStyleSheet("""
                QLabel#item-remaining-days-label {
                    font-size: 14px;
                    font-weight: bold;
                    font-family: 'Nunito Sans';
                    color: orange;
                }
            """)
        elif self.rem_days <= 28:
            self.setStyleSheet("""
                QLabel#item-remaining-days-label {
                    font-size: 14px;
                    font-weight: bold;
                    font-family: 'Nunito Sans';
                    color: yellow;
                }
            """)
        elif self.rem_days <= 365:
            self.setStyleSheet("""
                QLabel#item-remaining-days-label {
                    font-size: 14px;
                    font-weight: bold;
                    font-family: 'Nunito Sans';
                    color: green;
                }
            """)



class Item(QFrame):
    def __init__(self, id: int, name: str, expiry: str, remaining_days: int) -> None:
        super().__init__()
        self.setObjectName("item")
        self.id = id
        self.name = name
        self.exp = expiry
        self.rd = remaining_days
        self.consume_button = QPushButton("Consume")
        self.fav_button = QPushButton("Fav")

        self.consume_button.clicked.connect(self.clicked_consume)

        # Setup layout of item widget
        self.grid = QGridLayout()
        self.grid.setContentsMargins(0, 0, 0, 0)
        self.grid.setSpacing(0)
        self.setLayout(self.grid)

        # Generate item info labels
        self._name_label = ItemName(self.name)
        self._exp_label = ItemExpiryLabel(f"Best Before {self.exp}")
        self._rd_label = ItemRemainingDaysLabel(self.rd)

        # Add item info labels
        self.grid.addWidget(self._name_label, 0, 1)
        self.grid.addWidget(self._exp_label, 1, 1)
        self.grid.addWidget(self._rd_label, 2, 1)
        self.grid.addWidget(self.consume_button, 0, 0, 3, 1, Qt.AlignmentFlag.AlignCenter)
        self.grid.addWidget(self.fav_button, 0, 2, 3, 1, Qt.AlignmentFlag.AlignCenter)

        self.setStyleSheet("""
            QFrame#item {
                padding: 10px;
                border-radius: 10px;
                background: #f8f8f8;
                border: 1px solid #e0e0e0;
            }
        """)

    def clicked_consume(self) -> None:
        from app import APP
        APP.database.delete_product_by_id(self.id)
        APP.init_screen.inv_scroll.redraw_items()



class AddNewButton(QPushButton):
    def __init__(self) -> None:
        super().__init__(text="+")
        self.setObjectName("add-new-button")

        self.setStyleSheet("""
            QPushButton#add-new-button {
                background-color: #f9bc60;
                border-radius: 30px;
                border: 1px solid #000000;
                font-size: 30px;
                text-align: center;
            }
        """)

    @override
    def mousePressEvent(self, event) -> None: # type: ignore
        print("Add new printed")
        popup = PopupDialog(self)
        popup.exec_()



################################################################################
###### POP UP WIDGETS ##########################################################
################################################################################



class Heading1(QLabel):

    def __init__(self, text: str) -> None:
        super().__init__(text=text)
        self.setObjectName("heading1")

        self.setStyleSheet("""
            QLabel#heading1 {
                color: #004643;
                font-family: 'Montserrat';
                font-size: 30px;
                font-weight: bold;
            }
        """)



class FieldLabel(QLabel):

    def __init__(self, text: str) -> None:
        super().__init__(text=text)
        self.setObjectName("field-label")

        self.setStyleSheet("""
            QLabel#field-label {
                font-family: 'Roboto Regular';
                font-size: 12px;
            }
        """)



class Field(QLineEdit):

    def __init__(self) -> None:
        super().__init__()
        self.setObjectName("field")

        self.setStyleSheet("""
            QLineEdit#field {
                font-family: 'Roboto Regular';
                font-size: 20px;
            }
        """)



class PopupDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Add New Food Item")
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.heading = Heading1("Add New")

        self.setObjectName("popup-bg")
        self.setStyleSheet(""" 
            QDialog#popup-bg    {        
                background-color: #F5F5DC
            } 
        """)
        
        self.name_label = FieldLabel("Item Name")
        self.name_field = Field()
        self.exp_label = FieldLabel("Expiration Date")
        self.exp_field = Field()
        self.note_label = FieldLabel("Add Note")
        self.note_field = Field()
        self.confirm = QPushButton("Confirm")

        

        self.grid.addWidget(self.heading, 0, 0)
        self.grid.addWidget(self.name_label, 1, 0)
        self.grid.addWidget(self.name_field, 2, 0)
        self.grid.addWidget(self.exp_label, 3, 0)
        self.grid.addWidget(self.exp_field, 4, 0)
        self.grid.addWidget(self.note_label, 5, 0)
        self.grid.addWidget(self.note_field, 6, 0)
        self.grid.addWidget(self.confirm, 7, 0)

        self.confirm.clicked.connect(self._confirmed)

    def _confirmed(self):
        from app import APP

        if self._check_name() and self._check_date():
            APP.database.add_product(
                self.name_field.text(),
                self.exp_field.text(),
                "false",
                self.note_field.text()
            )
            APP.init_screen.inv_scroll.redraw_items()

    def _check_name(self) -> bool:
        return bool(self.name_field.text().strip())
    
    def _check_date(self) -> bool:
        if self.exp_field.text().strip():
            if re.match("^[0-9]{2}-[0-9]{2}-[0-9]{4}$", self.exp_field.text()):
                return True
        return False


        