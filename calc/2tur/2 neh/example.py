import sys
import sqlite3
import json
conn = sqlite3.connect("database.db")
cur = conn.cursor()
#Города
cur.execute('CREATE TABLE IF NOT EXISTS goroda (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, gorod_b INTEGER)')
conn.commit()
#Базы
cur.execute('CREATE TABLE IF NOT EXISTS base (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, gorod TEXT, val INTEGER)')
conn.commit()
#Товары
cur.execute('CREATE TABLE IF NOT EXISTS tovar (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, count INTEGER, cost INTEGER, base TEXT)')
conn.commit()

arg = sys.argv[1:]
print(arg)
if "help" in arg and len(arg) == 1:
    print("print(-a,-g,-b,-t)\nadd (-g,-b,-t)\nupdate (-g,-b,-t)\ndel (-g,-b,-t)")
    exit()
elif "help" in arg and "add" in arg:
    print("add -g name")
    print("add -b name gorod val")
    print("add -t name count cost base gorod")
    exit()
elif "help" in arg and "update" in arg:
    print("update -g oldname nowname")
    print("update -b -a(all) -n(old_name/new_name) -g(old_name_gorod/new_name_gorod) -val(old_val/new_val)")
    print("update -t -a(all) -n(old_name/new_name) -g(old_name_gorod/new_name_gorod) -c (old_count/new_count) -cs(old_cost/new_cost) -b(old_name_base/new_base_name)")
    exit()
elif "help" in arg and "print" in arg:
    print("print -g goroda")
    print("print -b base/ -b name_gorod - base in gorod")
    print("print -t tovar/ -t -base base_name - tovar in base/ -t -gorod name_gorod - tovar in gorod")
    exit()

if "add" == arg[0]:

    if "-g" == arg[1] and len(arg) == 3:
        cur.execute('INSERT INTO goroda (name, gorod_b) VALUES (?,?)', (arg[2], 0))
        conn.commit()
        print("Город добавлен")
    elif "-b" == arg[1] and len(arg) == 5:
        goroda = cur.execute('SELECT name FROM goroda').fetchall()
        gor = (arg[3],)
        if gor in goroda:
            cur.execute('INSERT INTO base (name, gorod, val) VALUES (?,?,?)', (arg[2], arg[3], arg[4]))
            conn.commit()
            cur.execute('UPDATE goroda SET gorod_b = gorod_b + 1 WHERE name =?', (arg[3],))
            conn.commit()
            print("База добавлена")
        else:
            print("Выбраного города не существует")
    elif "-t" == arg[1] and len(arg) == 6:
        base = cur.execute('SELECT name FROM base').fetchall()
        ba = (arg[5],)
        if ba in base:
            cur.execute('INSERT INTO tovar (name, count, cost, base) VALUES (?,?,?,?)', (arg[2], arg[3], arg[4], arg[5]))
            conn.commit()
            cur.execute('UPDATE base SET val = val - ? WHERE name =?', (int(arg[3]), arg[5]))
            conn.commit()
            print("Товар добавлен")
        else:
            print('Выбранной базы не сущетвует')
    else:
        print("Неверное кол-во агрументов")
elif "print" == arg[0]:
    if '-g' == arg[1] and len(arg) == 2:
        pr = cur.execute('SELECT * FROM goroda').fetchall()
        for i in pr:
            print(*i, sep=" ")
    elif '-b' == arg[1] and len(arg) == 2:
        pr = cur.execute('SELECT * FROM base').fetchall()
        for i in pr:
            print(*i, sep=" ")
    elif '-b' == arg[1] and len(arg) == 3:
        pr = cur.execute('SELECT * FROM base WHERE gorod =?', (arg[2],)).fetchall()
        for i in pr:
            print(*i, sep=" ")
    elif '-t' == arg[1] and len(arg) == 2:
        pr = cur.execute('SELECT * FROM tovar')
        for i in pr:
            print(*i, sep=" ")
    elif '-t' == arg[1] and '-base' == arg[2]:
        pr = cur.execute('SELECT * FROM tovar  WHERE base =?', (arg[3],)).fetchall()
        for i in pr:
            print(*i, sep=" ")
if arg[0] == 'createdb' and len(arg) == 1:
    with open('data.json', 'r') as file:
        data = json.load(file)
