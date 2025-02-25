from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QPropertyAnimation, QPoint

Form, Window = uic.loadUiType("calc.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)

window.setWindowTitle("Calculator")
window.resize(408, 559)

def write(number):
     if form.label.text() == "0":
          form.label.setText(number)
     else:
          form.label.setText(form.label.text() + number)

form.c0.clicked.connect(lambda: write(form.c0.text()))
form.c1.clicked.connect(lambda: write(form.c1.text()))
form.c2.clicked.connect(lambda: write(form.c2.text()))
form.c3.clicked.connect(lambda: write(form.c3.text()))
form.c4.clicked.connect(lambda: write(form.c4.text()))
form.c5.clicked.connect(lambda: write(form.c5.text()))
form.c6.clicked.connect(lambda: write(form.c6.text()))
form.c7.clicked.connect(lambda: write(form.c7.text()))
form.c8.clicked.connect(lambda: write(form.c8.text()))
form.c9.clicked.connect(lambda: write(form.c9.text()))

n1 = ""
n2 = ""
znak = ""
def CE():
     form.label.setText("0")
     form.label_2.setText("")
     global n1, n2, znak
     n1, n2, znak = "", "", ""

form.ce.clicked.connect(CE)

def CC():
     form.label.setText("0")
     global n2
     n2 =  ""

form.cc.clicked.connect(CC)

def DEL():
     text = str(form.label.text())
     form.label.setText(text[:-1])

form.cdel.clicked.connect(DEL)

def plus():
     global n1, znak
     n1 = form.label.text()
     znak = "+"
     form.label.setText("")

form.cp.clicked.connect(plus)

def minus():
     global n1, znak
     n1 = form.label.text()
     form.label.setText("")
     znak = "-"

form.cm.clicked.connect(minus)

def razdel():
     global n1, znak
     n1 = form.label.text()
     form.label.setText("")
     znak = "/"

form.cd.clicked.connect(razdel)

def umnog():
     global n1, znak
     n1 = form.label.text()
     form.label.setText("")
     znak = "*"

form.cu.clicked.connect(umnog)

def comma():
     if form.label.text() == "":
          form.label.setText(form.label.text() + "0.")
     else:
          if "." in form.label.text():
               pass
          else:
               form.label.setText(form.label.text() + ".")


form.ccoma.clicked.connect(comma)
def ravno():
     global n2, n1, znak
     n2 = form.label.text()
     try:
          otv = eval(str(n1) + znak + str(n2))
     except:
          otv = "0"
     if float(otv) % 1 == 0.0:
          form.label.setText(str(int(otv)))
     else:
          form.label.setText(str(otv))

form.cr.clicked.connect(ravno)

def save_file():
     file1 = open("config.txt", "a")
     text = str(form.label.text())
     file1.write(text)
     file1.write("\n")
     file1.close()

form.csave.clicked.connect(save_file)

def read_file():
     file, _ = QtWidgets.QFileDialog.getOpenFileName()
     file1 = open(file, "r")
     text = file1.readline()
     try:
          if float(eval(text)) % 1 == 0.0:
               form.label.setText(str(int(eval(text))))
          else:
               form.label.setText(str(eval(text)))
     except:
          form.label.setText("0")
     file1.close()

form.cread.clicked.connect(read_file)

def rash():
     if form.crash.text() == ">":
          window.resize(608, 559)
          form.label.resize(591, 51)
          form.crash.setText("<")
     else:
          window.resize(408, 559)
          form.label.resize(391, 51)
          form.crash.setText(">")

form.crash.clicked.connect(rash)

window.show()
app.exec()