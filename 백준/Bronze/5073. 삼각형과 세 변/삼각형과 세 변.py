while True:
    nums = list(map(int, input().split()))
    if sum(nums) == 0:
        break
    if len(set(nums)) == 1:
        print("Equilateral")
    elif sum(nums) <= max(nums) * 2:
        print("Invalid")
    elif len(set(nums)) == 2:
        print("Isosceles")
    else:
        print("Scalene")