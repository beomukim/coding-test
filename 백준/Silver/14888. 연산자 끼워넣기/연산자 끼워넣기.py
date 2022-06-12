import math
from itertools import permutations
n = int(input())
nums = list(map(int, input().split()))
operations = list(map(int, input().split()))
operations_symbol = []
operations_symbol += ['+'] * operations[0]
operations_symbol += ['-'] * operations[1]
operations_symbol += ['*'] * operations[2]
operations_symbol += ['%'] * operations[3]
operations_symbol = set(permutations(operations_symbol, n-1))
answer = []
for operation in operations_symbol:
    num = nums[0]
    for i in range(n-1):
        if operation[i] == '+':
            num += nums[i+1]
        if operation[i] == '-':
            num -= nums[i + 1]
        if operation[i] == '*':
            num *= nums[i + 1]
        if operation[i] == '%':
            if num <= 0:
                num = math.ceil(num / nums[i+1])
            else:
                num //= nums[i + 1]

    answer.append(num)

print(max(answer))
print(min(answer))