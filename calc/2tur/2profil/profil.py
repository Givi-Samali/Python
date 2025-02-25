import sys
import sqlite3
from sys import argv
arguments = argv[1:]

len_arg = len(arguments)
if 'help' in arguments:
    if len_arg == 0:
        exit()
    elif len_arg == 1:
        if arguments[0] == 'help':
            print('Commands:\n- help -\n- division -\n- cadet -\n- officer -')
    elif len_arg == 2:
        if arguments[0] == 'division' and arguments[1] == 'help':
            print('Division module commands:\n- help -\n- list -\n- add -\n- edit -\n- delete -')
        elif arguments[0] == 'cadet' and arguments[1] == 'help':
            print('Cadet module commands:\n- help -\n- list -\n- add -\n- edit -\n- delete -')
        elif arguments[0] == 'officer' and arguments[1] == 'help':
            print('Officer module commands:\n- help -\n- list -\n- add -\n- edit -\n- delete -')
    elif len_arg == 3:
        if arguments[0] == 'division' and arguments[1] == 'list' and arguments[2] == 'help':
            print('Division list command has no parameters')
        elif arguments[0] == 'division' and arguments[1] == 'add' and arguments[2] == 'help':
            print('Division add command parameters:\n-n : division name, required')
        elif arguments[0] == 'division' and arguments[1] == 'edit' and arguments[2] == 'help':
            print('Division edit command parameters:\n-i : Division ID, required\n-n : Name, required')
        elif arguments[0] == 'division' and arguments[1] == 'delete' and arguments[2] == 'help':
            print('Division delete command parameters:\n-i : Division ID\n-a : Delete all divisions')
        elif arguments[0] == 'cadet' and arguments[1] == 'list' and arguments[2] == 'help':
            print('Cadet list command parameters:\n-i : ID\n-l : last name\n-d : division ID\n-r : rank\n-o : division officer I\n-s : sorting, possible id, lastName\n-p : properties view, combination of i - id, r - rank, f - firstName, m - middleName, l - lastName, b – birthdate')
        elif arguments[0] == 'cadet' and arguments[1] == 'add' and arguments[2] == 'help':
            print('Cadet add command parameters:\n-f : first name, required\n-m : middle name, required\n-l : last name, required\n-b : birth date, required, format yyyy-MM-dd\n-r : rank, required\n-d : division ID, required')
        elif arguments[0] == 'cadet' and arguments[1] == 'edit' and arguments[2] == 'help':
            print('Cadet edit command parameters:\n-i : ID, required\n-f : first name\n-m : middle name\n-l : last name\n-b : birth date, format yyyy-MM-dd\n-r : rank\n-d : division ID')
        elif arguments[0] == 'cadet' and arguments[1] == 'delete' and arguments[2] == 'help':
            print('Cadet delete command parameters:\n-i : ID\n-d : division ID\n-o : division officer ID\n-a : delete all cadets')
        elif arguments[0] == 'officer' and arguments[1] == 'list' and arguments[2] == 'help':
            print('Officer list command parameters:\n-i : ID\n-l : last name\n-d : division ID\n-r : rank\n-c : cadet ID\n-s : sorting, possible id, lastName\n-p : properties view, combination of i - id, r - rank, f - firstName, m - middleName, l - lastName, b – birthdate')
        elif arguments[0] == 'officer' and arguments[1] == 'add' and arguments[2] == 'help':
            print('Officer add command parameters:\n-f : first name, required\n-m : middle name, required\n-l : last name, required\n-b : birth date, required, format yyyy-MM-dd\n-r : rank, required\n-d : division ID')
        elif arguments[0] == 'officer' and arguments[1] == 'edit' and arguments[2] == 'help':
            print('Officer edit command parameters:\n-i : ID, required\n-f : first name\n-m : middle name\n-l : last name\n-b : birth date, format yyyy-MM-dd\n-r : rank\n-d : division ID')
        elif arguments[0] == 'officer' and arguments[1] == 'delete' and arguments[2] == 'help':
            print('Officer delete command parameters:\n-i : ID\n-a : delete all officers')
    exit()
