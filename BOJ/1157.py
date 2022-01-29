s = list(input().upper())

x = list(set(s))

n=[]
for i in x:
    a = s.count(i)
    n.append(a)

if n.count(max(n))>1:
    print('?')
else:
    print(x[n.index(max(n))])