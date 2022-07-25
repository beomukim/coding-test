from collections import deque
n = int(input())
graph = []
for _ in range(n):
    ch = []
    l = int(input())
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    ch.append(l)
    ch.append((a,b))
    ch.append((c,d))
    graph.append(ch)
dx = [-2, -1, 1, 2, -2, -1, 1, 2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]
def bfs(l, start, end):
    ch = [[0] * l for _ in range(l)]
    q = deque([start])
    ch[start[0]][start[1]] = 1
    while q:
        a, b, = q.popleft()
        if (a,b) == end:
            return ch[a][b]
        else:
            for i in range(8):
                x = a+dx[i]
                y = b+dy[i]
                if 0<=x<l and 0<=y<l and ch[x][y] == 0:
                    ch[x][y] = ch[a][b] + 1
                    q.append((x, y))

for x in graph:
    l = x[0]
    start = x[1]
    end = x[2]
    print(bfs(l, start, end) - 1)