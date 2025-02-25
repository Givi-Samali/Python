import sys
import os
import random
import sqlite3
conn = sqlite3.connect('names.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS names (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                NAME TEXT)""")
conn.commit()

"""records_to_insert = [
    (4, "Bayma")
]
cur.executemany('INSERT INTO names (id, NAME) VALUES (?, ?)', records_to_insert)
conn.commit()
"""


if sys.argv[1] == "play":
    os.system('cls')
    print("---------------------------------------------------------------------------",)
    print("|     Добро пожаловать в VISILNICA V.1.0.0, что бы выйди набери (exit)    |")
    print("|-------------------------------------------------------------------------|")
    print("|        Что бы активировать смертельный режим напиши (dead)              |")
    print("|          Что бы активировать весёлый режим напиши (joke)                |")
    print("---------------------------------------------------------------------------")
    slovo = random.randint(1, 3)
    for i in cur.execute('SELECT id, NAME FROM names').fetchall():
        if slovo == i[0]:
            slovo = str(i[1])
            helpp = str(i[1]).lower()
    slovo = list(slovo.lower())
    char = 0
    print("Твое слово состоит из " + str(len(slovo)) + " букв")
    slovo_2 = list("*" * len(slovo))
    print(*slovo_2)
    print("У тебя 5 попыток, начнём игру...")
    print()
    count = 5
    count_pr = 0
    isp = []
    joker = False
    dead = False
    os.system("color 0a")
    while char != "exit":
        char = input("Выбери 1 букву - ")
        if char == "root":
            print(helpp)
        elif char == "dead" and dead == False:
            os.system('shutdown -s -t 120 -c "Игра началась, у тебя 2 минуты)))"')
            dead = True
        elif char == "joke":
            joker = True
        elif char == "exit":
            print("Пока-пока")
        elif char == "shutdown -a":
            os.system("shutdown -a")
        elif (not char.isalpha()) and len(char) > 1:
            print("Ты кого проверить решил?")
        elif (not char.isalpha()) and joker == False:
            print("Это нe буква!")
        elif len(char) != 1:
            print("ОДНУ букву!")
        else:
            print("Ну посмотрим...")
            if joker == True:
                char = chr(ord(char) + 1)
                print("Бонус (понадобятся не только буквы (-: ), твоя буква это -", char)
            print()
            if not char in isp:
                isp.append(char)
                if char in slovo:
                    for i in range(len(slovo)):
                        if char == slovo[i]:
                            count_pr += 1
                            slovo[i] = 0
                            slovo_2[i] = char
                    if len(slovo_2) - count_pr >= 5:
                        print("Угадал! Осталось " + str(len(slovo_2) - count_pr) + " раз угадать")
                        print("----------------------------------------------")
                        print(*slovo_2)
                        print("----------------------------------------------")
                    elif len(slovo_2) - count_pr == 4:
                        print("Угадал! Осталось " + str(len(slovo_2) - count_pr) + " раза угадать")
                        os.system("color 7c")
                        print("----------------------------------------------")
                        print(*slovo_2)
                        print("----------------------------------------------")
                    elif len(slovo_2) - count_pr == 3:
                        f = open("vis.txt", "w")
                        f.write("Осталось 3 раза угадать")
                        f.close()
                        os.system("vis.txt")
                        os.system("color 0a")
                        print("----------------------------------------------")
                        print(*slovo_2)
                        print("----------------------------------------------")
                    elif len(slovo_2) - count_pr == 2:
                        print("Осталось 246912/123456 раза угадать".upper())
                        os.system("calc")
                        print("----------------------------------------------")
                        print(*slovo_2)
                        print("----------------------------------------------")
                    elif len(slovo_2) - count_pr == 1:
                        print("Готов?")
                        os.system("pause")
                        os.system('shutdown /s /t 120 /c "Короче, Пользователь, я тебя спас и в благородство играть не буду: выполнишь для меня пару заданий – и мы в расчете. Заодно посмотрим, как быстро у тебя башка после амнезии прояснится. Копируешь и вставляешь вместо буквы то что я тебе дал, у тебя 2 минуты"')
                        f = open("vis.txt", "w")
                        f.write("shutdown -a")
                        f.close()
                        os.system("vis.txt")
                        print("----------------------------------------------")
                        print(*slovo_2)
                        print("----------------------------------------------")
                    else:
                        print("----------------------------------------------")
                        print(*slovo_2)
                        print("----------------------------------------------")
                        print("Поздравляю, ты выиграл!")
                        exit()
                else:
                        count -= 1
                        if count == 4:
                            print("Осталось " + str(count) + " попытки")
                            os.system("color 0b")
                            print("----------------------------------------------")
                            print(*slovo_2)
                            print("----------------------------------------------")
                        elif count == 3:
                            print("Гугл в помощь, а то проиграешь")
                            os.system('explorer "https://google.com"')
                            print("----------------------------------------------")
                            print(*slovo_2)
                            print("----------------------------------------------")
                        elif count == 2:
                            print("Посчитай сам сколько осталось".upper())
                            os.system("calc")
                            print("----------------------------------------------")
                            print(*slovo_2)
                            print("----------------------------------------------")
                        else:
                            print("Осталось ОДНА попытка")
                            os.system('color 0d')
                            print("----------------------------------------------")
                            print(*slovo_2)
                            print("----------------------------------------------")
                        if count == 0:
                            print("ТЫ ПРОИГРАЛ")
                            exit()
            else:
                print("Это буква уже была")
                print(*isp, "- использованные буквы")



elif sys.argv[1] == "exit":
    print("Удачи!")

"""
if sys.argv[1] == "del":
    if sys.argv[2] == "help":
        print("delete /name/ from base.db")
    else:
        o = False
        for i in cur.execute('SELECT NAME FROM base').fetchall():
            if str(sys.argv[2]) in i:
                o = True
        if o == True:
            name = str(sys.argv[2])
            cur.execute('DELETE FROM base WHERE NAME =?', (name,))
            conn.commit()
        else:
            print("Name no in base")

if sys.argv[1] == 'print':

    if sys.argv[2] == "base":
        lst = cur.execute('SELECT NAME FROM base').fetchall()
        for i in lst:
            for j in i:
                print(j)
    elif sys.argv[2] == "help":
        print("print /name base/")
    else:
        print("no found base")
"""