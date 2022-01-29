S = list(input())
abc = 'abcdefghijklmnopqrstuvwxyz'
A = list(abc)
for i in A:
    if i in S:
        print(S.index(i), end=' ')
    else:
        print(-1, end=' ')