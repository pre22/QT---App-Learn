from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys

class MyWindow(QMainWindow):
    def __ini__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200, 200, 1000, 600)
        self.setWindowTitle("Tech With Timi!")
        self.initUI()
    
    def initUI(self):
        # Label
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Anamo App")

        # Button
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Click me")
        self.b1.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText("You pressedthe button")


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    # win = QMainWindow()
    win.setGeometry(200, 200, 1000, 600)
    win.setWindowTitle("Tech With Timi!")
    win.show()
    sys.exit(app.exec_())


# window = MyWindow()
window()