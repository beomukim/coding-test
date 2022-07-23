import sys
sys.setrecursionlimit(10**6)
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
low = graph[0][0]
high = graph[0][0]
for i in range(n):
    if min(graph[i]) < low:
        low = min(graph[i])
    if max(graph[i]) > high:
        high = max(graph[i])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(a,b):
    ch[a][b] = 1
    for i in range(4):
        x = a+dx[i]
        y = b+dy[i]

        if 0<=x<n and 0<=y<n and ch[x][y] == 0:
            dfs(x,y)

res = []
for k in range(low-1, high+1):
    cnt = 0
    ch = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] <= k:
                ch[i][j] = 1

    for i in range(n):
        for j in range(n):
            if ch[i][j] == 0:
                dfs(i, j)
                cnt += 1

    res.append(cnt)

print(max(res))

