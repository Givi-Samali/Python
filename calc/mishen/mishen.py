from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox, QGraphicsEllipseItem
import pyqtgraph as pg
import random
import sqlite3
import threading
import time, math
Form, Window = uic.loadUiType("mishen.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
count = 0
form.progressBar.setRange(0, 100)
form.progressBar.setValue(0)
con = sqlite3.connect('database.db')
cur = con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                score INTEGER)""")
con.commit()

def add_score(name, score):
    cur.execute('INSERT INTO results (name, score) VALUES (?, ?)', (name, score))
    con.commit()

def lider_bord():
    lst = cur.execute('SELECT * FROM results ORDER BY score DESC LIMIT 10').fetchall()
    row_name = ''
    for i in range(len(lst)):
        row_name += f'{i+1}. ' + lst[i][1] + '\n'
    row_scores = ''
    for i in range(len(lst)):
        row_scores += str(lst[i][2]) + '\n'
    return [row_name, row_scores]


graphick = pg.plot()
form.verticalLayout.addWidget(graphick)
graphick.getPlotItem().hideAxis('bottom')
graphick.getPlotItem().hideAxis('left')
graphick.setBackground('w')
form.label.setText(lider_bord()[0])
form.label_3.setText(lider_bord()[1])
def set_mish():
    circle = [[0,0,1,'10', 0], [0,0,2, '9', 1.5], [0,0,3, '8', 2.5], [0,0,4, '7',3.5], [0,0,5, '6', 4.5], [0,0,6, '5', 5.5], [0,0,7, '4',6.5], [0,0,8, '3',7.5], [0,0,9, '2',8.5], [0,0,10, '1',9.5]]
    circle.reverse()
    for i in circle:
        x, y, r, txt, b = i[0], i[1], i[2], i[3], i[4]
        kryg = QGraphicsEllipseItem(x - (r/2), y - (r/2), r,r)
        kryg.setPen(pg.mkPen((0,0,0)))
        graphick.addItem(kryg)
        if txt != '10':
            p1 = b
            p2 = -b
            zero = 0.55
            xy = [(zero, p1 * 1.3 + 0.5), (p1 * 2.17 + 0.5 , zero), (zero, p2 * 1.3 + 0.5), (p2 * 2.17 + 0.5, zero)]
            for i in xy:
                textic = pg.TextItem(text = txt, color = (0,0,0), anchor= i)
                graphick.addItem(textic)
        else:
            textic = pg.TextItem(text = '10', color= (0,0,0), anchor= (0.5, 0.5))
            graphick.addItem(textic)
def create_lst():
    tlst = []
    for i in range(5):
        tlst.append([random.randint(-500, 500)/100, random.randint(-500, 500)/100])
    return tlst

score = 0
def setCon():
    global score, count
    lst = create_lst()
    #print(lst)
    radius = [0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5]
    for i in lst:
        x = i[0]
        y = i[1]
        r = 0.1
        vistrel = QGraphicsEllipseItem(x - (r / 2), y - (r / 2), r, r)
        vistrel.setPen(pg.mkPen((255, 255, 255)))
        vistrel.setBrush(pg.mkBrush((255, 0, 0)))
        graphick.addItem(vistrel)
        ranrad = math.sqrt(math.pow(x, 2) + math.pow(y, 2))
        for i in range(len(radius)- 1):
            r1 = radius[i]
            r2 = radius[i+1]
            if ranrad == 0:
                score += 100
                break
            elif r1 <= ranrad <= r2:
                score += 10 - i
                #print(score, 10 - i, x,y, ranrad)
                break
            else:
                continue
        else:
            #print(score, "мазила", x, y, ranrad)
            score += 0
        count += 20
        form.progressBar.setValue(count)
        time.sleep(1.5)
        graphick.hide()
        graphick.show()
    form.label_4.setText("Ваш результат: " + str(score))





def start():
    global count
    if form.lineEdit.text() == "":
        warning = QMessageBox()
        warning.setIcon(QMessageBox.Warning)
        warning.setText("Введите свою фамилию")
        warning.setWindowTitle("WARNING")
        warning.exec_()
    else:
        global score
        score = 0
        graphick.clear()
        set_mish()
        th = threading.Thread(target=setCon)
        th.start()
        th.join()
        add_score(form.lineEdit.text(), score)
        form.progressBar.setValue(0)
        count = 0
        form.label.setText(lider_bord()[0])
        form.label_3.setText(lider_bord()[1])


set_mish()
form.pushButton.clicked.connect(start)




app.exec()
