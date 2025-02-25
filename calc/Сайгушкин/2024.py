n = int(input())
if n == 1 or n == 2:
    print(2024)
    exit()
i = '0'
s = int('2024' + i)
k = 0
while True:
    i = str(k)
    for j in range(1, len(str(n))+1):
        d = i[-j:]
        s = int('2024' + d)
        if s % n == 0:
            while (s / 10) % n == 0:
                s //= 10
            print(s)
            exit()
    k += n
