n = int(input())
board = [input() for _ in range(n)]

# 두 인덱스의 사탕을 교환하여 얻을 수 있는 최대 사탕 개수를 구한다
def get_max_candies(board, r1, c1, r2, c2):
    # 두 칸의 사탕을 교환한 보드를 만든다
    new_board = [list(row) for row in board]
    new_board[r1][c1], new_board[r2][c2] = new_board[r2][c2], new_board[r1][c1]

    max_candies = 0
    # 행 검사
    for r in range(n):
        count = 1
        for c in range(1, n):
            if new_board[r][c] == new_board[r][c-1]:
                count += 1
            else:
                max_candies = max(max_candies, count)
                count = 1
        max_candies = max(max_candies, count)

    # 열 검사
    for c in range(n):
        count = 1
        for r in range(1, n):
            if new_board[r][c] == new_board[r-1][c]:
                count += 1
            else:
                max_candies = max(max_candies, count)
                count = 1
        max_candies = max(max_candies, count)

    return max_candies

# 모든 행과 열에 대하여 최대 사탕 개수를 구하고, 최댓값을 출력한다
max_candies = 0
for r in range(n):
    for c in range(n):
        if r+1 < n and board[r][c] != board[r+1][c]:
            max_candies = max(max_candies, get_max_candies(board, r, c, r+1, c))
        if c+1 < n and board[r][c] != board[r][c+1]:
            max_candies = max(max_candies, get_max_candies(board, r, c, r, c+1))

print(max_candies)
