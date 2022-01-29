n = float(input())
A = list(map(float, input().split()))
y = max(A)
B = []

for i in A:
    x = i/y*100
    B.append(x)

print(sum(B)/n)