def solve(board, row):
    if row == 8:
        for r in board:
            print(" ".join("Q" if x else "." for x in r))
        return True

    for col in range(8):
        if all(board[i][col] == 0 and
               abs(row-i) != abs(col-j)
               for i in range(row) for j in range(8)
               if board[i][j]):
            
            board[row][col] = 1

            if solve(board, row + 1):
                return True

            board[row][col] = 0

    return False

board = [[0] * 8 for _ in range(8)]
solve(board, 0)