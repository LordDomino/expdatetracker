from PyQt5.QtWidgets import (
    QFrame,
    QVBoxLayout,
    QLabel,
    
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



class ItemExpiryLabel(QLabel):
    def __init__(self, text: str) -> None:
        super().__init__(text=text)
        self.setObjectName("item-expiry-label")



class ItemRemainingDaysLabel(QLabel):
    def __init__(self, text: str) -> None:
        super().__init__(text=text)
        self.setObjectName("item-remaning-days-label")



class Item(QFrame):
    def __init__(self, name: str, expiry: str, remaining_days: int) -> None:
        self.item_name = name
        self.expiry = expiry
        self.remaining_days = remaining_days
