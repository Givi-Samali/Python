from PyQt5 import uic, QtWidgets
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication
import sqlite3

Form, Window = uic.loadUiType("sql.ui")
app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)


db = sqlite3.connect('data.db')
query = """
CREATE TABLE if not exists BOOKS
(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
FIRSTNAME TEXT NO NULL,
NAME TEXT NO NULL,
LASTNAME TEXT NO NULL,
GRUP INTEGER NO NULL
)
"""
cur = db.cursor()
cur.execute(query)
def but():
    NAME = str(form.lineEdit.text())
    fname, name, lname = NAME.split()
    query = """
        INSERT INTO BOOKS(FIRSTNAME, NAME, LASTNAME, GRUP)
        VALUES (?,?,?,?)
        """
    cur = db.cursor()
    cur.execute(query, (fname, name, lname, 5))
    db.commit()
    db.close()

form.pushButton.clicked.connect(but)

window.show()
app.exec()