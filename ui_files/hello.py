import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import (
    QApplication,
    QDialog,
    QMainWindow,
    QInputDialog,
    QListWidgetItem,
    QFileDialog
)
from qstackedwidget import Ui_MainWindow

class MyForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.stackedWidget.setCurrentWidget(self.ui.Home)
        self.ui.RedButton.clicked.connect(self.showRed)
        self.ui.BlueButton.clicked.connect(self.showBlue)
        self.ui.YellowBUtton.clicked.connect(self.showYellow)
        self.show()

    def showYellow(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Yellow)
        
    def showBlue(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Blue)

    def showRed(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Red)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyForm()
    window.show()
    sys.exit(app.exec_())