conn = sqlite3.connect('database.db')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS divisions (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)')
conn.commit()
cur.execute('CREATE TABLE IF NOT EXISTS cadets (id INTEGER PRIMARY KEY AUTOINCREMENT, FirstName TEXT, MiddleName '
            'TEXT, LastName TEXT, BirthDate DATE, Rank TEXT, Division INTEGER)')
conn.commit()
cur.execute('CREATE TABLE IF NOT EXISTS officers (id INTEGER PRIMARY KEY AUTOINCREMENT, FirstName TEXT, MiddleName '
            'TEXT, LastName TEXT, BirthDate DATE, Rank TEXT, Division INTEGER)')
conn.commit()

###   ADD FUNCTIONS
def add_division(name):
    cur.execute('INSERT INTO divisions (name) VALUES (?)', (name,))
    conn.commit()
    print('Ok')


def add_cadet(FirstName, MiddleName, LastName, BirthDate, Rank, Division):
    cur.execute(
        'INSERT INTO cadets (FirstName, MiddleName, LastName, BirthDate, Rank, Division) VALUES (?,?,?,?,?,?)',
        (FirstName, MiddleName, LastName, BirthDate, Rank, Division))
    conn.commit()
    print('Ok')


def add_officer(FirstName, MiddleName, LastName, BirthDate, Rank, Division):
    cur.execute(
        'INSERT INTO officers (FirstName, MiddleName, LastName, BirthDate, Rank, Division) VALUES (?,?,?,?,?,?)',
        (FirstName, MiddleName, LastName, BirthDate, Rank, Division))
    conn.commit()
    print('Ok')




###   LIST FUNCTIONS

def list_divisions():
    cur.execute('SELECT * FROM divisions')
    rows = cur.fetchall()
    for row in rows:
        print('{Division: {Id: ' + str(row[0]) + ', Name: ' + row[1] + '}}')


def list_cadets():
    cur.execute('SELECT * FROM cadets')
    rows = cur.fetchall()
    for row in rows:
        print('{Cadet: {Id: ' + str(row[0]) + ', Rank: ' + row[5] + ', FirstName: ' + row[1] + ', MiddleName: ' + row[
            2] + ', LastName: ' + row[3] + ', BirthDate: ' + row[4] + '}}')

def list_cadets_id():
    cur.execute('SELECT * FROM cadets ORDER BY id')
    rows = cur.fetchall()
    for row in rows:
        print('{Cadet: {Id: ' + str(row[0]) + ', Rank: ' + row[5] + ', FirstName: ' + row[1] + ', MiddleName: ' + row[
            2] + ', LastName: ' + row[3] + ', BirthDate: ' + row[4] + '}}')

def list_cadets_LastName():
    cur.execute('SELECT * FROM cadets ORDER BY LastName')
    rows = cur.fetchall()
    for row in rows:
        print('{Cadet: {Id: ' + str(row[0]) + ', Rank: ' + row[5] + ', FirstName: ' + row[1] + ', MiddleName: ' + row[
            2] + ', LastName: ' + row[3] + ', BirthDate: ' + row[4] + '}}')

def list_cadets_div():
    cur.execute('SELECT * FROM cadets ORDER BY Division')
    rows = cur.fetchall()
    for row in rows:
        print('{Cadet: {Id: ' + str(row[0]) + ', Rank: ' + row[5] + ', FirstName: ' + row[1] + ', MiddleName: ' + row[
            2] + ', LastName: ' + row[3] + ', BirthDate: ' + row[4] + '}}')

def list_cadets_rank():
    cur.execute('SELECT * FROM cadets ORDER BY Rank DESC')
    rows = cur.fetchall()
    for row in rows:
        print('{Cadet: {Id: ' + str(row[0]) + ', Rank: ' + row[5] + ', FirstName: ' + row[1] + ', MiddleName: ' + row[
            2] + ', LastName: ' + row[3] + ', BirthDate: ' + row[4] + '}}')



