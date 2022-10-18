#############################################################
# FILE : ex11_sudoku.py
# WRITER : Liron Gershuny , gerliron18 , 308350503
# EXERCISE : intro2cs ex11 2017-2018
# DESCRIPTION: A program that uses backtracking method
# to solve a sudoku game.
#############################################################
from ex11_backtrack import general_backtracking

EMPTY_CHAR = 0


def print_board(board, board_size=9):
    """ prints a sudoku board to the screen

    ---  board should be implemented as a dictinary 
         that points from a location to a number {(row,col):num}
    """
    for row in range(board_size):
        if (row % 3 == 0):
            print('-------------')
        toPrint = ''
        for col in range(board_size):
            if (col % 3 == 0):
                toPrint += '|'
            toPrint += str(board[(row, col)])
        toPrint += '|'
        print(toPrint)
    print('-------------')


def load_game(sudoku_file):
    """
    A function uses to load to the program a new sudoku board
    so it could work with it.
    :param sudoku_file: A template of not solved sudoku board
    :return: A dictionary that as coordinates of the matrix as
             the keys and the coordinate value as values.
    """
    sudoku_dic = {}
    with open(sudoku_file) as board:
        for row, single_row in enumerate(board):
            single_row = single_row.strip()
            single_row = single_row.split(",")
            for column, num in enumerate(single_row):
                sudoku_dic[(row, column)] = num
    return sudoku_dic


def convert_board_to_lists(board):
    """
    A function uses to convert the sudoku dictionary to a list
    of lists.
    :param board: A dictionary that as coordinates of the matrix as
           the keys and the coordinate value as values.
    :return: A list of lists represents the given sudoku board.
    """
    board_list = []
    for i in range(1, 10):
        board_list.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
    for key in sorted(board):
        value = int(board[key])
        row, column = key
        board_list[row][column] = int(value)
    return board_list


def row_checker(board_list, check_row, check_value):
    """
    A function that check if given row at the sudoku board
    is legal, means every char appear once in the row.
    :param board_list: A list of lists represents the given sudoku board.
    :param check_row: The row at the board that should be checked
    :param check_value: The assignment value being checked
    :return: True/False according to the row legitimacy
    """
    counter = 0
    for char in board_list[check_row]:
        if check_value == char:
            counter += 1
    if counter >= 2:  # If one char appear more than one time at the row
        return False
    return True


def column_checker(board_list, check_column, check_value):
    """
    A function that check if given column at the sudoku board
    is legal, means every char appear once in the column.
    :param board_list: A list of lists represents the given sudoku board.
    :param check_column: The column at the board that should be checked
    :param check_value: The assignment value being checked
    :return: True/False according to the column legitimacy
    """
    counter = 0
    for row in range(0, 9):
        if check_value == board_list[row][check_column]:
            counter += 1
    if counter >= 2:  # If one char appear more than one time at the column
        return False
    return True


def square_checker(board_list, check_row, check_column, check_value):
    """
    A function that check if given 3*3 square at the sudoku board
    is legal, means every char appear once in the square.
    :param board_list: A list of lists represents the given sudoku board.
    :param check_row: The row at the current square that should be checked
    :param check_column: The column at the current square
        that should be checked
    :param check_value: The assignment value being checked
    :return: True/False according to the square legitimacy
    """
    start_row = 0
    start_column = 0
    # Check which of the 3*3 square in the board should be checked
    if check_row % 3 == 0:
        start_row = check_row
    if check_row % 3 == 1:
        start_row = check_row - 1
    if check_row % 3 == 2:
        start_row = check_row - 2
    if check_column % 3 == 0:
        start_column = check_column
    if check_column % 3 == 1:
        start_column = check_column - 1
    if check_column % 3 == 2:
        start_column = check_column - 2
    for row in range(start_row, start_row + 3):
        for column in range(start_column, start_column + 3):
            if row == check_row and column == check_column:
                # If we are checking the assignment
                continue
            if board_list[row][column] == check_value:
                return False
    return True


def check_board(board, x, *args):
    """
    A function that manage all the checks should be done when the main
    backtracking function try to make any assignment at the board.
    :param board: A dictionary that as coordinates of the matrix as
           the keys and the coordinate value as values.
    :param x: A tuple represents the location on the board, row and column
    :param args: If the general backtracking function decide to send
           some more arguments it will get it.
    :return: True/False if the given assignment is legal at the current
             position of the sudoku board.
    """
    board_list = convert_board_to_lists(board)
    # Use helper function to convert the dictionary
    # of the board to list of lists
    check_row = x[0]
    check_column = x[1]
    check_value = int(board[x])
    if row_checker(board_list, check_row, check_value):
        if column_checker(board_list, check_column, check_value):
            if square_checker(board_list, check_row, check_column,
                              check_value):
                return True
    return False


def create_list_of_items(board_dic):
    """
    A function that given the sudoku board, it should bring up
    all the coordinates that has no assignment and should get some.
    :param board_dic: A dictionary that as coordinates of the matrix as
           the keys and the coordinate value as values.
    :return: A list of coordinates from the sudoku board that as no
             assignment the the moment and should get some.
    """
    items_list = []
    for key, value in board_dic.items():
        if int(value) == EMPTY_CHAR:
            items_list.append(key)
    return items_list


def run_game(sudoku_file, print_mode=False):
    """
    A function that tries to solve a sudoku problem using method
    of backtracking.
    :param sudoku_file: A template of sudoku board that the user want
           to solve.
    :param print_mode: The mode if the board as been solved or not
           and decide if it should be printed back.
    :return: True/False if the given sudoku board as any solution.
             If it has a solution the solved board will be printed.
    """
    board_dic = load_game(sudoku_file)
    items_list = create_list_of_items(board_dic)
    set_of_assignments = range(1, 10)
    items_list.sort()
    if general_backtracking(items_list, board_dic, 0, set_of_assignments,
                            check_board):
        # Call backtracking function from anouther program
        print_board(board_dic)
        return True
    return False
