import heapq
T, n = map(int, input().split())
heap = []
for i in range(n):
    a, b, c = map(int, input().split())
    heapq.heappush(heap, [-c, a, b])

for _ in range(T):
    now = heapq.heappop(heap)
    print(now[1])

    if now[2] - 1 > 0:
        heapq.heappush(heap, [now[0]+1, now[1], now[2]-1])
