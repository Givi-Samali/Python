from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

Form, Window = uic.loadUiType("ItZoo.ui")
app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)

window.setWindowTitle("ItZoo")
form.comboBox.addItems(["Млекопитающие", "Рептилии", "Рыбы", "Земноводные", "Птицы"])
form.frame_2.hide()
form.frame_2.move(0, 0)
window.resize(879, 461)


def new_window():
    form.frame.hide()
    form.frame_2.show()


form.izm.clicked.connect(new_window)


def new_window_2():
    form.frame_2.hide()
    form.frame.show()


form.dobav_val.clicked.connect(new_window_2)

window.show()
app.exec()