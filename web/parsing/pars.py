Вот пример кода для выполнения GET-запросов и парсинга сайтов на Python с использованием библиотек `requests` и `BeautifulSoup`.

### 1. Установите необходимые библиотеки
```bash
pip install requests beautifulsoup4
```

### 2. Базовый пример
```python
import requests
from bs4 import BeautifulSoup

# Выполняем GET-запрос к сайту
url = "https://example.com"
try:
    response = requests.get(url)
    
    # Проверяем успешность запроса (статус 200)
    response.raise_for_status()  # Если статус не 200, вызовет исключение
    
    # Парсим HTML-контент страницы
    soup = BeautifulSoup(response.text, 'html.parser')  # 'html.parser' — встроенный парсер Python
    
    # Пример извлечения данных:
    # Найдем все заголовки <h1> на странице
    headings = soup.find_all('h1')
    print("Заголовки на странице:")
    for heading in headings:
        print(heading.text.strip())  # .strip() удаляет лишние пробелы
    
    # Найдем все ссылки <a> на странице
    links = soup.find_all('a')
    print("\nСсылки на странице:")
    for link in links:
        print(f"{link.text.strip()} -> {link.get('href')}")

except requests.exceptions.RequestException as e:
    print(f"Ошибка при выполнении запроса: {e}")
```

---

### Пояснение кода:
1. **GET-запрос через `requests`**:
   - `requests.get(url)` отправляет GET-запрос к указанному URL.
   - `response.text` содержит HTML-код страницы.
   - `response.raise_for_status()` проверяет, был ли запрос успешным (код 200). Если нет, вызывает ошибку.

2. **Парсинг с `BeautifulSoup`**:
   - `BeautifulSoup(response.text, 'html.parser')` создает объект для парсинга HTML.
   - `soup.find_all('тег')` ищет все элементы по указанному тегу (например, `h1`, `a`).
   - `link.get('href')` извлекает значение атрибута `href` из тега `<a>`.

---

### 3. Пример с параметрами запроса и заголовками
Иногда сайты требуют указать заголовки (например, `User-Agent`) или параметры.

```python
import requests

url = "https://httpbin.org/get"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/91.0.4472.124",  # Пример User-Agent
}

params = {
    "key1": "value1",
    "key2": "value2",
}

try:
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    
    # Выведем URL с параметрами и ответ сервера
    print("Полный URL:", response.url)  # https://httpbin.org/get?key1=value1&key2=value2
    print("Ответ сервера (JSON):", response.json())

except requests.exceptions.RequestException as e:
    print(f"Ошибка: {e}")
```

---

### 4. Важные замечания:
1. **Соблюдайте правила сайта**:
   - Проверьте файл `robots.txt` сайта (напр., `https://example.com/robots.txt`).
   - Не отправляйте слишком частые запросы (может привести к блокировке IP).

2. **Обработка ошибок**:
   - Всегда используйте `try-except` для обработки сетевых ошибок.
   - Учитывайте коды ответа (404, 500 и т.д.).

3. **Динамические сайты**:
   - Если сайт использует JavaScript для загрузки данных, потребуются инструменты вроде **Selenium** или **Scrapy**.

---

Это базовая основа для работы с парсингом. Для сложных задач можно добавить:
- Парсинг данных через регулярные выражения (`re`).
- Использование `lxml` для ускорения парсинга.
- Сохранение данных в CSV/JSON.