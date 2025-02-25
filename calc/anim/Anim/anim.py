from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QFrame,  QTreeWidget, QTreeWidgetItem
from PyQt5.QtCore import QPropertyAnimation, QRect, QPoint, QEasingCurve

Form, Window = uic.loadUiType("anim.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
grid = QtWidgets.QGridLayout()
grid.addWidget(form.widget, 0, 0)
form.widget.plot(x = [0, 2], y = [0, 2])
form.widget.plot(x = [0, 0], y = [0, 3])

grid1 = QtWidgets.QGridLayout()
grid1.addWidget(form.widget_2, 0, 0)
form.widget_2.plot(x = [0, 1, 2, 4], y = [4, 10, 9, 6])

main = QtWidgets.QWidget()
main.resize(500, 500)
f = QtWidgets.QPushButton(main)
f.setText("TEST")
def test():

anim = QPropertyAnimation(form.pushButton, b"pos")
def ANIM():
    anim.setEasingCurve(QEasingCurve.OutBounce)
    anim.setDuration(3000)
    anim.setStartValue(QPoint(0, 0))
    anim.setEndValue(QPoint(500, 500))
    anim.start()
    main.show()
form.pushButton.clicked.connect(ANIM)

tree = QTreeWidget(main)
tree.setGeometry(0,100,100,100)
#form.tree.setColumnCount(1)

root = QTreeWidgetItem(tree)
root.setText(0, "One")

root1 = QTreeWidgetItem(root)
root1.setText(0, "Onee")

tree.expandAll()

tree.show()

window.show()
app.exec()