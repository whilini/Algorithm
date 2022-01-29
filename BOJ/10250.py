s = int(input())
a = []
for i in range(s):
    h, w, n = map(int, input().split())
    y = n%h
    x = n//h+1
    if y==0:
        y=h
        x=n//h
    a.append(y*100+x)
for i in a:
    print(i)