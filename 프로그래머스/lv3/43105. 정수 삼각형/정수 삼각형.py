def solution(triangle):
    answer = 0
    dy = [[0] * len(triangle) for _ in range(len(triangle))]
    dy[0][0] = triangle[0][0]
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                dy[i][j] = dy[i-1][j] + triangle[i][j]
            elif j == len(triangle[i]) - 1:
                dy[i][j] = dy[i-1][j-1] + triangle[i][j]
            else:
                dy[i][j] = max(dy[i-1][j], dy[i-1][j-1]) + triangle[i][j]
                
    return max(dy[-1])