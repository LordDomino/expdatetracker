# PROGRAM CONSTANTS
# Variables considered as global configuration values for main window
WIN_TITLE: str = "Expiration Date Tracker"
WIN_HEIGHT: int = 1920
WIN_WIDTH: int = 1080
WIN_SCALE: float = 0.4  # The actual display resolution of the main window is
                        # determined by the product of the height and the width
                        # with the scale.
WIN_RATIO: float = WIN_WIDTH / WIN_HEIGHT