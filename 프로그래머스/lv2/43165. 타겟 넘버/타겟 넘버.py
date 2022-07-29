def solution(numbers, target):
    global answer
    answer = 0
    ch = [0] * len(numbers)
    def dfs(v, sum):
        global answer
        if v == len(numbers):
            if sum == target:
                answer += 1
        else:
            dfs(v+1, sum+numbers[v])
            dfs(v+1, sum-numbers[v])
    dfs(0, 0)
    return answer
