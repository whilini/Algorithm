dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
S = list(input())
a = 0
for i in S:
    for j in dial:
        if i in j:        
            a = a + dial.index(j) + 3
print(a)