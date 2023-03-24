import sys
sys.setrecursionlimit(int(10e7))
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))

    answer = 0
    check = [[False] * w for _ in range(h)]
    def dfs(i, j):
        if graph[i][j] == 1 and not check[i][j]:
            check[i][j] = True
            dx = [-1, 1, 0, 0, -1, 1, 1, -1]
            dy = [0, 0, -1, 1, -1, 1, -1, 1]
            for k in range(8):
                x = i + dx[k]
                y = j + dy[k]
                if 0<=x<h and 0<=y<w and not check[x][y]:
                    dfs(x, y)

            return True

    for i in range(h):
        for j in range(w):
            if dfs(i, j):
                answer += 1

    print(answer)

