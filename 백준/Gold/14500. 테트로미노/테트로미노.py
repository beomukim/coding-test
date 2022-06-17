n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
answer = 0
def one(i, j):
    sum = 0
    dx = [0, 1, 2, 3]
    dy = [0, 0, 0, 0]
    for k in range(4):
        x = i + dx[k]
        y = j + dy[k]
        if x < 0 or y < 0 or x >= n or y >= m:
            return 0
        sum += graph[x][y]
    return sum
def two(i, j):
    sum = 0
    dx = [0, 0, 0, 0]
    dy = [0, 1, 2, 3]
    for k in range(4):
        x = i + dx[k]
        y = j + dy[k]
        if x < 0 or y < 0 or x >= n or y >= m:
            return 0
        sum += graph[x][y]
    return sum
def three(i, j):
    sum = 0
    dx = [0, 1, 0, 1]
    dy = [0, 0, 1, 1]
    for k in range(4):
        x = i + dx[k]
        y = j + dy[k]
        if x < 0 or y < 0 or x >= n or y >= m:
            return 0
        sum += graph[x][y]
    return sum
def four(i, j):
    sum = 0
    dx = [0, 1, 2, 2]
    dy = [0, 0, 0, 1]
    for k in range(4):
        x = i + dx[k]
        y = j + dy[k]
        if x < 0 or y < 0 or x >= n or y >= m:
            return 0
        sum += graph[x][y]
    return sum
def five(i, j):
    sum = 0
    dx = [0, 1, 1, 1]
    dy = [0, 0, -1, -2]
    for k in range(4):
        x = i + dx[k]
        y = j + dy[k]
        if x < 0 or y < 0 or x >= n or y >= m:
            return 0
        sum += graph[x][y]
    return sum
def six(i, j):
    sum = 0
    dx = [0, 0, 1, 2]
    dy = [0, 1, 1, 1]
    for k in range(4):
        x = i + dx[k]
        y = j + dy[k]
        if x < 0 or y < 0 or x >= n or y >= m:
            return 0
        sum += graph[x][y]
    return sum
def seven(i, j):
    sum = 0
    dx = [0, -1, -1, -1]
    dy = [0, 0, 1, 2]
    for k in range(4):
        x = i + dx[k]
        y = j + dy[k]
        if x < 0 or y < 0 or x >= n or y >= m:
            return 0
        sum += graph[x][y]
    return sum
def eight(i, j):
    sum = 0
    dx = [0, 0, -1, -2]
    dy = [0, 1, 1, 1]
    for k in range(4):
        x = i + dx[k]
        y = j + dy[k]
        if x < 0 or y < 0 or x >= n or y >= m:
            return 0
        sum += graph[x][y]
    return sum
def nine(i, j):
    sum = 0
    dx = [0, 0, 0, 1]
    dy = [0, 1, 2, 2]
    for k in range(4):
        x = i + dx[k]
        y = j + dy[k]
        if x < 0 or y < 0 or x >= n or y >= m:
            return 0
        sum += graph[x][y]
    return sum
def ten(i, j):
    sum = 0
    dx = [0, -1, -2, -2]
    dy = [0, 0, 0, 1]
    for k in range(4):
        x = i + dx[k]
        y = j + dy[k]
        if x < 0 or y < 0 or x >= n or y >= m:
            return 0
        sum += graph[x][y]
    return sum
def eleven(i, j):
    sum = 0
    dx = [0, 1, 1, 1]
    dy = [0, 0, 1, 2]
    for k in range(4):
        x = i + dx[k]
        y = j + dy[k]
        if x < 0 or y < 0 or x >= n or y >= m:
            return 0
        sum += graph[x][y]
    return sum
def twelve(i, j):
    sum = 0
    dx = [0, 1, 1, 2]
    dy = [0, 0, 1, 1]
    for k in range(4):
        x = i + dx[k]
        y = j + dy[k]
        if x < 0 or y < 0 or x >= n or y >= m:
            return 0
        sum += graph[x][y]
    return sum
def thirteen(i, j):
    sum = 0
    dx = [0, 0, -1, -1]
    dy = [0, 1, 1, 2]
    for k in range(4):
        x = i + dx[k]
        y = j + dy[k]
        if x < 0 or y < 0 or x >= n or y >= m:
            return 0
        sum += graph[x][y]
    return sum
def fourteen(i, j):
    sum = 0
    dx = [0, -1, -1, -2]
    dy = [0, 0, 1, 1]
    for k in range(4):
        x = i + dx[k]
        y = j + dy[k]
        if x < 0 or y < 0 or x >= n or y >= m:
            return 0
        sum += graph[x][y]
    return sum
def fifteen(i, j):
    sum = 0
    dx = [0, 0, 1, 1]
    dy = [0, 1, 1, 2]
    for k in range(4):
        x = i + dx[k]
        y = j + dy[k]
        if x < 0 or y < 0 or x >= n or y >= m:
            return 0
        sum += graph[x][y]
    return sum
def sixteen(i, j):
    sum = 0
    dx = [0, 0, 0, 1]
    dy = [0, 1, 2, 1]
    for k in range(4):
        x = i + dx[k]
        y = j + dy[k]
        if x < 0 or y < 0 or x >= n or y >= m:
            return 0
        sum += graph[x][y]
    return sum
def seventeen(i, j):
    sum = 0
    dx = [0, 1, 2, 1]
    dy = [0, 0, 0, 1]
    for k in range(4):
        x = i + dx[k]
        y = j + dy[k]
        if x < 0 or y < 0 or x >= n or y >= m:
            return 0
        sum += graph[x][y]
    return sum
def eighteen(i, j):
    sum = 0
    dx = [0, 0, 0, -1]
    dy = [0, 1, 2, 1]
    for k in range(4):
        x = i + dx[k]
        y = j + dy[k]
        if x < 0 or y < 0 or x >= n or y >= m:
            return 0
        sum += graph[x][y]
    return sum
def nighteen(i, j):
    dx = [0, 1, 2, 1]
    dy = [0, 0, 0, -1]
    sum = 0
    for k in range(4):
        x = i + dx[k]
        y = j + dy[k]
        if x < 0 or y < 0 or x >= n or y >= m:
            return 0
        sum += graph[x][y]
    return sum

for i in range(n):
    for j in range(m):
        if answer < one(i, j):
            answer = one(i, j)
        if answer < two(i, j):
            answer = two(i, j)
        if answer < three(i, j):
            answer = three(i, j)
        if answer < four(i, j):
            answer = four(i, j)
        if answer < five(i, j):
            answer = five(i, j)
        if answer < six(i, j):
            answer = six(i, j)
        if answer < seven(i, j):
            answer = seven(i, j)
        if answer < eight(i, j):
            answer = eight(i, j)
        if answer < nine(i, j):
            answer = nine(i, j)
        if answer < ten(i, j):
            answer = ten(i, j)
        if answer < eleven(i, j):
            answer = eleven(i, j)
        if answer < twelve(i, j):
            answer = twelve(i, j)
        if answer < thirteen(i, j):
            answer = thirteen(i, j)
        if answer < fourteen(i, j):
            answer = fourteen(i, j)
        if answer < fifteen(i, j):
            answer = fifteen(i, j)
        if answer < sixteen(i, j):
            answer = sixteen(i, j)
        if answer < seventeen(i, j):
            answer = seventeen(i, j)
        if answer < eighteen(i, j):
            answer = eighteen(i, j)
        if answer < nighteen(i, j):
            answer = nighteen(i, j)

print(answer)