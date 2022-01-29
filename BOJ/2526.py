A = []
for i in range(9):
    i = int(input())
    A.append(i)

print(max(A))
print(A.index(max(A))+1)