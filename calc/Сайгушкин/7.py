a, b = map(str, input().split(" "))
h1 = int(a[:2])
m1 = int(a[3:5])
h2 = int(b[:2])
m2 = int(b[3:5])
print(a, b, h1, h2, m1, m2)
if h1 > h2:
    h1, h2 = h2, h1
H = h2+h1
M = m2+m1
if M >= 60:
    H += 1
    M -= 60
H /= 2
M /= 2
M += (H % 1) * 60
H = int(H)
M = int(M)
print(f"{H:0{2}}:{M:0{2}}")
