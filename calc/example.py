def example():
    a, b = input().split()
    a, b = int(a), int(b)
    count = 0
    count_R = 0
    count_G = 0
    count_B = 0
    for i in range(1, a + 1):
        for j in range(1, b + 1):
            if (i * j) % 5 == 0:
                count_B += 1
            elif (i*j) % 3 == 0:
                count_G += 1
            elif (i*j) % 2 == 0:
                count_R += 1
            else:
                count += 1
    print("RED : " + str(count_R))
    print("GREEN : " + str(count_G))
    print("BLUE : " + str(count_B))
    print("BLACK : " + str(count))
example()






