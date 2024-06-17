

def import_board(path):
    board = []
    with open(path, 'r') as f:
        for line in f:
            if line[:4] == 'Grid':
                continue
            row = [int(x) for x in line.strip()]
            board.append(row)
    return board

def is_valid_move(board, row, col, number):
    # Check the rows and columns
    for i in range(9):
        if board[row][i] == number or board[i][col] == number:
            return False
        
    # Check the 3x3 grid
    start_row = row - row % 3
    start_col = col - col % 3

    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == number:
                return False
            
    return True

def get_valid_numbers(board):
    valid_numbers = [[[] for _ in range(9)] for _ in range(9)]

    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for number in range(1, 10):
                    if is_valid_move(board, row, col, number):
                        valid_numbers[row][col].append(number)

    return valid_numbers

def make_known_moves_from_valid_numbers(board, valid_numbers):
    for row in range(9):
        for col in range(9):
            if len(valid_numbers[row][col]) == 1:
                board[row][col] = valid_numbers[row][col][0]
                logging.debug(f"Setting {row}, {col} to {valid_numbers[row][col][0]}")

    return board

def make_known_moves(board):
    valid_numbers = get_valid_numbers(board)
    new_board = make_known_moves_from_valid_numbers(board, valid_numbers)

    while new_board != board:
        board = new_board
        valid_numbers = get_valid_numbers(board)
        new_board = make_known_moves_from_valid_numbers(board, valid_numbers)

    return new_board, valid_numbers


if __name__ == '__main__':
    board = import_board('096.txt')
    for row in board:
        print(row)

    new_board = make_known_moves(board)

    for row in new_board:
        print(row)