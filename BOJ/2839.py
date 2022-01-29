S = []
n = int(input())
a = n//5

while True:
    b = (n-5*a)//3
    if 5*a + 3*b == n:
        S.append(a+b)
    a -= 1
    if a<0:
        break

if len(S)>0:                
    print(min(S))
else:
    print('-1')