n = int(input())
for i in range(n):
    star1 = ' '*i + '*'*(2*n-2*i-1)
    print(star1)
for i in range(n-1, 0, -1):
    star2 = ' '*(i-1) + '*'*(2*n-2*i+1)
    print(star2)