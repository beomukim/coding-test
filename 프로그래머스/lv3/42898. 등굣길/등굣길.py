def solution(m, n, puddles):
    graph = [[0] * m for _ in range(n)]
    graph[0][0] = 1
    dx = [-1, 0]
    dy = [0, -1]
    for i in range(n):
        for j in range(m):
            if [j+1, i+1] in puddles or i == 0 and j == 0:
                continue
            tmp = []
            for k in range(2):
                x = i+dx[k]
                y = j+dy[k]
                if 0<=x<n and 0<=y<m:
                    tmp.append(graph[x][y])

            graph[i][j] = sum(tmp)
    print(graph)
    return graph[n-1][m-1] % 1000000007