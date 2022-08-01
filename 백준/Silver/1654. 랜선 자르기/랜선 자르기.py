k, n = map(int, input().split())
lope = []
for _ in range(k):
    lope.append(int(input()))

lt = 1
rt = max(lope)

while lt<=rt:
    mid = (lt+rt)//2
    tmp = 0
    for i in lope:
        tmp += i // mid

    if tmp >= n:
        res = mid
        lt = mid+1
    else:
        rt = mid-1

print(res)
