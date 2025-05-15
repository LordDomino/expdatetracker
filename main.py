from inspect import formatargvalues
from tkinter import Tk
from tkinter.ttk import Button, Style

# from styles import BUTTON_STYLE, configure_styles

# PROGRAM CONSTANTS
# Variables considered as global configuration values for root window
WIN_TITLE: str = "Expiration Date Tracker"
WIN_HEIGHT: int = 1920
WIN_WIDTH: int = 1080
WIN_SCALE: float = 0.4  # The actual display resolution of the root window is
                        # determined by the product of the height and the width
                        # with the scale.
WIN_RATIO: float = WIN_WIDTH / WIN_HEIGHT


# Style configurations


# Main tkinter object
root: Tk = Tk()


# Configure styles
style = Style()
style.configure("TButton", foreground="red", background="blue")


# Widgets here
button = Button(root, text="Hello World!", style="TButton")
button.pack()

# Properties of root object
root.title(WIN_TITLE)
root.geometry(f"{int(WIN_WIDTH*WIN_SCALE)}x{int(WIN_HEIGHT*WIN_SCALE)}")


if __name__ == "__main__":
    root.mainloop()