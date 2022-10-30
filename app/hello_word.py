from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 1000, 600)
    win.setWindowTitle("Tech With Timi!")

    label = QtWidgets.QLabel(win)
    label.setText("Anamo App")
    

    win.show()
    sys.exit(app.exec_())

window()