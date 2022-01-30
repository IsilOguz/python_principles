from turtle import onclick
from PyQt5.QtWidgets import QApplication, QMainWindow,QLabel,QLineEdit,QPushButton
from PyQt5.QtGui import QIcon
import sys


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setWindowTitle("Aeon's App")
    win.setGeometry(300,300,300,300)
    win.setWindowIcon(QIcon("python.png"))

    #Label Atamları
    label_name = QLabel(win)
    label_name.setText("Name :")
    label_name.move(20,20)
    label_surname = QLabel(win)
    label_surname.setText("Surname :")
    label_surname.move(20,55)
    
    #Text Input Atamaları
    text_name = QLineEdit(win)
    text_name.move(85,20)
    text_name.resize(100,25)
    text_surname = QLineEdit(win)
    text_surname.move(85,55)

    label_name_surname = QLabel(win)
    label_name_surname.move(85, 185)
    label_name_surname.resize(100, 25)
    text_surname.resize(200,25)
    def onClick():
        print("clicked!"+ text_name.text() + text_surname.text())
        label_name_surname.setText("Welcome"+ "  " + text_name.text() + "  " + text_surname.text())

    #Button Ataması
    button_save = QPushButton(win)
    button_save.move(20, 105)
    button_save.setText("Show My Name")
    button_save.clicked.connect(onClick)

    win.show()
    sys.exit(app.exec_( ))

window()