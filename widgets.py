from typing import override
from PyQt5.QtWidgets import (
    QFrame,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit,
    QDialog,
    QGridLayout,
    QTextEdit,
    QSizePolicy
)
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap
import re


class NavButton(QFrame):
    clicked = pyqtSignal()

    def __init__(self, label: str, image: QPixmap) -> None:
        super().__init__()
        self.setObjectName("nav-button")

        # Image setup
        self.img_label = QLabel()
        self.img_label.setPixmap(image)

        # Set layout for NavButton
        self.vbox = QVBoxLayout()
        self.vbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(self.vbox)

        self.label = QLabel(label, self)
        self.label.setObjectName("nav-button")
        self.label.setStyleSheet(""" 
            QLabel#nav-button{
                background-color: rgba(0, 0, 0, 0);
                font-family: 'Montserrat';
                font-size: 14px;
            }
        """)
        self.setObjectName("nav-button")
        self.setStyleSheet("""   
            QFrame#nav-button:hover {
                font-weight: bold;
                background-color: red;
                border-radius: 5px;    
            }
        """)

        self.vbox.addWidget(self.img_label, 0, Qt.AlignmentFlag.AlignCenter)
        self.vbox.addWidget(self.label, 0, Qt.AlignmentFlag.AlignCenter)

        # Interaction styling

    
    def mousePressEvent(self, event): # type: ignore
        super().mousePressEvent(event)
        self.clicked.emit()

    def set_selected(self) -> None:
        self.setStyleSheet("""   
            QFrame#nav-button {
                font-weight: bold;
                background-color: #e16162;
                border-radius: 5px;
            }

            QFrame#nav-button:hover {
                font-weight: bold;
                background-color: #e89595;
                border-radius: 5px;    
            }
        """)

    def set_deselected(self) -> None:
        self.setStyleSheet("""   
            QFrame#nav-button {
                font-weight: bold;
                background-color: #abd1c6;
                border-radius: 5px;
            }
                           
            QFrame#nav-button:hover {
                font-weight: bold;
                background-color: #ccf0e5;
                border-radius: 5px;    
            }
        """)

    

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
        if rem_days < 0:
            return "Expires today"
        elif rem_days == 1:
            return "Expires tomorrow"
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
                    color: #a6a300;
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



class ItemNotes(QLabel):

    def __init__(self, text: str) -> None:
        super().__init__(text=text)
        self.setObjectName("item-notes")
        self.setStyleSheet("""
            QLabel#item-notes {
                font-size: 14px;
                font-family: 'Nunito Sans';
            }
        """)
        self.setWordWrap(True)



class Item(QFrame):
    def __init__(self, id: int, name: str, expiry: str, remaining_days: int, notes: str) -> None:
        super().__init__()
        self.setObjectName("item")
        self.id = id
        self.name = name
        self.exp = expiry
        self.rd = remaining_days
        self.notes = notes

        # Setup layout of item widget
        self.grid = QGridLayout()
        self.grid.setContentsMargins(0, 0, 0, 0)
        self.grid.setSpacing(0)
        self.setLayout(self.grid)

        # Generate item info labels
        self._name_label = ItemName(self.name)
        self._exp_label = ItemExpiryLabel(f"Best Before {self.exp}")
        self._rd_label = ItemRemainingDaysLabel(self.rd)
        self._check_img_label = CheckButton()
        self._consume_button = QPushButton("Consume")
        self._fav_button = QPushButton("Fav")
        self._notes = ItemNotes(self.notes)

        self._check_img_label.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self._check_img_label.clicked.connect(self.clicked_consume)

        # Add item info labels
        self.grid.addWidget(self._name_label, 0, 1, Qt.AlignmentFlag.AlignBottom)
        self.grid.addWidget(self._exp_label, 1, 1, Qt.AlignmentFlag.AlignVCenter)
        self.grid.addWidget(self._rd_label, 2, 1, Qt.AlignmentFlag.AlignTop)
        # self.grid.addWidget(self._fav_button, 0, 2, 4, 1, Qt.AlignmentFlag.AlignCenter)

        self.grid.setColumnStretch(0, 0)
        self.grid.setColumnStretch(1, 1)
        self.grid.setColumnStretch(2, 0)
        
        if self.notes:
            self.grid.addWidget(self._notes, 3, 1)
            self.grid.addWidget(self._check_img_label, 0, 0, 4, 1, Qt.AlignmentFlag.AlignCenter)
        else:
            self.grid.addWidget(self._check_img_label, 0, 0, 3, 1, Qt.AlignmentFlag.AlignCenter)

        self._auto_set_style()

    def clicked_consume(self) -> None:
        from app import APP
        APP.database.delete_product_by_id(self.id)
        APP.home_screen.inv_scroll.redraw_items()

    def _auto_set_style(self) -> None:
        if self.rd < 0:
            self.setStyleSheet("""
                QFrame#item {
                    padding: 10px;
                    border-radius: 10px;
                    background: #ffe0db;
                    border: 1px solid #e0e0e0;
                }
            """)
        elif self.rd <= 7:
            self.setStyleSheet("""
                QFrame#item {
                    padding: 10px;
                    border-radius: 10px;
                    background: #ffeedb;
                    border: 1px solid #e0e0e0;
                }
            """)
        elif self.rd <= 28:
            self.setStyleSheet("""
                QFrame#item {
                    padding: 10px;
                    border-radius: 10px;
                    background: #fffddb;
                    border: 1px solid #e0e0e0;
                }
            """)
        elif self.rd <= 365:
            self.setStyleSheet("""
                QFrame#item {
                    padding: 10px;
                    border-radius: 10px;
                    background: #e8ffdb;
                    border: 1px solid #e0e0e0;
                }
            """)



class CheckButton(QLabel):
    clicked = pyqtSignal()

    def __init__(self) -> None:
        super().__init__()
        self.img = QPixmap("resources\\clipboard_check.png")
        self.img = self.img.scaledToWidth(40, Qt.TransformationMode.SmoothTransformation)
        self.setPixmap(self.img)
        self.setObjectName("check-button")

        self.setStyleSheet("""
            QLabel#check-button {
                margin: 10px;               
            }
        """)

    def mousePressEvent(self, event): # type: ignore
        super().mousePressEvent(event)
        self.clicked.emit()



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
                font-family: 'Nunito Sans';
                font-size: 14px;
                border: 1px solid #AAAAAA;
                border-radius: 5px;
                padding: 5px;
            }
        """)



class TextArea(QTextEdit):

    def __init__(self) -> None:
        super().__init__()
        self.setObjectName("text-area")

        self.setStyleSheet("""
            QTextEdit#text-area {
                font-family: 'Nunito Sans';
                font-size: 14px;
                border: 1px solid #AAAAAA;
                border-radius: 5px;
                padding: 5px;
            }
        """)



class PopupDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Add New Food Item")
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.heading = Heading1("Add new food item")

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
        self.note_field = TextArea()
        self.confirm = QPushButton("Confirm")

        self.note_field.resize(self.note_field.width(), self.note_field.height() * 2)

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
                self.note_field.toPlainText()
            )
            APP.home_screen.inv_scroll.redraw_items()

    def _check_name(self) -> bool:
        return bool(self.name_field.text().strip())
    
    def _check_date(self) -> bool:
        if self.exp_field.text().strip():
            if re.match("^[0-9]{2}-[0-9]{2}-[0-9]{4}$", self.exp_field.text()):
                return True
        return False
