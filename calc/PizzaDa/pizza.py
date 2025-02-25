from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
import sqlite3
import pyqtgraph as pg
from PyQt5.QtWidgets import QApplication, QGraphicsEllipseItem, QGraphicsLineItem

Form, Window = uic.loadUiType("PizzaDa.ui")
app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)

conn = sqlite3.connect('database.db')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS pizza (id INTEGER PRIMARY KEY AUTOINCREMENT,'
            'diametr INTEGER,'
            'friends INTEGER,'
            'ploshad FLOAT)')
conn.commit()

plt1 = pg.plot()
plt1.setBackground('w')
plt1.getPlotItem().hideAxis('bottom')
plt1.getPlotItem().hideAxis('left')
form.verticalLayout.addWidget(plt1)
circle = QGraphicsEllipseItem(0 - (5/2),0 - (5/2),5,5)
circle.setBrush(pg.mkBrush((255,255,0)))
circle.setPen(pg.mkPen((255,255,0)))
plt1.addItem(circle)
def add_db(diametr, friends, ploshad):
    cur.execute('INSERT INTO pizza (diametr, friends, ploshad) VALUES (?,?,?)', (diametr, friends, ploshad))
    conn.commit()

def ploshad(diametr, friends):
    o_pld = 3.14 * (diametr / 2)**2
    f_ploshad = o_pld / friends
    return round(f_ploshad, 2)


form.spinBox.setRange(1, 100)
form.ploshad.hide()
form.lineEdit.setInputMask("00;_")
def slize():
    if str(form.lineEdit.text()) == "" or int(form.lineEdit.text()) == 0:
        form.ploshad.setText("Введите корректные значения")
        form.ploshad.show()
    else:
        add_db(int(form.lineEdit.text()), int(form.spinBox.value()), float(ploshad(int(form.lineEdit.text()), int(form.spinBox.value()))))

        if int(form.spinBox.value()) != 1:
            pizza_add(5, int(form.spinBox.value()))
        form.ploshad.setText("Итоговая площадь: " + str(ploshad(int(form.lineEdit.text()), int(form.spinBox.value()))) + " см^2")
        form.ploshad.show()

def clear():
    print(str(form.lineEdit.text()))
    form.spinBox.setValue(0)
    form.lineEdit.setText("")
    form.ploshad.hide()
    plt1.clear()
    plt1.setBackground('w')
    plt1.getPlotItem().hideAxis('bottom')
    plt1.getPlotItem().hideAxis('left')
    circle = QGraphicsEllipseItem(0 - (5 / 2), 0 - (5 / 2), 5, 5)
    circle.setBrush(pg.mkBrush((255, 255, 0)))
    circle.setPen(pg.mkPen((255, 255, 0)))
    plt1.addItem(circle)



def pizza_add(d, count_people):
    circle = QGraphicsEllipseItem(0 - (d/2),0 - (d/2),d,d)
    circle.setBrush(pg.mkBrush((255,255,0)))
    circle.setPen(pg.mkPen((255,255,0)))
    plt1.addItem(circle)
    f = 360 / count_people
    a = 0
    for i in range(count_people):
        line = QGraphicsLineItem(0, 0, 0, d/2)
        line.setPen(pg.mkPen(width=2, color='black'))
        line.setRotation(a)
        plt1.addItem(line)
        a += f


form.Slize.clicked.connect(slize)
form.Clear.clicked.connect(clear)

window.show()
app.exec()