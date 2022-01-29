n = int(input())
d = n 
x = 0

while 1:
    a = d//10
    b = d%10
    c = (a+b)%10
    x+=1
   
    d = b*10+c
    
    if n==d:
        break

print(x)