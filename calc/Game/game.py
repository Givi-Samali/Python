from PyQt5 import uic
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPainter, QColor, QPen, QPixmap
from PyQt5.QtCore import Qt
import threading as th
import time

Form, Window = uic.loadUiType("game.ui")
app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.setWindowTitle("Game")


def start():
    count = 0
    while True:
        count += 1
        time.sleep(1)
        print(count)


def V():
    th1 = th.Thread(target=start())
    th1.start()

V()

window.show()
app.exec()



