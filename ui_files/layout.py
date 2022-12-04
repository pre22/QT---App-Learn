import sys

from PyQt5.QtWidgets import (
    QApplication,
    QDialog,
    QMainWindow
)
from demoListWidget2 import Ui_Dialog

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.listWidgetDiagnosis.itemSelectionChanged.connect(self.dispSelectedTest)
        # self.ui.listWidgetDiagnosis.itemClicked.connect(self.dispSelectedTest)
        self.show()
    
    def dispSelectedTest(self):
        self.ui.listWidgetSelectedTests.clear()
        items = self.ui.listWidgetDiagnosis.selectedItems()
        for i in list(items):
            self.ui.listWidgetSelectedTests.addItem(i.text())




        

    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyForm()
    window.show()
    sys.exit(app.exec_())