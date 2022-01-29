def d(n):
    n = n + sum(map(int, str(n)))
    return n

A=[]

for i in range(1, 10001):
    x = d(i)
    A.append(x)
    
for j in range(1, 10001):
    if j not in A:
        print(j)