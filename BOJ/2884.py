x, y = list(map(int, input().split()))

if x>0 and y<45:
    print(x-1, y+15, end=' ')
if x>0 and y>=45:
    print(x, y-45, end=' ')

if x==0 and y>=45:
    print(0, y-45, end=' ')
if x==0 and y<45:
    print(23, y+15, end=' ')
    