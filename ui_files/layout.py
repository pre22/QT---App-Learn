import sys

from PyQt5.QtWidgets import (
    QApplication,
    QDialog,
    QMainWindow
)
from demoCheckBox1 import Ui_Dialog

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.checkBoxCheese.stateChanged.connect(self.dispAmount)
        self.ui.checkBoxOlives.stateChanged.connect(self.dispAmount)
        self.ui.checkBoxSausages.stateChanged.connect(self.dispAmount)

        self.show()

    def dispAmount(self):
        amount = 10

        if self.ui.checkBoxCheese.isChecked() == True:
            amount = amount+1
        if self.ui.checkBoxOlives.isChecked() == True:
            amount = amount+1
        if self.ui.checkBoxSausages.isChecked() == True:
            amount = amount+2
        
        self.ui.labelAmount.setText("Total amount for pizza is "+str(amount))

    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyForm()
    window.show()
    sys.exit(app.exec_())