def list_cadets_by_p(parametr):
    cur.execute('SELECT * FROM cadets')
    rows = cur.fetchall()
    for row in rows:
        print('{Cadet: {', end='')
        for p in parametr:
            if p == 'i':
                print(f'Id: {row[0]}', end=', ')
            elif p == 'r':
                print(f'Rank: {row[5]}', end=', ')
            elif p == 'f':
                print(f'FirstName: {row[1]}', end=', ')
            elif p == 'm':
                print(f'MiddleName: {row[2]}', end=', ')
            elif p == 'l':
                print(f'LastName: {row[3]}', end=', ')
            elif p == 'b':
                print(f'BirthDate: {row[4]}', end='')
        print('}}', end='\n')

def list_officers_by_p(parametr):
    cur.execute('SELECT * FROM officers')
    rows = cur.fetchall()
    for row in rows:
        print('{Officer: {', end='')
        for p in parametr:
            if p == 'i':
                print(f'Id: {row[0]}', end=', ')
            elif p == 'r':
                print(f'Rank: {row[5]}', end=', ')
            elif p == 'f':
                print(f'FirstName: {row[1]}', end=', ')
            elif p == 'm':
                print(f'MiddleName: {row[2]}', end=', ')
            elif p == 'l':
                print(f'LastName: {row[3]}', end=', ')
            elif p == 'b':
                print(f'BirthDate: {row[4]}', end='')
        print('}}', end='\n')


def list_officers():
    cur.execute('SELECT * FROM officers')
    rows = cur.fetchall()
    for row in rows:
        print('{Officer: {Id:'+ str(row[0]) + ', Rank:'+ row[5] + ', FirstName:'+ row[1] + ', MiddleName:'+ row[
            2] + ', LastName:'+ row[3] + ', BirthDate:'+ row[4] + '}}')

def list_officers_id():
    cur.execute('SELECT * FROM officers ORDER BY id')
    rows = cur.fetchall()
    for row in rows:
        print('{Officer: {Id:'+ str(row[0]) + ', Rank:'+ row[5] + ', FirstName:'+ row[1] + ', MiddleName:'+ row[
            2] + ', LastName:'+ row[3] + ', BirthDate:'+ row[4] + '}}')

def list_officers_LastName():
    cur.execute('SELECT * FROM officers ORDER BY LastName')
    rows = cur.fetchall()
    for row in rows:
        print('{Officer: {Id:'+ str(row[0]) + ', Rank:'+ row[5] + ', FirstName:'+ row[1] + ', MiddleName:'+ row[
            2] + ', LastName:'+ row[3] + ', BirthDate:'+ row[4] + '}}')

def list_officer_div():
    cur.execute('SELECT * FROM officers ORDER BY Division')
    rows = cur.fetchall()
    for row in rows:
        print('{Officer: {Id:'+ str(row[0]) + ', Rank:'+ row[5] + ', FirstName:'+ row[1] + ', MiddleName:'+ row[
            2] + ', LastName:'+ row[3] + ', BirthDate:'+ row[4] + '}}')

def list_officers_rank():
    cur.execute('SELECT * FROM officers ORDER BY Rank DESC')
    rows = cur.fetchall()
    for row in rows:
        print('{Officer: {Id:'+ str(row[0]) + ', Rank:'+ row[5] + ', FirstName:'+ row[1] + ', MiddleName:'+ row[
            2] + ', LastName:'+ row[3] + ', BirthDate:'+ row[4] + '}}')

def list_officers_id():
    cur.execute('SELECT * FROM officers ORDER BY id')
    rows = cur.fetchall()
    for row in rows:
        print('{Officer: {Id:'+ str(row[0]) + ', Rank:'+ row[5] + ', FirstName:'+ row[1] + ', MiddleName:'+ row[
            2] + ', LastName:'+ row[3] + ', BirthDate:'+ row[4] + '}}')


### DELETE
def delete_division(id):
    cur.execute('DELETE FROM divisions WHERE id =?', (id,))
    conn.commit()
    print('Ok')


def delete_all_division():
    cur.execute('DELETE FROM divisions')
    conn.commit()
    print('Ok')


