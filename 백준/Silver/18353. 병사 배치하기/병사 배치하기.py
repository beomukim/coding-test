n = int(input())
nums = list(map(int, input().split()))
dy = [0] * n
dy[0] = 1
for i in range(1, n):
    answer = 1
    for j in range(i-1, -1, -1):
        if nums[i] < nums[j]:
            tmp = dy[j] + 1
            if answer < tmp:
                answer = tmp
    dy[i] = answer


print(n - max(dy))