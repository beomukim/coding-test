from itertools import combinations
n = int(input())
nums = list(map(int, input().split()))
sums = []
for i in range(1, len(nums) + 1):
    com = list(combinations(nums, i))
    for c in com:
        sums.append(sum(c))
answer = sorted(sums)[-1] + 1
for l in list(zip(range(1, len(sums)+1), sorted(set(sums)))):
    if l[0] != l[1]:
        answer = l[0]
        break

print(answer)