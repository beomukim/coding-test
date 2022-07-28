from collections import deque
m, n, h = map(int, input().split())
graph = []
for _ in range(h):
    tmp = []
    for _ in range(n):
        tmp.append(list(map(int, input().split())))
    graph.append(tmp)
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dh = [0, 0, 0, 0, 1, -1]

q = deque()
ch = [[[0] * m for _ in range(n)] for _ in range(h)]
for k in range(h):
    for i in range(n):
        for j in range(m):
            if graph[k][i][j] == 1:
                q.append((k, i, j))
                ch[k][i][j] = 1
while q:
    c, a, b = q.popleft()
    ch[c][a][b] = 1
    for i in range(6):
        x = a+dx[i]
        y = b+dy[i]
        z = c+dh[i]
        if 0<=x<n and 0<=y<m and 0<=z<h and ch[z][x][y] == 0 and graph[z][x][y] == 0:
            q.append((z,x,y))
            graph[z][x][y] = graph[c][a][b] + 1

ans = 0
for k in range(h):
    for i in range(n):
        for j in range(m):
            if graph[k][i][j] == 0:
                print(-1)
                exit(0)
            if graph[k][i][j] > ans:
                ans = graph[k][i][j]

if ans == 1:
    print(0)
else:
    print(ans-1)