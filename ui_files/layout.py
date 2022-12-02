import sys

from PyQt5.QtWidgets import (
    QApplication,
    QDialog,
    QMainWindow
)
from demoLineEdits import Ui_MainWindow

class MyForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.ButtonClickMe.clicked.connect(self.dispmessage)
        self.show()
    def dispmessage(self):
        self.ui.labelResponse.setText("Hello " + self.ui.lineEditName.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyForm()
    window.show()
    sys.exit(app.exec_())