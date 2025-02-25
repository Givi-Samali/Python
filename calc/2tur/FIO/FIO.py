import sys
import sqlite3

con = sqlite3.connect('database.db')
cur = con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT,'
            'name TEXT,'
            'last_name TEXT,'
            'sur_name TEXT,'
            'login TEXT,'
            'password TEXT,'
            'balance INTEGER)')
con.commit()
cur.execute('CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY AUTOINCREMENT,'
            'name TEXT,'
            'price INTEGER,'
            'count INTEGER)')
con.commit()
cur.execute('CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY AUTOINCREMENT,'
            'products_id TEXT,'
            'counts TEXT)')
con.commit()
cur.execute('CREATE Table IF NOT EXISTS avt (bool INTEGER, id INTEGER)')

gg = cur.execute('SELECT * FROM avt').fetchall()
if gg[0][0] == True:
    ID = gg[0][1]
    acc = True
else:
    acc = False

def add_user(name, last_name, sur_name, login, password):
    cur.execute('INSERT INTO users (name, last_name, sur_name, login, password, balance) VALUES (?,?,?,?,?,?)',
                (name, last_name, sur_name, login, password, 0))
    con.commit()


def login(login, password):
    lst = cur.execute('SELECT id, login, password FROM users').fetchall()
    for i in lst:
        if i[1] == login and i[2] == password:
            global ID
            cur.execute('DELETE FROM avt')
            con.commit()
            cur.execute('INSERT INTO avt (bool, id) VALUES (?,?)', (True, i[0]))
            con.commit()
            ID = i[0]
            break
    else:
        print('Такой учётной записи не существует, проверьте введёные логин и пароль или зарегестрируйтесь')


def logout():
    cur.execute('DELETE FROM avt')
    con.commit()
    cur.execute('INSERT INTO avt (bool, id) VALUES (?,?)', (False, 0))
    con.commit()


def delete_account():
    avt = cur.execute('SELECT * FROM avt').fetchall()
    if avt[0][0] == True:
        print('Вы уверены, что хотите удалить учётную запись?')
        print('Введите "Да" для да, "Нет" для нет')
        ans = input()
        if ans == 'Да':
            cur.execute('DELETE FROM users WHERE id =?', (avt[0][1],))
            con.commit()
            print('Учётная запись удалена')
        else:
            print('Отменено')
    else:
        print('Вы не вошли в учётную запись, войдите, чтобы удалить')


def list():
    cur.execute('SELECT * FROM products')
    rows = cur.fetchall()
    for row in rows:
        print('{Id: ' + str(row[0]) + ', Name: ' + row[1] + ', Price: ' + str(row[2]) + ', Count: ' + str(row[3]) + '}')
    print()

def buy(name, count):
    for line in cur.execute('SELECT * FROM products').fetchall():
        if line[1] == name:
            if line[3] >= int(count):
                cur.execute('UPDATE products SET count = count -? WHERE id =?', (count, line[0]))
                con.commit()
                price = cur.execute('SELECT price FROM products WHERE name =?', (name,)).fetchall()[0][0]
                cur.execute('UPDATE users SET balance = balance -? WHERE id =?', (int(count)*price, ID))
                con.commit()
                print(f'Вы купили {count} шт. товара {name}')
            else:
                print(f'Осталось на складе {line[3]} шт. товара {name}')
            break
    else:
        print('Такой товар не существует')

def add_balance(summary, id):
    cur.execute('UPDATE users SET balance = balance +? WHERE id =?', (summary, id))
    con.commit()
    print(f'Теперь ваш баланс: {cur.execute("SELECT balance FROM users WHERE id =?", (id,)).fetchall()[0][0]}')

def status(id):
    stat = cur.execute('SELECT * FROM users WHERE id =?', (id,)).fetchall()
    print(f'ФИО: {stat[0][1]} {stat[0][2]} {stat[0][3]}\n'
          f'Баланс: {stat[0][6]}')
          #f'Количество совершённых покупок: {len(stat[7].split())}'

if sys.argv[1] == "reg":
    add_user(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
    print("reg")
elif sys.argv[1] == "login":
    login(sys.argv[2], sys.argv[3])
    print("login")
elif sys.argv[1] == "logout":
    logout()
    print("logout")
elif sys.argv[1] == "delete_account":
    if acc == True:
        print("delete_account")
    else:
        print("Login in account")
elif sys.argv[1] == "list":
    if acc == True:
        list()
    else:
        print("Login in account")
elif sys.argv[1] == "buy":
    if acc == True:
        buy(sys.argv[2], sys.argv[3])
        print("buy")
    else:
        print("Login in account")
elif sys.argv[1] == "addbalance":
    if acc == True:
        add_balance(sys.argv[2], ID)
        print("addbalance")
    else:
        print("Login in account")
elif sys.argv[1] == "status":
    if acc == True:
        status(ID)
        print("status")
    else:
        print("Login in account")
elif sys.argv[1] == "mysell":
    if acc == True:
        print("mysell")
    else:
        print("Login in account")