A = []
for i in range(10):
    y = int(input())
    x = y%42
    A.append(x)

print(len(set(A)))