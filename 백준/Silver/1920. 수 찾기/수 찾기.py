n = int(input())
nums = list(map(int, input().split()))
nums.sort()
m = int(input())
k = list(map(int, input().split()))
for x in k:
    isTrue = False
    lt = 0
    rt = n-1
    while lt<=rt:
        mid = (lt+rt)//2
        if nums[mid] < x:
            lt = mid+1
        elif nums[mid] > x:
            rt = mid-1
        else:
            print(1)
            isTrue = True
            break
    if not isTrue:
        print(0)

