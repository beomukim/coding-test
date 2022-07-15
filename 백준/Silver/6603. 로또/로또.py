from itertools import combinations
nums = []
while True:
    num = list(map(int, input().split()))
    if len(num) == 1:
        break
    else:
        nums.append(num)

for n in nums:
    k = n[0]
    for c in list(combinations(n[1:],6)):
        print(' '.join(map(str, c)))

    print()