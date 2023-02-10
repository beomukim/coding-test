import sys
sys.setrecursionlimit(10**5)

def solution(maps):
    check = [[False] * len(maps[0]) for _ in range(len(maps))]

    def bfs(i, j, total):
        total += int(maps[i][j])
        check[i][j] = True
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for k in range(4):
            x = i + dx[k]
            y = j + dy[k]
            if 0<=x<len(maps) and 0<=y<len(maps[0]) and not check[x][y] and maps[x][y] != 'X':
                total = bfs(x, y, total)

        return total
    
    result = []
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != 'X' and not check[i][j]:
                result.append(bfs(i, j, 0))
    if not result:
        return [-1]
    return sorted(result)