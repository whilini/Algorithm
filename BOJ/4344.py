a = int(input())

for i in range(a):
    score = list(map(int, input().split()))
    pg = sum(score[1:])/score[0]
    Good = []
    for j in score[1:]:
        if j > pg:        
            Good.append(j)
    
    rate = len(Good)/score[0]*100

    print(str(f'{rate:.3f}') + '%')