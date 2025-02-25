import sqlite3

conn = sqlite3.connect('data_base.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS data_base (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                PU TEXT,
                PRO TEXT,
                OP TEXT)""")
conn.commit()

print(cur.execute('SELECT * FROM data_base').fetchall())