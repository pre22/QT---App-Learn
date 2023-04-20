import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox


class MyWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        btn_exit = QPushButton('Exit', self)
        btn_exit.setGeometry(50, 50, 100, 50)
        btn_exit.clicked.connect(self.on_exit_clicked)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Exit Example')
        self.show()

    def on_exit_clicked(self):

        # Display a message box asking if the user really wants to exit
        reply = QMessageBox.question(self, 'Message', 'Are you sure you want to exit?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        # If the user clicks Yes, exit the application
        if reply == QMessageBox.Yes:
            print('Yes')
            QApplication.quit()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    widget = MyWidget()
    sys.exit(app.exec_())
