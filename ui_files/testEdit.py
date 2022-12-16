import sqlite3, sys
from sqlite3 import Error
from PyQt5 import QtGui
from PyQt5.QtWidgets import (
    QApplication,
    QDialog,
    QMainWindow,
    QInputDialog,
    QListWidgetItem,
    QFileDialog
)
from demoDatabase import Ui_MainWindow

class MyForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButtonCreateDB.clicked.connect(self.createDatabase)
        self.show()

    def createDatabase(self):
        try:
            conn = sqlite3.connect(self.ui.lineEditDBName.text()+".db")
            self.ui.labelResponse.setText("Database is created")
            conn.close()
        except Error as e:
            self.ui.labelResponse.setText("Some error has occurred")

        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyForm()
    window.show()
    sys.exit(app.exec_())