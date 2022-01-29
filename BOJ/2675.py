n = int(input())
for i in range(n):
    A = list(map(str, input().split()))
    x = int(A[0])
    y = list(str(A[1]))
    W = []
    for j in y:
        word = j*x
        W.append(word)
    
    print("".join(W))