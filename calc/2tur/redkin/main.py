from PyQt5 import uic
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPainter, QColor, QPen, QPixmap
from PyQt5.QtCore import Qt

Form, Window = uic.loadUiType("mainwindow.ui")
app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.setWindowTitle("Diplom")
window.resize(1538, 980)
wid = QWidget()
la = QLabel()
la.setText("ADS")
la.show()




qp = QPainter()
qp.begin(window)
pen = QPen(Qt.black, 2, Qt.SolidLine)
qp.setPen(pen)
qp.drawLine(0, 10, 250, 10)  
qp.end()

x = True
def Putton_One():
    global x
    if x == True:
        a = QPixmap("button.png")
        form.putton_one.setPixmap(a)
        x = False
    else:
        a = QPixmap("exbutton.png")
        form.putton_one.setPixmap(a)
        x = True
form.pushButton_3.clicked.connect(Putton_One)



window.show()
app.exec()



