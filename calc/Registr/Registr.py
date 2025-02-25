from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QHeaderView, QMessageBox
from PyQt5.QtCore import QPropertyAnimation, QRect, QPoint, QEasingCurve
import sqlite3

Form, Window = uic.loadUiType("untitled.ui")
app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.resize(461, 351)
form.frame_2.move(0, 0)
form.frame_2.hide()
form.spinBox.setRange(18, 99)


conn = sqlite3.connect('users.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                UZ TEXT,
                age INTEGER,
                type_komand TEXT)""")
conn.commit()

AGE = []
AGE_I = []
def add_user():
    name = form.lineEdit_name.text()
    UZ = form.lineEdit_uz.text()
    age = form.spinBox.value()
    AGE.append(age)
    if age not in AGE_I:
        AGE_I.append(age)
    if form.osnova.isChecked():
        type_komand = "Основа"
    elif form.profil.isChecked():
        type_komand = "Профиль"

    if form.profil.isChecked() or form.osnova.isChecked():
        if name != '' and UZ != '' and age != 0 and type_komand != '':
            cur.execute('INSERT INTO users (name, UZ, age, type_komand) VALUES (?, ?, ?, ?)', (name, UZ, age, type_komand,))
            conn.commit()
            check_massage()
        else:
            error_massage()
    else:
        error_massage()

form.ADD.clicked.connect(add_user)
def error_massage():
    msg = QMessageBox()
    msg.setWindowTitle("Ошибка")
    msg.setText("Введите правильные данные")
    msg.setIcon(QMessageBox.Warning)
    msg.exec_()


def check_massage():
    msg = QMessageBox()
    msg.setWindowTitle("Добавление в БД")
    msg.setText("Успешно!")
    msg.setIcon(QMessageBox.Information)
    msg.exec_()


def remove_user():
    row = form.tableWidget.currentRow()
    form.tableWidget.removeRow(row)
    id = form.tableWidget.currentRow()
    try:
        lst_id = cur.execute('SELECT id FROM users').fetchall()
        id = int(id)
        if id in lst_id:
            cur.execute('DELETE FROM users WHERE id = ?', (id,))
            conn.commit()
            update_table()
    except:
        error_massage()



def update_table():
    form.tableWidget.setColumnCount(5)
    form.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    form.tableWidget.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem('ID'))
    form.tableWidget.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem('ФИО'))
    form.tableWidget.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem('Учебное Заведение'))
    form.tableWidget.setHorizontalHeaderItem(3, QtWidgets.QTableWidgetItem('Возраст'))
    form.tableWidget.setHorizontalHeaderItem(4, QtWidgets.QTableWidgetItem('Команда'))
    form.tableWidget.verticalHeader().setDefaultSectionSize(20)
    form.tableWidget.horizontalHeader().setDefaultSectionSize(60)
    form.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Fixed)
    form.tableWidget.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Fixed)

    bd = cur.execute('SELECT * FROM users').fetchall()
    form.tableWidget.setRowCount(len(bd))
    for i in range(len(bd)):
        for j in range(len(bd[i])):
            form.tableWidget.setItem(i, j, QTableWidgetItem(str(bd[i][j])))
def BD():
    window.resize(641, 551)
    form.frame.hide()
    form.frame_3.hide()
    form.frame_2.show()
    update_table()

def Back():
    window.resize(461, 351)
    form.frame_2.hide()
    form.frame_3.show()
    form.frame.show()


def GRAPH():
    window.resize(960, 351)
    form.graph_2.setText("У\n\nБ\n\nР\n\nА\n\nТ\n\nЬ")
    grid = QtWidgets.QGridLayout()
    grid.addWidget(form.frame_3, 0, 0)
    form.frame_3.move(460, 5)
    X = []
    AGE_I.sort()
    for i in range(len(AGE_I)):
        X.append(AGE.count(AGE_I[i]))
    form.frame_3.plot(x=AGE_I, y=X)

def GRAPH_2():
    window.resize(461, 351)

form.graph_2.clicked.connect(GRAPH_2)
form.graph.clicked.connect(GRAPH)
form.Back.clicked.connect(Back)
form.BD.clicked.connect(BD)
form.pushButton.clicked.connect(remove_user)

window.show()
app.exec()