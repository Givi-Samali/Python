n, t = map(int, input().split())
s = input()
for i in range(t):
    if 'SO' in s:
        s = s.replace('SO', 'OS')
    else:
        break
print(s)
