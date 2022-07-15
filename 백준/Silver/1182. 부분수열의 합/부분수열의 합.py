from itertools import combinations
answer = 0
n, s = map(int, input().split())
nums = list(map(int, input().split()))
for i in range(1, len(nums) + 1):
    com = list(combinations(nums, i))
    for n in com:
        if sum(n) == s:
            answer += 1

print(answer)