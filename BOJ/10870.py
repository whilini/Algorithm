n = int(input())
a = 0
b = 1
r = 0
while r != n:
    a, b = b, a+b
    r+=1
if r == n:
    print(a)