import sys
import os
command = 0
def START():
    global command
    os.system('cls')
    print('MARINE SAFETY BELT MONITOR')
    command = input('>>')
    if command == 'exit':
        os.system('exit')
    elif command == 'help':
        os.system('cls')
        print('1) init - инициализация внешнего хранилища')
        print('2) show - вывод содержимого внешнего хранилища')
        print('3) add – ручное добавление записи в хранилище\n4) load - загрузка данных из источников\n5) mon - произвести оценку обстановки\n6) clean – очистка внешнего хранилища\n7) exit - выход из программы')
        print('\n')
        q = 0
        while q != 'q':
            q = input('Для возврата введите "q": ')
        else:
            START()
    elif 'init' in command:
        os.system('cls')
        INIT()
    elif 'show' in command:
        os.system('cls')
        SHOW()
    elif 'add' in command:
        os.system('cls')
        ADD()
    elif 'load' in command:
        os.system('cls')
        LOAD()
    elif 'mon' in command:
        os.system('cls')
        MON()
    elif 'clean' in command:
        os.system('cls')
        CLEAN()
    elif 'exit' in command:
        os.system('cls')
        EXIT()
def INIT():
    global command
    if command == 'init help':
        print('Модуль init инициализирует внешнее хранилище данных для работы программы.')
        print('При успешном исполнении init будет выведено сообщение:')
        print('"База данных успешно проинициализирована!".')
        print('Если хранилище было инициализировано ранее, то будет')
        print('выведено сообщение "База данных была проинициализирована ранее!"')
        print('\n')
        q = 0
        while q != 'q':
            q = input('Для возврата введите "q": ')
        else:
            START()

def SHOW():
    global command
    if command == 'show help':
        print('Модуль show при вызове без аргументов отображает имена хранимых в БД таблиц.')
        print('При вызове show [наименование_таблицы] модуль отображает')
        print('пронумерованное содержимое таблицы.')
        print('Каждая строка выводимых данных соответствует одной')
        print('записи в выводимой таблице.')
        print('\n')
        q = 0
        while q != 'q':
            q = input('Для возврата введите "q": ')
        else:
            START()

def ADD():
    global command
    if command == 'add help':
        print('Модуль add ожидает в качестве аргумента название таблицы.')
        print('Пример: >>add [наименование_таблицы]')
        print('Программа перейдет в режим добавления данных.')
        print('При попытке вызова модуля add без аргумента программа')
        print('Предупредит пользователя об ошибке')
        print('\n')
        q = 0
        while q != 'q':
            q = input('Для возврата введите "q": ')
        else:
            START()

def LOAD():
    global command
    if command == 'load help':
        print('Модуль load ожидает в качестве аргумента относительный путь')
        print('к одноименному с соответствующей таблицей файлу с данными.')
        print('Пример: >>load [относительный_путь_к_файлу]')
        print('При успешном выполнении выводит количество добавленных записей')
        print('\n')
        q = 0
        while q != 'q':
            q = input('Для возврата введите "q": ')
        else:
            START()

def MON():
    global command
    if command == 'mon help':
        print('Модуль mon производит автоматический анализ')
        print('обстановки на театре проведения учений.')
        print('При обнаружении несанкционированных целей производится')
        print('формирование необходимых телеграмм.')
        print('Модуль mon не принимает аргументов.')
        print('\n')
        q = 0
        while q != 'q':
            q = input('Для возврата введите "q": ')
        else:
            START()

def  CLEAN():
    global command
    if command == 'clean help':
        print('Модуль clean производит очистку внешней')
        print('базы данных приложения.')
        print('Модуль принимает в качестве аргумента наименование')
        print('таблицы, которую необходимо очистить. При вызове модуля')
        print('clean без аргументов модуль очистит все таблицы.')
        print('\n')
        q = 0
        while q != 'q':
            q = input('Для возврата введите "q": ')
        else:
            START()

def EXIT():
    global command
    if command == 'exit help':
        print('Модуль exit производит штатный выход из программы,')
        print('гарантируя сохранение внесенных во внешнее хранилище изменений')
        print('\n')
        q = 0
        while q != 'q':
            q = input('Для возврата введите "q": ')
        else:
            START()

while command != 'exit':
    START()
