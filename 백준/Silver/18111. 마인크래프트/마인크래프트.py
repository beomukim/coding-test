import sys

n, m, b = map(int, input().split())
ground = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

min_time, max_height = float('inf'), -1
for height in range(257):
    blocks, time = b, 0
    for i in range(n):
        for j in range(m):
            diff = ground[i][j] - height
            if diff > 0:
                # 블록을 땅에서 제거
                time += diff * 2
                blocks += diff
            elif diff < 0:
                # 블록을 땅에 쌓음
                time -= diff
                blocks += diff
    if blocks >= 0 and time <= min_time:
        min_time = time
        max_height = height

print(min_time, max_height)