def delete_cadet(id):
    cur.execute('DELETE FROM cadets WHERE id =?', (id,))
    conn.commit()
    print('Ok')


def delete_cadet_division(division):
    cur.execute('DELETE FROM cadets WHERE Division =?', (division,))
    conn.commit()
    print('Ok')


def delete_cadet_OfficerID(OfficierID):
    DivID = cur.execute('SELECT Division FROM officers WHERE id =?', (OfficierID,)).fetchall()[0]
    cur.execute('DELETE FROM cadets WHERE Division =?', (DivID,))
    conn.commit()
    print('Ok')


def delete_all_cadets():
    cur.execute('DELETE FROM cadets')
    conn.commit()
    print('Ok')


def delete_officer(id):
    cur.execute('DELETE FROM officers WHERE id =?', (id,))
    conn.commit()
    print('Ok')


def delete_all_officers():
    cur.execute('DELETE FROM officers')
    conn.commit()
    print('Ok')


### EDIT

def edit_division(id, name):
    cur.execute('UPDATE divisions SET name =? WHERE id =?', (name, id))
    conn.commit()
    print('Ok')

def edit_cadet(id, parametr, update):
    if parametr == '-f':
        cur.execute('UPDATE cadets SET FirstName =? WHERE id =?', (update, id))
        conn.commit()
    elif parametr == '-m':
        cur.execute('UPDATE cadets SET MiddleName =? WHERE id =?', (update, id))
        conn.commit()
    elif parametr == '-l':
        cur.execute('UPDATE cadets SET LastName =? WHERE id =?', (update, id))
        conn.commit()
    elif parametr == 'd':
        cur.execute('UPDATE cadets SET BithDate =? WHERE id =?', (update, id))
        conn.commit()
    elif parametr == '-r':
        cur.execute('UPDATE cadets SET Rank =? WHERE id =?', (update, id))
        conn.commit()
    elif parametr == '-d':
        cur.execute('UPDATE cadets SET Division =? WHERE id =?', (update, id))
        conn.commit()
    print('Ok')


def edit_officer(id, parametr, update):
    if parametr == '-f':
        cur.execute('UPDATE officers SET FirstName =? WHERE id =?', (update, id))
        conn.commit()
    elif parametr == '-m':
        cur.execute('UPDATE officers SET MiddleName =? WHERE id =?', (update, id))
        conn.commit()
    elif parametr == '-l':
        cur.execute('UPDATE officers SET LastName =? WHERE id =?', (update, id))
        conn.commit()
    elif parametr == 'd':
        cur.execute('UPDATE officers SET BithDate =? WHERE id =?', (update, id))
        conn.commit()
    elif parametr == '-r':
        cur.execute('UPDATE officers SET Rank =? WHERE id =?', (update, id))
        conn.commit()
    elif parametr == '-d':
        cur.execute('UPDATE officers SET Division =? WHERE id =?', (update, id))
        conn.commit()
    print('Ok')


if sys.argv[1] == "division":
    ohibka_parametra = True
    ohibka_module = True
    if sys.argv[2] == "list":
        list_divisions()
    elif sys.argv[2] == "add":
        add_division(sys.argv[3])
    elif sys.argv[2] == "edit":
        if len(sys.argv[2:]) == 5:
            edit_division(int(sys.argv[4]), sys.argv[6])
        else:
            ohibka_module = False
    elif sys.argv[2] == "delete":
        if len(sys.argv[2:]) == 1:
            ohibka_parametra = False
        else:
            if sys.argv[3] == "-i":
                delete_division(int(sys.argv[4]))
            elif sys.argv[3] == "-a":
                delete_all_division()
            else:
                ohibka_parametra = False
    elif sys.argv[2] == "help":
        pass
    else:
        ohibka_parametra = False
    if ohibka_parametra == False:
        print(f'Error: not set parameter "{sys.argv[2]}" for command "{sys.argv[1]}"')
    if ohibka_module == False:
        print(f'Error: not enough params for command "{sys.argv[2]}" in module "{sys.argv[1]}". Type "{sys.argv[1]} {sys.argv[2]} help" for details')

