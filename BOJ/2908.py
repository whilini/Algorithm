a, b = input().split()

x = int(a[::-1])
y = int(b[::-1])

if x<y:
    print(y)
else:
    print(x)