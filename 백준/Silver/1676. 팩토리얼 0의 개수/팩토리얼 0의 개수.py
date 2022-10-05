import math
def solution(n):
    if n < 5:
        return 0
    else:
        answer = 0
        while n != 0:
            n //= 5
            answer += n
        return answer

n = int(input())
print(solution(n))
