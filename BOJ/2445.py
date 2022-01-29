n = int(input())
for i in range(1, n+1):
    butter = '*'*i + ' '*(2*n-2*i) + '*'*i
    print(butter)
for i in range(n-1, 0, -1):
    fly = '*'*i + ' '*(2*n-2*i) + '*'*i
    print(fly)