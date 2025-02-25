import sys
import sqlite3
ar = sys.argv[1:]

conn = sqlite3.connect("BD.db")
cur = conn.cursor()
cur.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
age INTEGER,
login TEXT,
pswd TEXT,
href TEXT,
login_h TEXT,
pswd_h TEXT,
vhod INTEGER
)
''')
conn.commit()

if "help" in ar:
    print('Напишите "BD", что бы отобразить БД')
    print('Введите "login", что бы войти в систему')
    print('Введите "registr", что бы зарегистрироваться')
    print('Напишите "addhref", что бы добавить сайт')
if ar[0].lower() == "registr":
    cur.execute('SELECT login FROM Users')
    Users = cur.fetchall()
    print("Введите ваш логин")
    Login = input()
    for user in Users:
        if str(user) == Login:
            print("Данный пользователь уже существует")
            exit()
    print("Введите сколько вам лет")
    Age = int(input())
    print('Придумайте пароль')
    Pswd = input()
    cur.execute('INSERT INTO Users (login, age, pswd) VALUES (?,?,?)', (Login, Age, Pswd))
    conn.commit()
    print('Для входа в систему введите "login"')
    exit()
if ar[0].lower() == "login":
    cur.execute('SELECT login,pswd FROM Users')
    Users = cur.fetchall()
    for i in Users:
        print(i)
    print("Введите логин")
    Login = input()
    try:
        if Login not in Users[0]:
            print("Данного пользователя не существует")
            exit()
    except:
        print("Данного пользователя не существует")
        exit()
    print("Введите пароль")
    Paswd = input()
    for user in Users:
        if user[0] == Login:
            if user[1] == Paswd:
                print("Вы успешно вошли")
            else:
                print("Пароль не верный")
                exit()
else:
    cur.execute('SELECT * FROM Users')
    Users = cur.fetchall()
    for i in Users:
        print(i)
    print(sys.argv)
    print(ar)

    print("NO")