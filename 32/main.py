import sys
from PyQt5 import QtWidgets
from MainWindow import Ui_MainWindow

class myCalculator(QtWidgets.QMainWindow):
    def __init__(self):
        super(myCalculator,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.addButton.clicked.connect(self.add)
        self.ui.buttonSubstract.clicked.connect(self.substract)
        self.ui.buttonMultiply.clicked.connect(self.multiply)
        self.ui.buttonDivide.clicked.connect(self.divide)

    def add(self):
        result = int(self.ui.lineEditNum1.text()) + int(self.ui.lineEditNum2.text())
        self.ui.resultLabel2.setText(str(result))
 
    def substract(self):
        result = int(self.ui.lineEditNum1.text()) - int(self.ui.lineEditNum2.text())
        self.ui.resultLabel2.setText(str(result))
 
    def multiply(self):
        result = int(self.ui.lineEditNum1.text()) * int(self.ui.lineEditNum2.text())
        self.ui.resultLabel2.setText(str(result))
    def divide(self):
        result = int(self.ui.lineEditNum1.text()) / int(self.ui.lineEditNum2.text())
        self.ui.resultLabel2.setText(str(result))


app = QtWidgets.QApplication(sys.argv)
win = myCalculator()
win.show()
sys.exit(app.exec_())