elif sys.argv[1] == "cadet":
    ohibka_parametra = True
    ohibka_module = True
    if sys.argv[2] == "list":
        if len(sys.argv[2:]) == 1:
            list_cadets()
        else:
            if sys.argv[3] == "-i":
                list_cadets_id()
            elif sys.argv[3] == "-l":
                list_cadets_LastName()
            elif sys.argv[3] == "-d":
                list_cadets_div()
            elif sys.argv[3] == "-r":
                list_cadets_rank()
            elif sys.argv[3] == "-o":
                pass
            elif sys.argv[3] == "-s":
                pass
            elif sys.argv[3] == "-p":
                try:
                    list_cadets_by_p(sys.argv[4])
                except:
                    list_cadets_by_p("irfmlb")
            else:
                ohibka_parametra = False
    elif sys.argv[2] == "add":
        if len(sys.argv[3:]) == 6:
            add_cadet(sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8])
        else:
            ohibka_module = False
    elif sys.argv[2] == "edit":
        if len(sys.argv[2:]) == 5:
            edit_cadet(int(sys.argv[4]), sys.argv[5], sys.argv[6])
        else:
            ohibka_module = False
    elif sys.argv[2] == "delete":
        if sys.argv[2:] == 1:
            ohibka_module = False
        else:
            if sys.argv[3] == "-i":
                delete_cadet(int(sys.argv[4]))
            elif sys.argv[3] == "-d":
                delete_cadet_division(int(sys.argv[4]))
            elif sys.argv[3] == "-o":
                delete_cadet_OfficerID(int(sys.argv[4]))
            elif sys.argv[3] == "-a":
                delete_all_cadets()
            else:
                ohibka_parametra = False
    elif sys.argv[2] == "help":
        pass
    else:
        ohibka_parametra = False
    if ohibka_parametra == False:
        print(f'Error: not set parameter "{sys.argv[2]}" for command "{sys.argv[1]}"')
    if ohibka_module == False:
        print(f'Error: not enough params for command "{sys.argv[2]}" in module "{sys.argv[1]}". Type "{sys.argv[1]} {sys.argv[2]} help" for details')

elif sys.argv[1] == "officer":
    ohibka_parametra = True
    ohibka_module = True
    if sys.argv[2] == "list":
        if len(sys.argv[2:]) == 1:
            list_officers()
        else:
            if sys.argv[3] == "-i":
                list_officers_id()
            elif sys.argv[3] == "-l":
                list_officers_LastName()
            elif sys.argv[3] == "-d":
                list_officer_div()
            elif sys.argv[3] == "-r":
                list_officers_rank()
            elif sys.argv[3] == "-c":
                pass
            elif sys.argv[3] == "-s":
                pass
            elif sys.argv[3] == "-p":
                try:
                    list_officers_by_p(sys.argv[4])
                except:
                    list_officers_by_p("irfmlb")
            else:
                ohibka_parametra = False
    elif sys.argv[2] == "add":
        if len(sys.argv[3:]) == 6:
            add_officer(sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8])
        else:
            ohibka_module = False
    elif sys.argv[2] == "edit":
        if len(sys.argv[2:]) == 5:
            edit_officer(int(sys.argv[4]), sys.argv[5], sys.argv[6])
        else:
            ohibka_module = False
    elif sys.argv[2] == "delete":
        if len(sys.argv[2:]) == 1:
            ohibka_parametra = False
        else:
            if sys.argv[3] == "-i":
                delete_officer(int(sys.argv[4]))
            elif sys.argv[3] == "-a":
                delete_all_officers()
            else:
                ohibka_parametra = False
    elif sys.argv[2] == "help":
        pass
    else:
        ohibka_parametra = False
    if ohibka_parametra == False:
        print(f'Error: not set parameter "{sys.argv[2]}" for command "{sys.argv[1]}"')
    if ohibka_module == False:
        print(f'Error: not enough params for command "{sys.argv[2]}" in module "{sys.argv[1]}". Type "{sys.argv[1]} {sys.argv[2]} help" for details')
else:
    print(f'Error: not set parameter "{sys.argv[1]}" for programm')