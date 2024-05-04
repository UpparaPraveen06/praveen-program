from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import *
import sys
from ADDITUINui import *

class Naveen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.calculate)
    def calculate(self):
        a = float(self.ui.lineEdit.text())
        b = float(self.ui.lineEdit_2.text())
        c = a+b
        self.ui.label_4.setText("Result = {:.2f}".format(c))

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = Naveen()
    w.show()
    sys.exit(app.exec_())

