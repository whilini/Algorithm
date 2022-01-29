n = int(input())

k=0
s=0
while n>s:
    k+=1
    s+=k
if k%2==0:
    x = n - sum(range(k))
    y = k + 1 - x   
elif k%2==1:
    y = n - sum(range(k))
    x = k + 1 - y
            
print(str(x) + '/' + str(y))