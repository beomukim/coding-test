n = int(input())
l = list(map(int, input().split()))
dy = [0] * n
dy[0] = l[0]
for i in range(1, n):
    m = 0
    for j in range(i-1, -1, -1):
        if l[j] < l[i] and dy[j] > m:
            m = dy[j]

    dy[i] = m + l[i]

print(max(dy))