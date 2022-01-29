K = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
n = input()
for i in K:
    if i in n:
        n = n.replace(i, '#')
print(len(n))