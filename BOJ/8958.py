n = int(input())

for i in range(n):
    ox = list(input())
    score = 0
    sum_score = 0
    
    for s in ox:
        if s == 'O':
            score += 1
            sum_score += score
        elif s =='X':
            score = 0
        
    print(sum_score)