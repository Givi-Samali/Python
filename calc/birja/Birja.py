from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QTreeWidget
from PyQt5.QtCore import QPropertyAnimation, QRect, QPoint, QEasingCurve
import pyqtgraph as pg
import random
import threading as th
import time

Form, Window = uic.loadUiType("birja.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
count = [0] * 11

y1 = list(range(100))
plt1 = pg.plot(x = [], y = [0])
form.verticalLayout.addWidget(plt1)
def program(y1):
    x1 = [0]
    for i in range(100):
        time.sleep(1)
        znahenie = random.randint(0, 10)
        if znahenie == 0:
            count[0] += 1
        elif znahenie == 1:
            count[1] += 1
        elif znahenie == 2:
            count[2] += 1
        elif znahenie == 3:
            count[3] += 1
        elif znahenie == 4:
            count[4] += 1
        elif znahenie == 5:
            count[5] += 1
        elif znahenie == 6:
            count[6] += 1
        elif znahenie == 7:
            count[7] += 1
        elif znahenie == 8:
            count[8] += 1
        elif znahenie == 9:
            count[9] += 1
        elif znahenie == 10:
            count[10] += 1
        x1.append(znahenie)
        plt1.plot(x = y1[:i+1], y=x1[:i+1])
        print(count)
def start():
    th1 = th.Thread(target=program, args = (y1,))
    th1.start() 

start()

form.tree = QtWidgets().QTreeWidget(form).setGeometry(150,300,50,50)
form.tree.setStyleSheet('background-color: black;')
window.show()
app.exec()
