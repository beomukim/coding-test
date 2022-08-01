k, n = map(int, input().split())
lope = []
for _ in range(k):
    lope.append(int(input()))

lt = 0
rt = max(lope)

while lt<=rt:
    mid = (lt+rt)//2
    if mid == 0:
        print(1)
        exit(0)
    tmp = 0
    for i in lope:
        tmp += i // mid

    if tmp < n:
        rt = mid - 1
    else:
        lt = mid + 1

print(rt)
