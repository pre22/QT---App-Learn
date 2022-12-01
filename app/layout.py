import sys

from PyQt5.Widgets import (
    QApplication,
    QHBoxLayout,
    QPushButton,
    QWidget
)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QHBoxLayout Example")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())