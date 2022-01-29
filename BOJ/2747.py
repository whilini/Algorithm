n=int(input())
P=[0]*46
P[1]=1
def pibo(n):
    if n<=1:
        return P[n]
    if P[n] :
        return P[n]
    P[n]=pibo(n-1)+pibo(n-2)   
    return P[n]
print(pibo(n))