import sys
from PyQt5 import QtWidgets
from MainWindow import Ui_MainWindow
import random
num = random.randint(1,100)

class guessTheNumber(QtWidgets.QMainWindow):
    def __init__(self):
        super(guessTheNumber,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.sendButton.clicked.connect(self.result)
        self.counter = 1    


    def result(self,counter):
        if int(self.ui.lineEditGuess.text()) > num:
            self.ui.labelNum3.setText(str("Too High"))
            self.ui.labelTry.setText(f"{self.counter} Try")
    
        elif int(self.ui.lineEditGuess.text()) < num:
            self.ui.labelNum3.setText(str("Too Low"))
            self.ui.labelTry.setText(f"{self.counter} Try")

        elif int(self.ui.lineEditGuess.text()) == num:
            self.ui.labelNum3.setText(str(f"Bingo! You took only {self.counter} tries!"))
            self.ui.labelTry.setText(f"{self.counter} Try")
        self.counter += 1

                
 
            


app = QtWidgets.QApplication(sys.argv)
win = guessTheNumber()
win.show()
sys.exit(app.exec_())

