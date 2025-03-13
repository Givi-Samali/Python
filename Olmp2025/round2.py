import sqlite3
import os



def qq(com):
    while com != 'q':
        com = input('Для возврата введите "q": ')
    else:
        main()

def helps(com):
    dicts = {
        'help' : '''1) init - инициализация внешнего хранилища
2) show - вывод содержимого внешнего хранилища
3) add – ручное добавление записи в хранилище
4) load - загрузка данных из источников
5) mon - произвести оценку обстановки
6) clean – очистка внешнего хранилища
7) exit - выход из программы\n''',

        'init help': '''Модуль init инициализирует внешнее хранилище данных для работы программы.
При успешном исполнении init будет выведено сообщение:
"База данных успешно проинициализирована!".
Если хранилище было инициализировано ранее, то будет
выведено сообщение "База данных была проинициализирована ранее!"\n''',

        'show help': '''Модуль show при вызове без аргументов отображает имена хранимых в БД таблиц.
При вызове show [наименование_таблицы] модуль отображает
пронумерованное содержимое таблицы.
Каждая строка выводимых данных соответствует одной
записи в выводимой таблице.\n''',

        'add help': '''Модуль add ожидает в качестве аргумента название таблицы.
Пример: >>add [наименование_таблицы]
3 Программа перейдет в режим добавления данных.
4 При попытке вызова модуля add без аргумента программа
5 Предупредит пользователя об ошибке\n''',

        'load help': '''Модуль load ожидает в качестве аргумента относительный путь
к одноименному с соответствующей таблицей файлу с данными.
Пример: >>load [относительный_путь_к_файлу]
При успешном выполнении выводит количество добавленных записей\n''',

        'mon help': '''Модуль mon производит автоматический анализ
обстановки на театре проведения учений.
При обнаружении несанкционированных целей производится
формирование необходимых телеграмм.
Модуль mon не принимает аргументов.\n''',

        'clean help': '''Модуль clean производит очистку внешней
базы данных приложения.
Модуль принимает в качестве аргумента наименование
таблицы, которую необходимо очистить. При вызове модуля
clean без аргументов модуль очистит все таблицы.\n'''
    }
    os.system('cls')
    print(dicts.get(" ".join(com), "Unknown command"))
    qq(com)

def init(com):
    if os.path.isfile('database.db'):
        os.system('cls')
        print('База данных была проинициализирована ранее!\n')
        qq(com)
    else:
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()

        cur.execute('CREATE TABLE IF NOT EXISTS Participants (id INTEGER PRIMARY KEY AUTOINCREMENT,'
                    'number INTEGER,'
                    'coord TEXT,'
                    'name TEXT,'
                    'class TEXT,'
                    'strana TEXT,'
                    'code TEXT)')
        conn.commit()

        with open("Participants.txt", 'r', encoding='utf-8') as f:
            for line in f:
                two = list(line.split())[:2]
                three = list(line.split())[-3:]
                name = " ".join(list(line.split())[2:-3])
                cur.execute('INSERT INTO Participants (number,coord,name,class,strana,code) VALUES (?,?,?,?,?,?)', (int(two[0]), two[1], name, three[0], three[1], str(three[2]).replace('\n','')))
                conn.commit()
            f.close()

        cur.execute('CREATE TABLE IF NOT EXISTS Allowed (id INTEGER PRIMARY KEY AUTOINCREMENT,'
                    'code TEXT)')
        conn.commit()

        with open('Allowed.txt', 'r', encoding='utf-8') as f:
            for line in f:
                cur.execute('INSERT INTO Allowed (code) VALUES (?)', (str(list(line.split())[0]).replace('\n', ''),))
                conn.commit()
            f.close()

        cur.execute('CREATE TABLE IF NOT EXISTS Situation (id INTEGER PRIMARY KEY AUTOINCREMENT,'
                    'coord TEXT,'
                    'code TEXT)')
        conn.commit()

        with open('Situation.txt', 'r', encoding='utf-8') as f:
            for line in f:
                cur.execute("INSERT INTO Situation (coord,code) VALUES (?,?)", (str(line[:5]), str(line[6:]).replace('\n','')))
                conn.commit()
            f.close()

        cur.execute('CREATE TABLE IF NOT EXISTS Classes (id INTEGER PRIMARY KEY AUTOINCREMENT,'
                    'class TEXT,'
                    'name_class TEXT)')
        conn.commit()

        with open("Classes.txt", "r", encoding='utf-8') as f:
            for line in f:
                cur.execute('INSERT INTO Classes (class, name_class) VALUES (?,?)', (str(line[0]), str(line[2:]).replace('\n', '')))
                conn.commit()
            f.close()
        os.system('cls')
        print("База данных успешно проинициализирована!\n")
        qq(com)

