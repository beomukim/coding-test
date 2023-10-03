import math

n = int(input())
nums = list(map(int, input().split()))
b, c = map(int, input().split())
answer = 0
for num in nums:
        answer += 1
        num -= b
        if num > 0:
                answer += math.ceil(num / c)

print(answer)