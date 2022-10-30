from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys

def clicked():
    print("clicked")

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 1000, 600)
    win.setWindowTitle("Tech With Timi!")

    # Label
    label = QtWidgets.QLabel(win)
    label.setText("Anamo App")

    # Button
    b1 = QtWidgets.QPushButton(win)
    b1.setText("Click me")
    b1.clicked.connect(clicked)
    

    win.show()
    sys.exit(app.exec_())

window()