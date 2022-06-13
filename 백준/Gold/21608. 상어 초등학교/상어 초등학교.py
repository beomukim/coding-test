from collections import defaultdict
n = int(input())
favorite = []
for _ in range(n**2):
    favorite.append(list(map(int, input().split())))

graph = [[0] * n for _ in range(n)]
like = defaultdict(list)
for f in favorite:
    like[f[0]] = f[1:]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def one(i, j, student):
    count = 0
    for k in range(4):
        x = i + dx[k]
        y = j + dy[k]
        if x < 0 or y < 0 or x >= n or y >= n:
            continue

        if graph[x][y] in like[student]:
            count += 1

    return count

def two(i, j):
    count = 0
    for k in range(4):
        x = i + dx[k]
        y = j + dy[k]
        if x < 0 or y < 0 or x >= n or y >= n:
            continue

        if graph[x][y] == 0:
            count += 1

    return count
for f in favorite:
    student = f[0]
    empty = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 0:
                empty.append((i, j))

    empty.sort(key=lambda x: x[1], reverse=True)
    empty.sort(key=lambda x: x[0], reverse=True)
    empty.sort(key=lambda x: two(x[0], x[1]))
    empty.sort(key=lambda x: one(x[0], x[1], student))
    spot = empty[-1]
    graph[spot[0]][spot[1]] = student
answer = 0
for i in range(n):
    for j in range(n):
        if one(i, j, graph[i][j]) == 1:
            answer += 1
        if one(i, j, graph[i][j]) == 2:
            answer += 10
        if one(i, j, graph[i][j]) == 3:
            answer += 100
        if one(i, j, graph[i][j]) == 4:
            answer += 1000

print(answer)