from board import board

def valid_board(board):
    """
    Returns if the board is valid
    :param board: 2-d list of ints
    :return: bool
    """
    # Check 9x9 array
    if len(board) != 9:
        return False
    
    for i in range(len(board)):
        if len(board[i]) != 9:
            return False

    # Check rows
    for i in range(len(board)):
        row = sorted(list(filter(lambda a: a != 0, board[i])))
        unique_row = sorted(list(set(row)))
        if row != unique_row:
            return False

    # Check columns
    for i in range(len(board)):
        column = sorted(
            list(filter(lambda a: a != 0, [row[i] for row in board])))
        unique_column = sorted(list(set(column)))
        if column != unique_column:
            return False

    # Check 3x3 boxes
    for i in range(9):
        if i % 3 == 0:
            box_1 = board[i][:3] + board[i + 1][:3] + board[i + 2][:3]
            sorted_box_1 = sorted(list(filter(lambda a: a != 0, box_1)))
            unique_sorted_box_1 = sorted(list(set(sorted_box_1)))
            if sorted_box_1 != unique_sorted_box_1:
                return False

            box_2 = board[i][3:6] + board[i + 1][3:6] + board[i + 2][3:6]
            sorted_box_2 = sorted(list(filter(lambda a: a != 0, box_2)))
            unique_sorted_box_2 = sorted(list(set(sorted_box_2)))
            if sorted_box_2 != unique_sorted_box_2:
                return False

            box_3 = board[i][6:] + board[i + 1][6:] + board[i + 2][6:]
            sorted_box_3 = sorted(list(filter(lambda a: a != 0, box_3)))
            unique_sorted_box_3 = sorted(list(set(sorted_box_3)))
            if sorted_box_3 != unique_sorted_box_3:
                return False

    return True


def solve(board):
    """
    Solves a sudoku board
    :param board: 2-d list of ints
    :return: bool: False if not solvable
    """
    empty = find_empty(board)
    if empty:
        row, col = empty
    else:
        return True

    for i in range(1, 10):
        if valid_move(board, (row, col), i):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False


def valid_move(board, pos, num):
    """
    Returns if the attempted move is valid
    :param board: 2-d list of ints
    :param pos: (row, col) position to inset
    :param num: int to insert
    :return: bool
    """
    # Check row
    for i in range(0, len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check Col
    for i in range(0, len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check 3x3 box
    box_x = pos[1]//3
    box_y = pos[0]//3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True


def find_empty(board):
    """
    Finds the next empty space (indicated by a zero) on the board
    :param board: 2-d list of ints
    :return: (int, int) (row, col)
    """
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)

    return None


def print_board(board):
    """
    Prints the board
    :param board: 2-d list of ints
    :return: None
    """
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(len(board[i])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == len(board[i]) - 1:
                print(board[i][j], end="\n")
            else:
                print(str(board[i][j]) + " ", end="")


print_board(board)
print('\nsolvable: ' + str(valid_board(board)) + '\n')
solve(board)
print_board(board)