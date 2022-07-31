import copy
from itertools import combinations
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(input().split()))
res = True
def dfs(a, b, i):
    global res
    if not 0<=a<n:
        return
    if not 0<=b<n:
        return
    if graph_list[a][b] == 'O':
        return
    if graph_list[a][b] == 'S':
        res = False
        return
    if res:
        if i == 0:
            dfs(a, b+1, i)
        if i == 1:
            dfs(a, b-1, i)
        if i == 2:
            dfs(a+1, b, i)
        if i == 3:
            dfs(a-1, b, i)

zero = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'X':
            zero.append((i,j))

for z in list(combinations(zero, 3)):
    graph_list = copy.deepcopy(graph)

    for i in range(3):
        a, b = z[i]
        graph_list[a][b] = 'O'

    for i in range(n):
        for j in range(n):
            if graph_list[i][j] == 'T':
                for k in range(4):
                    dfs(i, j, k)

    if res:
        print('YES')
        exit(0)
    res = True

print('NO')