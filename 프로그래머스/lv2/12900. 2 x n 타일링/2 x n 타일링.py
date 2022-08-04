def solution(n):
    answer = 0
    dy = [0] * (n+1)
    dy[0] = 1
    dy[1] = 1
    for i in range(2, n+1):
        dy[i] = dy[i-1] + dy[i-2] % 1000000007
    return dy[n] % 1000000007