k = int(input())

n=1
while True:
    if k==1:
        print(1)
        break

    n+=1
    if 3*n*n-9*n+8<= k <= 3*n*n-3*n+1:
        print(n)
        break