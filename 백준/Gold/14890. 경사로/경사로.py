n, l = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

visited = []
def check(i):
    for j in range(n-1):
        k = j + l
        step = graph[i][j]
        if step - graph[i][j+1] > 1:
            return False
        if graph[i][j+1] == step - 1:
            if k >= n:
                return False
            for m in range(j+1, k+1):
                if (i,m) in visited:
                    return False
                if graph[i][m] != step - 1:
                    return False
                else:
                    visited.append((i, m))
    return True

def check2(i):
    for j in range(n-1, 0, -1):
        k = j - l
        step = graph[i][j]
        if step - graph[i][j-1] > 1:
            return False
        if graph[i][j-1] == step - 1:
            if k < 0:
                return False
            for m in range(j-1, k-1, -1):
                if (i,m) in visited:
                    return False
                if graph[i][m] != step - 1:
                    return False
                else:
                    visited.append((i, m))
    return True

answer = 0
for i in range(n):
    if check(i):
        if check2(i):
            answer += 1


graph = list(map(list, zip(*graph)))
visited = []
for i in range(n):
    if check(i):
        if check2(i):
            answer += 1

print(answer)