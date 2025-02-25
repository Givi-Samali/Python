a = int(input())
B = list(map(int, input().split()))
C = list(map(int, input().split()))
count = 0
count_2 = 0
for i in C:
    count += min(B) + i
for i in B:
    count_2 += min(C) + i
print(min(count, count_2))

