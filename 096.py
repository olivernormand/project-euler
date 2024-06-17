import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

"""
Let's just make the simplest possible recursive solver for this problem.
Even thought it makes me feel sad. 
"""

def same_row(i, j):
    return i // 9 == j // 9

def same_col(i, j):
    return (i - j) % 9 == 0

def same_block(i, j):
    return i // 27 == j // 27 and i % 9 // 3 == j % 9 // 3

def import_board(path):
    board = ""
    with open(path, 'r') as f:
        for line in f:
            if line[:4] == 'Grid':
                continue
            row = line.strip().replace(" ", "")
            board += row
    return board

def recursive_solver(a):

    i = a.find('0')

    if i == -1:
        return a
    
    excluded_numbers = set()
    for j in range(81):
        if same_row(i, j) or same_col(i, j) or same_block(i, j):
            excluded_numbers.add(a[j])

    for m in '123456789':
        if m not in excluded_numbers:
            new_board = a[:i] + m + a[i + 1:]
            # print(new_board.replace('0', '.'))
            result = recursive_solver(new_board)
            if result:
                return result              

def pretty_print_board(board):
    for i in range(9):
        print(board[i * 9: i * 9 + 9])

if __name__ == '__main__':

    board = import_board('096.txt')
    boards = [board[i:i+81] for i in range(0, len(board), 81)]

    solved_boards = []
    
    for i, board in enumerate(boards):
        print("Board: ", i + 1)
        
        pretty_print_board(board)
        solved_board = recursive_solver(board)
        solved_boards.append(solved_board)
        pretty_print_board(solved_board)

    top_left_sum = 0

    for i in range(50):
        top_left_sum += int(solved_boards[i][0:3])

    print(top_left_sum)
