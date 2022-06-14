from collections import deque
n = int(input())
graph = [[0] * n for _ in range(n)]
graph[0][0] = 1
k = int(input())
for _ in range(k):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 2

l = int(input())
turn = deque([])
tail_turn = deque([])
for _ in range(l):
    a, b = input().split()
    turn.append((int(a), b))
answer = 0
k = [0, 0]
tail = [0, 0]
direction = 0
tail_direction = 0
while True:
    if direction == 0:
        x, y = k
        if y+1 >= n or graph[x][y+1] == 1:
            break
        k[1] = y+1
        if graph[x][y+1] != 2:
            if tail_direction == 0:
                graph[tail[0]][tail[1]] = 0
                tail[1] += 1
                graph[tail[0]][tail[1]] = 1
            if tail_direction == 1:
                graph[tail[0]][tail[1]] = 0
                tail[0] += 1
                graph[tail[0]][tail[1]] = 1
            if tail_direction == 2:
                graph[tail[0]][tail[1]] = 0
                tail[1] -= 1
                graph[tail[0]][tail[1]] = 1
            if tail_direction == 3:
                graph[tail[0]][tail[1]] = 0
                tail[0] -= 1
                graph[tail[0]][tail[1]] = 1

        graph[x][y+1] = 1
        answer += 1
    elif direction == 1:
        x, y = k
        if x + 1 >= n or graph[x+1][y] == 1:
            break
        k[0] = x+1
        if graph[x+1][y] != 2:
            if tail_direction == 0:
                graph[tail[0]][tail[1]] = 0
                tail[1] += 1
                graph[tail[0]][tail[1]] = 1
            if tail_direction == 1:
                graph[tail[0]][tail[1]] = 0
                tail[0] += 1
                graph[tail[0]][tail[1]] = 1
            if tail_direction == 2:
                graph[tail[0]][tail[1]] = 0
                tail[1] -= 1
                graph[tail[0]][tail[1]] = 1
            if tail_direction == 3:
                graph[tail[0]][tail[1]] = 0
                tail[0] -= 1
                graph[tail[0]][tail[1]] = 1
        graph[x+1][y] = 1
        answer += 1
    elif direction == 2:
        x, y = k
        if y - 1 < 0 or graph[x][y - 1] == 1:
            break
        k[1] = y - 1
        if graph[x][y - 1] != 2:
            if tail_direction == 0:
                graph[tail[0]][tail[1]] = 0
                tail[1] += 1
                graph[tail[0]][tail[1]] = 1
            if tail_direction == 1:
                graph[tail[0]][tail[1]] = 0
                tail[0] += 1
                graph[tail[0]][tail[1]] = 1
            if tail_direction == 2:
                graph[tail[0]][tail[1]] = 0
                tail[1] -= 1
                graph[tail[0]][tail[1]] = 1
            if tail_direction == 3:
                graph[tail[0]][tail[1]] = 0
                tail[0] -= 1
                graph[tail[0]][tail[1]] = 1
        graph[x][y - 1] = 1
        answer += 1
    elif direction == 3:
        x, y = k
        if x - 1 < 0 or graph[x - 1][y] == 1:
            break
        k[0] = x - 1
        if graph[x - 1][y] != 2:
            if tail_direction == 0:
                graph[tail[0]][tail[1]] = 0
                tail[1] += 1
                graph[tail[0]][tail[1]] = 1
            if tail_direction == 1:
                graph[tail[0]][tail[1]] = 0
                tail[0] += 1
                graph[tail[0]][tail[1]] = 1
            if tail_direction == 2:
                graph[tail[0]][tail[1]] = 0
                tail[1] -= 1
                graph[tail[0]][tail[1]] = 1
            if tail_direction == 3:
                graph[tail[0]][tail[1]] = 0
                tail[0] -= 1
                graph[tail[0]][tail[1]] = 1
        graph[x - 1][y] = 1
        answer += 1

    if turn:
        t = turn[0]
        if answer == t[0]:
            if t[1] == 'D':
                direction = (direction+1) % 4
                tail_turn.append((k[0], k[1], 'D'))
            if t[1] == 'L':
                direction = (direction-1) % 4
                tail_turn.append((k[0], k[1], 'L'))

            turn.popleft()

    if tail_turn:
        t = tail_turn[0]
        if tail[0] == t[0] and tail[1] == t[1]:
            if t[2] == 'D':
                tail_direction = (tail_direction+1) % 4
            if t[2] == 'L':
                tail_direction = (tail_direction-1) % 4

            tail_turn.popleft()

    
print(answer+1)