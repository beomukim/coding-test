from collections import deque
m, n = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()
ch = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i, j))
            ch[i][j] = 1
while q:
    a, b = q.popleft()
    ch[a][b] = 1
    for i in range(4):
        x = a+dx[i]
        y = b+dy[i]

        if 0<=x<n and 0<=y<m and ch[x][y] == 0 and graph[x][y] == 0:
            q.append((x,y))
            graph[x][y] = graph[a][b] + 1

ans = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(-1)
            exit(0)
        if graph[i][j] > ans:
            ans = graph[i][j]

if ans == 1:
    print(0)
else:
    print(ans-1)