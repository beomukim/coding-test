n = int(input())
body = [list(map(int, input().split())) for _ in range(n)]
def check(b):
    weight, height = b[0], b[1]
    res = 1
    for x in body:
        if weight < x[0] and height < x[1]:
            res += 1
    return res

answer = []
for b in body:
    answer.append(check(b))
print(*answer)