n = int(input())
res = list(input())

bonus = 0
answer = 0
for i in range(n):
    if res[i] == 'O':
        answer += bonus
        bonus += 1
        answer += i+1
    else:
        bonus = 0

print(answer)