a = input()
b = list(input())
C = [0] * len(b)
for i in range(len(C)):
    C[i] = ord(b[i])
L = list(range(78, 91))
for i in range(65, 78):
    L.append(i)
otv = []
count = 0
i = 0
na = ord(a)
while count != len(b):
    if C[i] == na:
        otv.append("P")
        i += 1
        count += 1
    elif L.index(na) > L.index(C[i]):
        otv.append("L" + str(L.index(na) - L.index(C[i])))
        na = C[i]
    else:
        otv.append("R" + str(L.index(C[i]) - L.index(na)))
        na = C[i]
for i in otv:
    print(i, sep="\n")