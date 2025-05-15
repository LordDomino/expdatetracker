import sys
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QFrame
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QApplication

def main():
    app = QApplication(sys.argv)
    win = QMainWindow()
    
    wid = QFrame()
    button = QPushButton("Hello", win)



    container = QFrame()
    cont_vbox = QVBoxLayout()

    cont_vbox.addWidget(button)
    cont_vbox.addWidget(wid)

    win.setCentralWidget(container)

    vbox = QVBoxLayout()

    for i in range(5):
        label = QLabel(f"Label {i + 1}")
        vbox.addWidget(label)

    container.setLayout(cont_vbox)
    wid.setLayout(vbox)

    

    def remove():
        for i in reversed(range(vbox.count())): 
            vbox.itemAt(i).widget().setText("H")
            vbox.itemAt(i).widget().setParent(None)

    button.clicked.connect(remove)
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()