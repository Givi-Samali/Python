import requests
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

OBJECT = '''
border-color: rgb(50,50,50);
border-style: solid;
border-width: 1px;
border-radius: 1px;
min-width: 250;
min-height: 35;
max-width: 250;
max-height: 35;
'''

form.lineEdit.setStyleSheet(OBJECT)
form.pushButton.setStyleSheet(OBJECT)

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


def parsing():
    label.clear()
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

    except requests.exceptions.RequestException as e:
        label.setText(f"Ошибка: {str(e)}")

form.pushButton.clicked.connect(parsing)
window.show()
app.exec()