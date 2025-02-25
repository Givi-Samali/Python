def aa():
    a = int(input())
    if 2024 % a == 0:
        print(2024)
        exit()
    if a > 2024:
        print(a*(10**len(str(a))) - len(str(a)) * a)
    if a < 2024:
        print(a*(10**len(str(a))) + (len(str(a))+1) * a)
    for i in range(len(str(a))+1):
        for j in range(10**i):
            if int("2024" + str(j).zfill(i)) % a == 0:
                print(int("2024" + str(j).zfill(i)))
                exit()

aa()




