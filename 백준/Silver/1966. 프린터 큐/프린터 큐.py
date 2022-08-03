from collections import deque
# n = deque([1,2,3])
# print(list(zip(n, range(3))))
k = int(input())
for _ in range(k):
    cnt = 0
    n, m = map(int, input().split())
    nums = deque(zip(list(map(int, input().split())), range(n)))
    while True:
        large = max([x[0] for x in nums])
        now = nums.popleft()
        if now[0] != large:
            nums.append(now)
        else:
            cnt += 1
            if now[1] == m:
                print(cnt)
                break