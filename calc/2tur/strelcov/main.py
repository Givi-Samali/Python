from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5 import uic

Form, Window = uic.loadUiType("index.ui")
app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)

form.comboBox.addItems(["X", "1", "2", "3"])

form.comboBox_2.addItems(["X", "1", "2", "3", "4", "5", "6", "7", "8"])

form.pushRub_1.hide()
form.pushRub_2.hide()
form.pushRub_3.hide()
form.pushRub_4.hide()
form.pushRub_5.hide()
form.pushRub_6.hide()
form.pushRub_7.hide()
form.pushRub_8.hide()

def RUBEZ():
    pixmap = QPixmap(form.comboBox.currentText() + ".png")
    form.label_2.setPixmap(pixmap)

form.comboBox.currentTextChanged.connect(RUBEZ)

def UCHASTKI():
    if form.comboBox_2.currentText() == "1":
        form.pushRub_1.show()
        form.pushRub_2.hide()
        form.pushRub_3.hide()
        form.pushRub_4.hide()
        form.pushRub_5.hide()
        form.pushRub_6.hide()
        form.pushRub_7.hide()
        form.pushRub_8.hide()
    elif form.comboBox_2.currentText() == "2":
        form.pushRub_1.show()
        form.pushRub_2.hide()
        form.pushRub_3.hide()
        form.pushRub_4.hide()
        form.pushRub_5.show()
        form.pushRub_6.hide()
        form.pushRub_7.hide()
        form.pushRub_8.hide()
    elif form.comboBox_2.currentText() == "3":
        form.pushRub_1.hide()
        form.pushRub_2.show()
        form.pushRub_3.hide()
        form.pushRub_4.show()
        form.pushRub_5.hide()
        form.pushRub_6.hide()
        form.pushRub_7.show()
        form.pushRub_8.hide()
    elif form.comboBox_2.currentText() == "4":
        form.pushRub_1.show()
        form.pushRub_2.hide()
        form.pushRub_3.show()
        form.pushRub_4.hide()
        form.pushRub_5.show()
        form.pushRub_6.hide()
        form.pushRub_7.show()
        form.pushRub_8.hide()
    elif form.comboBox_2.currentText() == "5":
        form.pushRub_1.show()
        form.pushRub_2.show()
        form.pushRub_3.show()
        form.pushRub_4.show()
        form.pushRub_5.show()
        form.pushRub_6.hide()
        form.pushRub_7.hide()
        form.pushRub_8.hide()
    elif form.comboBox_2.currentText() == "6":
        form.pushRub_1.show()
        form.pushRub_2.show()
        form.pushRub_3.show()
        form.pushRub_4.show()
        form.pushRub_5.show()
        form.pushRub_6.show()
        form.pushRub_7.hide()
        form.pushRub_8.hide()
    elif form.comboBox_2.currentText() == "7":
        form.pushRub_1.show()
        form.pushRub_2.show()
        form.pushRub_3.show()
        form.pushRub_4.show()
        form.pushRub_5.show()
        form.pushRub_6.show()
        form.pushRub_7.show()
        form.pushRub_8.hide()
    elif form.comboBox_2.currentText() == "8":
        form.pushRub_1.show()
        form.pushRub_2.show()
        form.pushRub_3.show()
        form.pushRub_4.show()
        form.pushRub_5.show()
        form.pushRub_6.show()
        form.pushRub_7.show()
        form.pushRub_8.show()
    else:
        msg = QMessageBox()
        msg.setWindowTitle("Ошибка ")
        msg.setText("Неверный количество")
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()

form.comboBox_2.currentTextChanged.connect(UCHASTKI)


window.show()
app.exec()

