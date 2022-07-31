n = int(input())
nums = []
for _ in range(n):
    nums.append(list(map(int, input().split())))
dy = [[0] * n for _ in range(n)]
dy[0][0] = nums[0][0]
for i in range(1, n):
    for j in range(len(nums[i])):
        if j == 0:
            dy[i][j] = dy[i-1][j] + nums[i][j]
        elif j == len(nums[i]) - 1:
            dy[i][j] = dy[i-1][j-1] + nums[i][j]
        else:
            dy[i][j] = max(dy[i-1][j], dy[i-1][j-1]) + nums[i][j]
print(max(dy[-1]))
