n, c = map(int, input().split())
network = []
for _ in range(n):
    network.append(int(input()))
network.sort()
lt = 1
rt = network[-1]
def count(l):
    tmp = network[0]
    cnt = 1
    for i in range(1, n):
        if network[i] - tmp >= l:
            cnt += 1
            tmp = network[i]

    return cnt
while lt<=rt:
    mid = (lt+rt)//2

    if count(mid) >= c:
        res = mid
        lt = mid+1
    else:
        rt = mid-1

print(res)
