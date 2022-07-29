from collections import deque
def solution(maps):
    answer = 0
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 1:
                maps[i][j] = 0
            else:
                maps[i][j] = -1
    maps[0][0] = 1
    maps[-1][-1] = 0
    q = deque([(0,0)])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        a, b = q.popleft()
        if a == len(maps) - 1 and b == len(maps[0]) - 1:
            answer = maps[a][b]
            break
        for i in range(4):
            x = a+dx[i]
            y = b+dy[i]
            if 0<=x<len(maps) and 0<=y<len(maps[0]) and maps[x][y] == 0:
                q.append((x,y))
                maps[x][y] = maps[a][b] + 1
    if answer == 0:
        return -1
    return answer