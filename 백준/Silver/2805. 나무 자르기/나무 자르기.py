n, m = map(int, input().split())
trees = list(map(int, input().split()))
def count(l):
    sum = 0
    for x in trees:
        if x > l:
            sum += x-l
    return sum
lt = 0
rt = max(trees)
while lt<=rt:
    mid = (lt+rt)//2

    if count(mid) >= m:
        res = mid
        lt = mid+1
    else:
        rt = mid-1
print(res)