import copy
from itertools import product
n, m = map(int, input().split())
graph_origin = []
for _ in range(n):
    graph_origin.append(list(map(int, input().split())))

graph = copy.deepcopy(graph_origin)
# s = [1,2,3,4]
# print(list(product(s, repeat=5)))

def right(i, j):
    for k in range(j+1, m):
        if graph[i][k] == 6:
            break
        if graph[i][k] != 0:
            continue
        else:
            graph[i][k] = -1

def left(i, j):
    for k in range(j-1, -1, -1):
        if graph[i][k] == 6:
            break
        if graph[i][k] != 0:
            continue
        else:
            graph[i][k] = -1

def down(i, j):
    for k in range(i+1, n):
        if graph[k][j] == 6:
            break
        if graph[k][j] != 0:
            continue
        else:
            graph[k][j] = -1

def up(i, j):
    for k in range(i-1, -1, -1):
        if graph[k][j] == 6:
            break
        if graph[k][j] != 0:
            continue
        else:
            graph[k][j] = -1


def watch(i, j, num, direction):
    if num == 1:
        if direction == 0:
            right(i, j)
        elif direction == 1:
            left(i, j)
        elif direction == 2:
            up(i, j)
        elif direction == 3:
            down(i, j)
    elif num == 2:
        if direction == 0 or direction == 2:
            right(i, j)
            left(i, j)
        elif direction == 1 or direction == 3:
            up(i, j)
            down(i, j)
    elif num == 3:
        if direction == 0:
            up(i, j)
            right(i ,j)
        elif direction == 1:
            right(i, j)
            down(i, j)
        elif direction == 2:
            down(i, j)
            left(i, j)
        elif direction == 3:
            left(i, j)
            up(i, j)
    elif num == 4:
        if direction == 0:
            up(i, j)
            right(i, j)
            down(i, j)
        elif direction == 1:
            right(i, j)
            down(i, j)
            left(i ,j)
        elif direction == 2:
            down(i, j)
            left(i, j)
            up(i, j)
        elif direction == 3:
            left(i, j)
            up(i, j)
            right(i, j)
    elif num == 5:
        left(i, j)
        up(i, j)
        right(i, j)
        down(i, j)

cctv = []
for i in range(n):
    for j in range(m):
        if graph[i][j] != 0 and graph[i][j] != 6:
            cctv.append((graph[i][j], i, j))

def blind():
    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                count += 1

    return count

answer = n * m
for i in list(product(range(4), repeat=len(cctv))):
    for j in range(len(cctv)):
        watch(cctv[j][1], cctv[j][2], cctv[j][0], i[j])

    if blind() < answer:
        answer = blind()
    graph = copy.deepcopy(graph_origin)


print(answer)
