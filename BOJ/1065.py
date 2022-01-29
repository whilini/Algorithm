n  = int(input())
A = []

for i in range(1, n+1):
    if i<100:
        A.append(i)
    elif 100<=i<1000:
        B = list(map(int, str(i)))
        if B[0]+B[2] == 2*B[1]:
            A.append(i)

print(len(set(A)))