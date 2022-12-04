import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import (
    QApplication,
    QDialog,
    QMainWindow,
    QInputDialog,
    QListWidgetItem
)
from demoSlider import Ui_Dialog

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.horizontalScrollBarSugarLevel.valueChanged.connect(self.scrollhorizontal)
        self.ui.verticalScrollBarPulseRate.valueChanged.connect(self.scrollvertical)
        self.ui.horizontalSliderBloodPressure.valueChanged.connect(self.sliderhorizontal)
        self.ui.verticalSliderCholestLevel.valueChanged.connect(self.slidervertical)
        self.show()
 
    def scrollhorizontal(self,value):
        self.ui.lineEditResult.setText("Sugar Level : "+str(value))
    
    def scrollvertical(self, value):
        self.ui.lineEditResult.setText("Pulse Rate : "+str(value))
    
    def sliderhorizontal(self, value):
        self.ui.lineEditResult.setText("Blood Pressure : "+str(value))

    def slidervertical(self, value):
        self.ui.lineEditResult.setText("Cholestrol Level : "+str(value))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyForm()
    window.show()
    sys.exit(app.exec_())