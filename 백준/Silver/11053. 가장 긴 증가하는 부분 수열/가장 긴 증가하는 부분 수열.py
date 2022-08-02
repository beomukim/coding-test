n = int(input())
nums = list(map(int, input().split()))
dy = [1] * n

for i in range(1, n):
    for j in range(i-1, -1, -1):
        if nums[j] < nums[i]:
            dy[i] = max(dy[i], dy[j]+1)

print(max(dy))