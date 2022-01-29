a = int(input())
b = int(input())
c = int(input())

R = list(str(a*b*c))

for i in range(10):
    print(R.count(str(i)))