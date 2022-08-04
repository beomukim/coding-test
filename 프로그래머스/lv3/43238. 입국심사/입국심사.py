def solution(n, times):
    answer = 0
    lt = 1
    rt = n * max(times)
    while lt<=rt:
        mid = (lt+rt)//2
        sum = 0
        for t in times:
            sum += mid // t
        
        if sum >= n:
            res = mid
            rt = mid-1
        else:
            lt = mid+1
    return res

