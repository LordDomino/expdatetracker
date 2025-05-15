from PyQt5.QtWidgets import (
    QFrame,
    QVBoxLayout,
    QLabel,
    QPushButton
)
from PyQt5.QtCore import Qt




class NavButton(QFrame):

    def __init__(self, label: str, image = None) -> None:
        super().__init__()
        self.setObjectName("nav-button")

        # Set layout for NavButton
        self.vbox = QVBoxLayout()
        self.setLayout(self.vbox)
        self.vbox.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label = QLabel(label, self)
        self.label.setObjectName("button-text")

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



class ItemRemainingDaysLabel(QLabel):
    def __init__(self, val: int) -> None:
        super().__init__(text=self._generate_label_text(val))
        self.setObjectName("item-remaining-days-label")

    def _generate_label_text(self, rem_days: int) -> str:
        if rem_days <= 0:
            return "Expired"
        elif rem_days == 1:
            return f"Expires in {rem_days} day"
        else:
            return f"Expires in {rem_days} days"



class Item(QFrame):
    def __init__(self, name: str, expiry: str, remaining_days: int) -> None:
        super().__init__()
        self.setObjectName("item")
        self.name = name
        self.exp = expiry
        self.rd = remaining_days

        # Setup layout of item widget
        self.vbox = QVBoxLayout()
        self.vbox.setContentsMargins(0, 0, 0, 0)
        self.vbox.setSpacing(0)
        self.setLayout(self.vbox)

        # Generate item info labels
        self._name_label = ItemName(self.name)
        self._exp_label = ItemExpiryLabel(f"Best Before {self.exp}")
        self._rd_label = ItemRemainingDaysLabel(self.rd)

        # Add item info labels
        self.vbox.addWidget(self._name_label)
        self.vbox.addWidget(self._exp_label)
        self.vbox.addWidget(self._rd_label)

        self.setStyleSheet("""
            QFrame#item {
                padding: 10px;
                border-radius: 10px;
                background: #f8f8f8;
                border: 1px solid #e0e0e0;
            }
        """)



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