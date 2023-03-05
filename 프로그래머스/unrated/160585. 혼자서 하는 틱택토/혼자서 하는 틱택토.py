def solution(board):
    first = 0
    second = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O':
                first += 1
            if board[i][j] == 'X':
                second += 1
    
    if second > first or first - second > 1:
        return 0
    
    def first_wins():
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] and board[i][0] == "O":
                return True
            if board[0][i] == board[1][i] == board[2][i] and board[0][i] == "O":
                return True
        if board[0][0] == board[1][1] == board[2][2] and board[0][0] == "O":
            return True
        if board[0][2] == board[1][1] == board[2][0] and board[0][2] == "O":
            return True
        
    def second_wins():
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] and board[i][0] == "X":
                return True
            if board[0][i] == board[1][i] == board[2][i] and board[0][i] == "X":
                return True
        if board[0][0] == board[1][1] == board[2][2] and board[0][0] == "X":
            return True
        if board[0][2] == board[1][1] == board[2][0] and board[0][2] == "X":
            return True
    
    if first_wins() and first == second:
        return 0
    
    if second_wins() and first > second:
        return 0
    
    
    
    return 1
    
    
            
                