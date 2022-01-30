import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
def calculaterApp():
    app = QtWidgets.QApplication(sys.argv)
    win = QtWidgets.QMainWindow()
    win.setWindowTitle("Calculater App")
    win.setGeometry(800,200,250,00)
    win.setWindowIcon(QIcon("applogo.png"))


    #Labels
    label_num1 = QtWidgets.QLabel(win)
    label_num1.setText("1st Number :")
    label_num1.move(20,20)
    
    label_num2 = QtWidgets.QLabel(win)
    label_num2.setText("2nd Number :")
    label_num2.move(20,55)

    labelResult = QtWidgets.QLabel(win)
    labelResult.setText("RESULT :")
    labelResult.move(20,260)
  
    labelResult2 = QtWidgets.QLabel(win)
    labelResult2.setText("  ")
    labelResult2.move(100,260)

    
    #Line Edits
    lineEditNum1 = QtWidgets.QLineEdit(win)
    lineEditNum1.move(100,20)
    lineEditNum1.resize(100,25)

    lineEditNum2 = QtWidgets.QLineEdit(win)
    lineEditNum2.move(100,55)
    lineEditNum2.resize(100,25)

    def add():
        result = int(lineEditNum1.text()) + int(lineEditNum2.text())
        labelResult2.setText(str(result))

    def substract():
        result = int(lineEditNum1.text()) - int(lineEditNum2.text())
        labelResult2.setText(str(result))

    def multiply():
        result = int(lineEditNum1.text()) * int(lineEditNum2.text())
        labelResult2.setText(str(result))

    def divide():
        result = int(lineEditNum1.text()) / int(lineEditNum2.text())
        labelResult2.setText(str(result))

    #Buttons
    buttonAdd =  QtWidgets.QPushButton(win)
    buttonAdd.setText("Add")
    buttonAdd.move(100,100)
    buttonAdd.clicked.connect(add)

    buttonSubstract =  QtWidgets.QPushButton(win)
    buttonSubstract.setText("Substract")
    buttonSubstract.move(100,140)
    buttonSubstract.clicked.connect(substract)

    buttonMultiply =  QtWidgets.QPushButton(win)
    buttonMultiply.setText("Multiply")
    buttonMultiply.move(100,180)
    buttonMultiply.clicked.connect(multiply)

    buttonDivide =  QtWidgets.QPushButton(win)
    buttonDivide.setText("Divide")
    buttonDivide.move(100,220)
    buttonDivide.clicked.connect(divide)

    win.show()
    sys.exit(app.exec_())

calculaterApp()