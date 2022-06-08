from itertools import combinations
n = int(input())
stat = []
for _ in range(n):
    stat.append(list(map(int, input().split())))

answer = 100*20*20
comb = list(combinations(range(n), n // 2))
for i in range(len(comb) // 2):
    team_a = list(comb[i])
    team_b = [b for b in range(n) if not b in team_a]

    comb_a = list(combinations(team_a, 2))
    comb_b = list(combinations(team_b, 2))

    sum_a = 0
    sum_b = 0
    for a in comb_a:
        i, j = a
        sum_a += stat[i][j]
        sum_a += stat[j][i]
    for b in comb_b:
        i, j = b
        sum_b += stat[i][j]
        sum_b += stat[j][i]

    temp_answer = abs(sum_a - sum_b)
    if answer > temp_answer:
        answer = temp_answer

print(answer)