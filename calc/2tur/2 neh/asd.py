import sys
import sqlite3
import json, xml

arg = sys.argv[1:]

conn = sqlite3.connect("data.db")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS base (id INTEGER PRIMARY KEY AUTOINCREMENT, age INTEGER, name TEXT, data TEXT)")
conn.commit()

if arg[0] == "help":
    print("add -a INT -n STR -d STR\nprint\nupdate -i INT\nclear -i INT")
elif arg[0] == "add":
    cur.execute("INSERT INTO base (age, name, data) VALUES (?,?,?)", (arg[2], arg[4], arg[6]))
    conn.commit()
elif arg[0] == "print":
    row = cur.execute("SELECT * FROM base").fetchall()
    for i in row:
        print(i)
elif arg[0] == "update":
    cur.execute('UPDATE base SET age =?, name =?, data =? WHERE id =?', (arg[3], arg[4], arg[5], arg[2]))
    conn.commit()
else:
    print("error")