def load(com):
    if len(com) == 1:
        os.system('cls')
        print("Требуется относительный путь к файлу!\n")
        qq(com)
    else:
        if os.path.isfile(str(com[1])):
            name_db = com[1]
            name_db = name_db[:-4]
            conn = sqlite3.connect('database.db')
            cur = conn.cursor()
            db = cur.execute(f'SELECT * FROM {name_db}').fetchall()
            db_old = []
            db_new = []
            for i in db:
                db_old.append(i[1:])
            if 'Classes.txt' in com:
                with open(str(com[1]), 'r', encoding='utf-8') as f:
                    for line in f:
                        db_new.append((line[0], str(line[2:]).replace('\n', '')))
                db_print = [x for x in db_new if x not in db_old]
                for i in db_print:
                    cur.execute('INSERT INTO Classes (class, name_class) VALUES (?,?)', (i[0], i[1]))
                    conn.commit()
                a = len(db_print)
                b = len([x for x in db_new if x in db_old])
                os.system('cls')
                print(f'Данные занесены в хранилище: Classes\nЗаписей произведено – {a}\nПроигнорировано – {b}\n')

            elif 'Allowed.txt' in com:
                with open(str(com[1]), 'r', encoding='utf-8') as f:
                    for line in f:
                        db_new.append((line.replace('\n', ''),))
                db_print = [x for x in db_new if x not in db_old]
                for i in db_print:
                    cur.execute('INSERT INTO Allowed (code) VALUES (?)', (i[0],))
                    conn.commit()
                a = len(db_print)
                b = len([x for x in db_new if x in db_old])
                os.system('cls')
                print(f'Данные занесены в хранилище: Allowed\nЗаписей произведено – {a}\nПроигнорировано – {b}\n')

            elif 'Participants.txt' in com:
                with open(str(com[1]), 'r', encoding='utf-8') as f:
                    for line in f:
                        two = list(line.split())[:2]
                        three = list(line.split())[-3:]
                        name = " ".join(list(line.split())[2:-3])
                        db_new.append((int(two[0]), two[1], name, three[0], three[1], three[2].replace('\n', '')))
                db_print = [x for x in db_new if x not in db_old]
                for i in db_print:
                    cur.execute('INSERT INTO Participants (number,coord,name,class,strana,code) VALUES (?,?,?,?,?,?)', (i[0], i[1], i[2], i[3], i[4], i[5]))
                    conn.commit()
                a = len(db_print)
                b = len([x for x in db_new if x in db_old])
                os.system('cls')
                print(f'Данные занесены в хранилище: Participants\nЗаписей произведено – {a}\nПроигнорировано – {b}\n')

            elif 'Situation.txt' in com:
                with open(str(com[1]), 'r', encoding='utf-8') as f:
                    for line in f:
                        coord = line[:5]
                        code = line[6:].replace('\n', '')
                        db_new.append((coord, code))
                db_print = [x for x in db_new if x not in db_old]
                for i in db_print:
                    cur.execute('INSERT INTO Situation (coord, code) VALUES (?,?)', (i[0], i[1]))
                    conn.commit()
                a = len(db_print)
                b = len([x for x in db_new if x in db_old])
                os.system('cls')
                print(f'Данные занесены в хранилище: Situation\nЗаписей произведено – {a}\nПроигнорировано – {b}\n')
            qq(com)
        else:
            os.system('cls')
            print('Данного файла не существует!\n')
            qq(com)

