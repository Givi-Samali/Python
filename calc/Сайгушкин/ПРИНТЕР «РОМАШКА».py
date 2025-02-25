pos = input()
row = input()
if row == '':
    exit()
if row[0] == pos:
    print('P')
    row = row[1:]
alf = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
for i in row:
    a = alf.index(pos) - alf.index(i)
    if a < 0:
        b = alf.index(pos) + abs(alf.index(i) - 26)
        if b > abs(a):
            print(f'R{(abs(a))}')
        else:
            print(f'L{abs(b)}')
    else:
        b = 26 - alf.index(pos) + alf.index(i)
        if a < b:
            print(f'L{a}')
        else:
            print(f'R{b}')
    print('P')
    pos = i

