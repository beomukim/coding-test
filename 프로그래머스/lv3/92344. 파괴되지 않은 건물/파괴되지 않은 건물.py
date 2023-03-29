def solution(board, skill):
    answer = 0
    diff = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]
    for type, r1, c1, r2, c2, degree in skill:
        d = -degree if type == 1 else degree
        diff[r1][c1] += d
        diff[r1][c2 + 1] += -d
        diff[r2 + 1][c1] += -d
        diff[r2 + 1][c2 + 1] += d
    
    for i in range(len(board)):
        for j in range(1, len(board[0])):
            diff[i][j] += diff[i][j-1]
    
    for i in range(len(board[0])):
        for j in range(1, len(board)):
            diff[j][i] += diff[j-1][i]
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += diff[i][j]
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] > 0:
                answer += 1
    return answer