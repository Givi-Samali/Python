from PyQt5 import uic
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt

Form, Window = uic.loadUiType("mainwindow.ui")
app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.setWindowTitle("Diplom")


qp = QPainter()
qp.begin(window)
pen = QPen(Qt.black, 2, Qt.SolidLine)
qp.setPen(pen)
qp.drawLine(0, 10, 250, 10)  
qp.end()


window.show()
app.exec()



