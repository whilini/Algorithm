n = int(input())
for i in range(1, n+1):
    star1 = ' '*(n-i) + '*'*(2*i-1)
    print(star1)
for i in range(n-1, 0, -1):
    star2 = ' '*(n-i) + '*'*(2*i-1)
    print(star2)