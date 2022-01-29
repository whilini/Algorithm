a = int(input())
S = list(map(int, input().split()))
X = [1]
for i in range(2, max(S)//2):
    for j in S:
        if j>i and j%i==0:
            X.append(j)
for j in X:
    if j in S:
        del S[S.index(j)]               
print(len(S))