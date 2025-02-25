from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication
import pyqtgraph as pg
import sqlite3

Form, Window = uic.loadUiType("Calendar.ui")
app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.setWindowTitle("Calendar")
window.resize(1061, 641)
form.frame_2.hide()
form.frame_2.move(0, 0)




# DATA = '2024-01-28' !!!

conn = sqlite3.connect('tasks.db')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, '
            'created_at DATETIME DEFAULT CURRENT_TIMESTAMP, '
            'task TEXT, date DATE)')
conn.commit()

def add_task_bd_():
    task = form.textEdit.toPlainText()
    date = form.calendarWidget.selectedDate().toString('yyyy-MM-dd')
    cur.execute('INSERT INTO tasks (task, date) VALUES (?, ?)', (task, date))
    conn.commit()
    posible(sort_tasks_for_graph())
form.pushButton_dobav.clicked.connect(add_task_bd_)
def del_task_bd(id):
    cur.execute('DELETE FROM tasks WHERE id =?', (id,))
    conn.commit()
    for i in range(len(sort_tasks_for_list())+1):
        form.formLayout.removeRow(0)
    per()

def sort_tasks_for_graph():
    tasks_for_graph = cur.execute("""SELECT date, COUNT(*) AS count_of_records FROM tasks
                                  GROUP BY date
                                  ORDER BY date""").fetchall()
    return tasks_for_graph

def sort_tasks_for_list():
    tasks_for_list = cur.execute('SELECT * FROM tasks ORDER BY created_at').fetchall()
    return tasks_for_list

def update_task(id):
    print(id)
    # cur.execute('UPDATE tasks SET task =?, date =? WHERE id =?', (task, date, id))
    # conn.commit()


def per():
    form.frame.hide()
    form.labellist = []
    form.combolist = []
    bsa_lst = sort_tasks_for_list()
    for i in range(len(bsa_lst)):
        text_1 = QtWidgets.QLabel(f"Создана:{bsa_lst[i][1]}\n")
        text_1.setObjectName(f'text_1_{bsa_lst[i][0]}')
        text_2 = QtWidgets.QLineEdit(f"Назначена:{bsa_lst[i][3]}\n")
        text_2.setInputMask('Назначена: 0000-00-00')
        text_2.setObjectName(f'text_2_{bsa_lst[i][0]}')
        text = QtWidgets.QTextEdit(f"Описание:{bsa_lst[i][2]}")
        text.setObjectName(f'text_{bsa_lst[i][0]}')
        lay_left = QtWidgets.QWidget()
        vbox = QtWidgets.QVBoxLayout(lay_left)
        vbox.addWidget(text_1)
        vbox.addWidget(text_2)
        vbox.addWidget(text)

        text.setFixedSize(600, 150)
        form.labellist.append(lay_left)
        t = QtWidgets.QPushButton("Изменить")
        t.setObjectName(f't{bsa_lst[i][0]}')
        t.clicked.connect(lambda: update_task(t.objectName()[1:]))
        t.setFixedSize(100, 40)
        s = QtWidgets.QPushButton("Удалить")
        s.clicked.connect(lambda: del_task_bd(bsa_lst[i][0]))
        s.setFixedSize(100, 40)
        lay = QtWidgets.QVBoxLayout()
        lay.addStretch(1)
        lay.addWidget(t)
        lay.addWidget(s)
        form.combolist.append(lay)
        form.formLayout.addRow(form.labellist[i], form.combolist[i])

    form.frame_2.show()

plt1 = pg.plot()
plt1.showGrid(x = True, y = True)
form.verticalLayout.addWidget(plt1)

def posible(lst):
    plt1.clear()
    x, y = [], []
    l = 1
    for i in lst:
        x.append(l)
        y.append(i[1])
        text = pg.TextItem(i[0])
        text.setPos(l + 0.5 , 0)
        plt1.addItem(text, ignoreBounce = True)
        l += 1
    x.append(l)
    plt1.plot(x, y, stepMode=True, fillLevel = 0, brush = (0, 0, 255))

# posible([('1.03.2024', 7), ('2.03.2024', 3), ('3.03.2024', 5)])
form.pushButton_perehod.clicked.connect(per)


def per2():
    form.frame_2.hide()
    form.frame.show()
    posible(sort_tasks_for_graph())

form.pushButton_perehod2.clicked.connect(per2)
posible(sort_tasks_for_graph())

window.show()
app.exec()