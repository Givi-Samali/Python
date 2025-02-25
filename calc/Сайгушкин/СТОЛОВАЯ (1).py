"""n, t = map(int, input().split())
cash = input()
for i in range(t):
    if 'SO' in cash:
        cash = cash.replace('SO', 'OS')
    else:
        break
print(cash)"""
i = open("input.txt", "r")
n, t = map(int, i.readline().split())
cash = i.readline()
for j in range(t):
    if "SO" in cash:
        cash = cash.replace('SO', 'OS')
    else:
        break
o = open('output.txt', 'w')
o.write(cash)