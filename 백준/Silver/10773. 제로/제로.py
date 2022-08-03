n = int(input())
nums = []
for _ in range(n):
    num = int(input())
    if num == 0:
        nums.pop()
    else:
        nums.append(num)
print(sum(nums))