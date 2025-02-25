import datetime
import time
from PyQt5 import uic
import os
import sys
import subprocess
from PyQt5.QtCore import QProcess
import sqlite3
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMessageBox, QTableWidgetItem, QLabel, QWidget, QBoxLayout

"""class ScrollLabel(QtWidgets.QScrollArea):

    # constructor
    def __init__(self, *args, **kwargs):
        QtWidgets.QScrollArea.__init__(self, *args, **kwargs)

        # making widget resizable
        self.setWidgetResizable(True)

        # making qwidget object
        content = QWidget(self)
        self.setWidget(content)

        # vertical box layout
        lay = QtWidgets.QVBoxLayout(content)

        # creating label
        self.label = QLabel(content)

        # setting alignment to the text
        self.label.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        # making label multi-line
        self.label.setWordWrap(True)

        # adding label to the layout
        lay.addWidget(self.label)

"""
Form, Window = uic.loadUiType("mainwindow.ui")
app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)

form.user.setDisabled(True)
form.cmd.setDisabled(True)
form.window.setDisabled(True)
form.systeminfo.setDisabled(True)

form.label.setWordWrap(True)

#a = QtWidgets.QPushButton
#a.setStyleSheet()
def PROVERKA():
    text = subprocess.check_output('=', shell=True)
    try:
        text.decode('cp866')
        form.label.setText("Ok")
        form.user.setDisabled(False)
        form.user.setStyleSheet("border-color:rgb(0, 255, 0);border-width: 1px;border-style:solid;")
        form.cmd.setDisabled(False)
        form.cmd.setStyleSheet("border-color:rgb(0, 255, 0);border-width: 1px;border-style:solid;")
        form.window.setDisabled(False)
        form.window.setStyleSheet("border-color:rgb(0, 255, 0);border-width: 1px;border-style:solid;")
        form.systeminfo.setDisabled(False)
        form.systeminfo.setStyleSheet("border-color:rgb(0, 255, 0);border-width: 1px;border-style:solid;")
    except:
        form.label.setText("No")

form.proverka.clicked.connect(PROVERKA)

def IFCONFIG():
    text = subprocess.check_output('ipconfig', shell=True)
    form.label.setText(str(text.decode('cp866')))

form.cmd.clicked.connect(IFCONFIG)

def USERS():
    text = subprocess.check_output('net users', shell=True)
    form.label.setText(str(text.decode('cp866')))

form.user.clicked.connect(USERS)

def WINDOW():
    text = subprocess.check_output('ver', shell=True)
    form.label.setText(str(text.decode('cp866')))

form.window.clicked.connect(WINDOW)

def SYSINF():
    text = subprocess.check_output('systeminfo', shell=True)
    form.label.setText(str(text.decode('cp866')))

form.systeminfo.clicked.connect(SYSINF)

def LOGOFF():
    os.system('calc')

form.log.clicked.connect(LOGOFF)

window.show()
app.exec()
