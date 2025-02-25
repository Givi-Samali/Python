from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QHeaderView, QMessageBox
import sqlite3

Form, Window = uic.loadUiType("pro.ui")
app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)

conn = sqlite3.connect('data_base.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS data_base (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                PU TEXT,
                PRO TEXT,
                OP TEXT)""")
conn.commit()

def add_data_PU(PU):
    sPU = f'{PU[0]}, {PU[1]}, {PU[2]}'
    cur.execute('INSERT INTO data_base (PU) VALUES (?)', (sPU,))
    conn.commit()
    update_table()

form.D_PU.clicked.connect(lambda: add_data_PU([form.PU_X.text(), form.PU_Y.text(), form.PU_R.text()]))

def add_data_PRO(PRO):
    sPRO = f'{PRO[0]}, {PRO[1]}, {PRO[2]}'
    cur.execute('INSERT INTO data_base (PRO) VALUES (?)', (sPRO,))
    conn.commit()
    update_table()

form.D_PRO.clicked.connect(lambda: add_data_PRO([form.PRO_X.text(), form.PRO_Y.text(), form.PRO_R.text()]))

def add_data_OP(OP):
    sOP = f'{OP[0]}, {OP[1]}'
    cur.execute('INSERT INTO data_base (OP) VALUES (?)', (sOP,))
    conn.commit()
    update_table()

form.D_OP.clicked.connect(lambda: add_data_OP([form.OP_X.text(), form.OP_Y.text()]))



def remove_data():
    try:
        j = form.tableWidget.currentRow()
        id = int(form.tableWidget.item(j, 0).text())
        cur.execute('DELETE FROM data_base WHERE id =?', (id,))
        conn.commit()
        update_table()
    except:
        error_massage("Ошибка", "Невозможно удалить")


form.CLEAR_2.clicked.connect(remove_data)

def error_massage(x, y):
    msg = QMessageBox()
    msg.setWindowTitle(f"{x}")
    msg.setText(f"{y}")
    msg.setIcon(QMessageBox.Warning)
    msg.exec_()


def check_massage(x, y):
    msg = QMessageBox()
    msg.setWindowTitle(f"{x}")
    msg.setText(f"{y}")
    msg.setIcon(QMessageBox.Information)
    msg.exec_()


def update_table():
    form.tableWidget.setColumnCount(4)
    form.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    form.tableWidget.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem('ID'))
    form.tableWidget.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem('ПУ(x, y, дальность'))
    form.tableWidget.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem('ПРО(x, y, радиус'))
    form.tableWidget.setHorizontalHeaderItem(3, QtWidgets.QTableWidgetItem('ОП(x, y'))
    form.tableWidget.verticalHeader().setDefaultSectionSize(20)
    form.tableWidget.horizontalHeader().setDefaultSectionSize(60)
    form.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Fixed)
    form.tableWidget.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Fixed)

    bd = cur.execute('SELECT * FROM data_base').fetchall()
    form.tableWidget.setRowCount(len(bd))
    for i in range(len(bd)):
        for j in range(len(bd[i])):
            form.tableWidget.setItem(i, j, QTableWidgetItem(str(bd[i][j])))


def rashet():
    pass

def bd():
    pass

def clear():
    pass

def delite():
    pass

update_table()

window.show()
app.exec()