from tkinter import Misc
from tkinter.ttk import Button
from tkinter.ttk import Style


class CButton(Button):
    def __init__(self, master: Misc | None = None, text: float | str = "") -> None:
        style = Style()
        style.configure("TButton", foreground="red", background="white")
        super().__init__(master, text=text, style="TButton")