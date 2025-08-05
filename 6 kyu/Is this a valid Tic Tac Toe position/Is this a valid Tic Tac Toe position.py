def is_valid_position(board: tuple[tuple[str, ...], ...]) -> bool:
    x_count = sum(row.count('X') for row in board)
    o_count = sum(row.count('O') for row in board)

    if not (x_count == o_count or x_count == o_count + 1):
        return False

    x_wins = any(
        all(cell == 'X' for cell in row) for row in board
    ) or any(
        all(board[i][j] == 'X' for i in range(3)) for j in range(3)
    ) or all(board[i][i] == 'X' for i in range(3)) or all(board[i][2 - i] == 'X' for i in range(3))

    o_wins = any(
        all(cell == 'O' for cell in row) for row in board
    ) or any(
        all(board[i][j] == 'O' for i in range(3)) for j in range(3)
    ) or all(board[i][i] == 'O' for i in range(3)) or all(board[i][2 - i] == 'O' for i in range(3))

    if x_wins and o_wins:
        return False
    if x_wins and x_count != o_count + 1:
        return False
    if o_wins and x_count != o_count:
        return False
    
    return True