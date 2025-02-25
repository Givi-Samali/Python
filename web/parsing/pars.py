import requests
import os
from PyQt5 import uic
from PyQt5 import QtWidgets
from bs4 import BeautifulSoup
from PyQt5.QtCore import Qt
from urllib.parse import urljoin  # Добавлено для обработки относительных ссылок

Form, Window = uic.loadUiType("main.ui")
app = QtWidgets.QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.setWindowTitle("Parsing")

OBJECT_LABEL = '''
border-color: rgb(50,50,50);
border-style: solid;
border-width: 1px;
border-radius: 1px;
min-height: 35;
max-height: 35;
'''
OBJECT_PUSH = '''
QPushButton {
border-color: rgb(50,50,50);
border-style: solid;
border-width: 1px;
border-radius: 1px;
min-height: 35;
max-height: 35;
}
QPushButton:hover {
border-color: rgb(50,50,50);
border-style: solid;
border-width: 3px;
border-radius: 1px;
}
'''

form.lineEdit.setStyleSheet(OBJECT_LABEL)
form.pars.setStyleSheet(OBJECT_PUSH)
form.pars_a.setStyleSheet(OBJECT_PUSH)
form.pars_h.setStyleSheet(OBJECT_PUSH)

label = QtWidgets.QLabel()
label.setWordWrap(True)
label.setAlignment(Qt.AlignTop)
label.setOpenExternalLinks(True)

lay = QtWidgets.QVBoxLayout()
form.frame.setLayout(lay)
scroll = QtWidgets.QScrollArea()
scroll.setWidgetResizable(True)
scroll.setWidget(label)
lay.addWidget(scroll)

html_all = ''


def parsing_h():
    label.clear()
    global html_all
    url = form.lineEdit.text()
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Собираем HTML-контент
        html_content = []

        # Заголовки
        headings = soup.find_all('h1')
        html_content.append("<h2>Заголовки:</h2>")
        for heading in headings:
            html_content.append(f"<p>{heading.text.strip()}</p>")
        label.setText("".join(html_content))
        html_all = "".join(html_content)
    except requests.exceptions.RequestException as e:
            label.setText(f"Ошибка: {str(e)}")

def parsing_a():
    label.clear()
    global html_all
    url = form.lineEdit.text()
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Собираем HTML-контент
        html_content = []
        # Ссылки
        links = soup.find_all('a')
        html_content.append("<h2>Ссылки:</h2>")
        for link in links:
            href = link.get('href')
            if href:
                # Преобразуем относительные ссылки в абсолютные
                absolute_url = urljoin(url, href)
                html_content.append(
                    f'<p><a href="{absolute_url}">{link.text.strip() or absolute_url}</a></p>'
                )

        # Устанавливаем весь HTML за один раз
        label.setText("".join(html_content))
        html_all = html_all +  "".join(html_content)
    except requests.exceptions.RequestException as e:
        label.setText(f"Ошибка: {str(e)}")


def pars_all():
    global html_all
    html_all = ""
    parsing_h()
    parsing_a()
    label.setText(html_all)

form.pars.clicked.connect(pars_all)
form.pars_h.clicked.connect(parsing_h)
form.pars_a.clicked.connect(parsing_a)
window.show()
app.exec()