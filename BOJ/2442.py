n = int(input())
for i in range(1,n+1):
    star = ' '*(n-i) + '*'*(2*i-1)
    print(star)