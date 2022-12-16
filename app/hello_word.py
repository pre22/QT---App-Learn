# from PyQt5 import QtWidgets
# from PyQt5.QtWidgets import QApplication,QMainWindow
# import sys

# class MyWindow(QMainWindow):
#     def __ini__(self):
#         super(MyWindow, self).__init__()
#         self.setGeometry(200, 200, 1000, 600)
#         self.setWindowTitle("Tech With Timi!")
#         self.initUI()
    
#     def initUI(self):
#         # Label
#         self.label = QtWidgets.QLabel(self)
#         self.label.setText("Anamo App")

#         # Button
#         self.b1 = QtWidgets.QPushButton(self)
#         self.b1.setText("Click me")
#         self.b1.clicked.connect(self.clicked)

#     def clicked(self):
#         self.label.setText("You pressedthe button")


# def window():
#     app = QApplication(sys.argv)
#     win = MyWindow()
#     # win = QMainWindow()
#     win.setGeometry(200, 200, 1000, 600)
#     win.setWindowTitle("Tech With Timi!")
#     win.show()
#     sys.exit(app.exec_())


# # window = MyWindow()
# window()


from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget

import sys

from random import randint


class AnotherWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another Window % d" % randint(0,100))
        layout.addWidget(self.label)
        self.setLayout(layout)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.w = AnotherWindow()
        self.button = QPushButton("Push for Window")
        self.button.clicked.connect(self.toggle_window)
        self.setCentralWidget(self.button)

    def toggle_window(self, checked):
        if self.w.isVisible():
            self.w.hide()

        else:
            self.w.show()


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()

# import sys
# from random import randint

# from PyQt5.QtWidgets import (
#     QApplication,
#     QLabel,
#     QMainWindow,
#     QPushButton,
#     QVBoxLayout,
#     QWidget,
# )


# class AnotherWindow(QWidget):
#     """
#     This "window" is a QWidget. If it has no parent,
#     it will appear as a free-floating window.
#     """

#     def __init__(self):
#         super().__init__()
#         layout = QVBoxLayout()
#         self.label = QLabel("Another Window % d" % randint(0, 100))
#         layout.addWidget(self.label)
#         self.setLayout(layout)


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.window1 = AnotherWindow()
#         self.window2 = AnotherWindow()

#         l = QVBoxLayout()
#         button1 = QPushButton("Push for Window 1")
#         button1.clicked.connect(
#             lambda checked: self.toggle_window(self.window1)
#         )
#         l.addWidget(button1)

#         button2 = QPushButton("Push for Window 2")
#         button2.clicked.connect(
#             lambda checked: self.toggle_window(self.window2)
#         )
#         l.addWidget(button2)

#         w = QWidget()
#         w.setLayout(l)
#         self.setCentralWidget(w)

#     def toggle_window(self, window):
#         if window.isVisible():
#             window.hide()

#         else:
#             window.show()


# app = QApplication(sys.argv)
# w = MainWindow()
# w.show()
# app.exec()