def show(com):
    if len(com) == 1:
        os.system('cls')
        print('''1. Participants – оперативные данные об участниках
2. Allowed – список разрешенных судов
3. Situation – данные обстановки
4. Classes – классификатор кораблей-участников\n''')
        qq(com)
    else:
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        try:
            os.system('cls')
            db = cur.execute(f'SELECT * FROM {com[1]}').fetchall()
            coun = 1
            for i in db:
                print(str(coun) + ")", *i[1:])
                coun += 1
            print('\n')
        except:
            os.system('cls')
            print('Такой таблицы не существует!\n')
        qq(com)

def add_part(com):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    os.system('cls')
    print(f"Add mode (Таблица: {com[1]}):\n")
    number = max(cur.execute('SELECT id FROM Participants').fetchall())
    print('[1] Порядковый номер корабля', *number)
    bort = input('[2] Бортовой номер корабля ')
    if not bort.isdigit() or (not (1 < int(bort) < 999)) or len(bort) != 3:
        add_part(com)
    coord = input('[3] Координаты корабля ')
    if not (coord[:2].isdigit() or coord[2] == ':' or coord[3:].isdigit() or (0 < int(coord[:2]) < 99) or (0 < int(coord[2:]) < 99)) or len(coord) != 5:
        add_part(com)
    name = input('[4] Наименование корабля ')
    if not name.isalpha():
        add_part(com)
    clas = input('[5] Класс корабля ')
    if not clas.isdigit() or len(clas) != 1:
        add_part(com)
    country = input('[6] Принадлежность ')
    if not country.islower() or len(country) != 2:
        add_part(com)
    codes = input('[7] Код системы «свой-чужой» ')
    if len(codes) != 19:
        add_part(com)
    cur.execute('INSERT INTO Participants (number,coord,name,class,strana,code) VALUES (?,?,?,?,?,?)', (bort, coord, name, clas, country, codes))
    conn.commit()
    os.system('cls')
    print('Запись в таблицу Participants успешно добавлена!\n')
    repeats = input('Повторить? (y/n): ')
    if repeats == 'y':
        add_part(com)
    else:
        main()

def add_allowed(com):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    os.system('cls')
    print(f"Add mode (Таблица: {com[1]}):\n")
    codes = input('[1] Код системы «свой-чужой» ')
    if len(codes) != 19:
        add_allowed(com)
    cur.execute('INSERT INTO Allowed (code) VALUES (?)', (codes,))
    conn.commit()
    os.system('cls')
    print(f'Запись в таблицу {com[1]} успешно добавлена!\n')
    repeats = input('Повторить? (y/n): ')
    if repeats == 'y':
        add_part(com)
    else:
        main()

def add_situation(com):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    os.system('cls')
    print(f"Add mode (Таблица: {com[1]}):\n")
    coord = input('[1] Координаты корабля ')
    if not (coord[:2].isdigit() or coord[2] == ':' or coord[3:].isdigit() or (0 < int(coord[:2]) < 99) or (0 < int(coord[2:]) < 99)) or len(coord) != 5:
        add_part(com)
    codes = input('[2] Код системы «свой-чужой» ')
    if len(codes) != 19:
        add_allowed(com)
    cur.execute('INSERT INTO Situation (coord, code) VALUES (?,?)', (coord, codes))
    conn.commit()
    os.system('cls')
    print(f'Запись в таблицу {com[1]} успешно добавлена!\n')
    repeats = input('Повторить? (y/n): ')
    if repeats == 'y':
        add_part(com)
    else:
        main()

def add_classes(com):
    os.system('cls')
    print('Вносить изменения в эту таблицу невозможно!\n')
    qq(com)

def add(com):
    if len(com) == 1:
        os.system('cls')
        print('Требуется указать таблицу!\n')
        qq(com)
    else:
        if com[1] == 'Participants':
            add_part(com)
        elif com[1] == 'Allowed':
            add_allowed(com)
        elif com[1] == 'Situation':
            add_situation(com)
        elif com[1] == 'Classes':
            add_classes(com)

def main():
    os.system('cls')
    print("MARINE SAFETY BELT MONITOR")
    com = list(input(">>").split())
    if "help" in com:
        helps(com)
    elif "init" in com:
        init(com)
    elif "load" in com:
        load(com)
    elif "show" in com:
        show(com)
    elif "add" in com:
        add(com)
    while com[0] != "exit":
        main()
    else:
        exit()
main()