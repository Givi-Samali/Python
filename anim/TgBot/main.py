class Person:
    def __init__(self, age):
        self.age = age
        self.age = 30
person = Person(25).age
person['age'] = 30

print(Person)
print(person)
'''
import lxml
from bs4 import BeautifulSoup
import requests
import telebot




bot = telebot.TeleBot('7358848011:AAFRW09Z_3pcnimB-JHNZ13-VKx4MYwAgRg');

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, отправь мне URL")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    elif 'https://zoloto585.ru/' in message.text:
        url = message.text
        response = requests.get(url)
        bs = BeautifulSoup(response.text, "lxml")
        temp = bs.find('div', class_='prices__value')
        temp_1 = bs.find('h1', class_='product-page__name')
        otv = temp_1.text + '\n' + temp.text
        bot.send_message(message.from_user.id, otv)
    elif 'https://sunlight.net/' in message.text:
        url = message.text
        response = requests.get(url)
        bs = BeautifulSoup(response.text, "lxml")
        temp = bs.find('div', class_='supreme-product-card__price-discount-price')
        temp_1 = bs.find('h1', class_='supreme-product-card__info-name-title')
        otv = str(temp_1.text).replace('\n', '') + '\n' +  str(temp.text).replace('\n', '')
        cost = str(temp.text).replace('₽', '')
        cost = cost.replace('\n', '')

        cost = cost.replace(' ', '')
        cost = cost.replace('\u202f', '')
        cost = cost.replace('\xa0', '')
        otv_2 = round(int(cost) - ((int(cost)/100)*20))

        bot.send_message(message.from_user.id, otv)
        bot.send_message(message.from_user.id, 'Ваша новая цена: ' + str(otv_2) + ' ₽')
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
bot.polling(none_stop=True, interval=0)'''




