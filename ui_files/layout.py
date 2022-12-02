import sys

from PyQt5.QtWidgets import (
    QApplication,
    QDialog,
    QMainWindow
)
from demoRadioButton1 import Ui_Dialog

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.radioButtonFirstClass.toggled.connect(self.dispFare)
        self.ui.radioButtonSecondClass.toggled.connect(self.dispFare)
        self.ui.radioButtonEconomyClass.toggled.connect(self.dispFare)
        self.show()

    def dispFare(self):
        fare = 0
        if self.ui.radioButtonFirstClass.isChecked() == True:
            fare = 150
        if self.ui.radioButtonSecondClass.isChecked() == True:
            fare = 120
        if self.ui.radioButtonEconomyClass.isChecked() == True:
            fare = 100
        self.ui.labelFare.setText("Air Fare is "+str(fare))

    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyForm()
    window.show()
    sys.exit(app.exec_())