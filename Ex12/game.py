#############################################################
# FILE : game.py
# WRITERS : Liron Gershuny , gerliron18 , 308350503
#           Chana Goldstein , c.goldstein , 316556976
# EXERCISE : intro2cs ex12 2017-2018
# DESCRIPTION: The "brain" behind the Four In A Row game
#############################################################

class Game:
    """
    This class represents the "brain" behind the Four In A Row game. It
    creates the board game, and has functions that run the game
    process (such as putting in disks, checking for winners, etc.)

    """
    PLAYER_ONE = 0
    PLAYER_TWO = 1
    DRAW = 2

    NUM_ROWS = 6
    NUM_COL = 7
    EMPTY_SPOT = None
    WINNING_MOVE_PLAYER_ONE = "0000"
    WINNING_MOVE_PLAYER_TWO = "1111"
    COLUMN = 3
    ROW = 4
    DIAGONAL_DOWN_RIGHT = 5
    DIAGONAL_DOWN_LEFT = 6
    ILLEGAL_MOVE = "Illegal move."

    def __init__(self):
        """
        creates a board as a list of lists. Empty spots are represented by
        the value None. Once a spot is occupied, the value changes to either
        0 (if the disk belongs to player one) or 1 (if the disk belongs to
        player two).
        """
        self.__board = [[self.EMPTY_SPOT] * self.NUM_COL for rows in
                        range(self.NUM_ROWS)]

    def make_move(self, column):
        """
        This function manages the process of making a move in the game. It
        checks if the move is legal, if so, it makes the move. If not,
        it raises an exception.
        :param column: A number between 0-6 that represents a column in the
        board.
        :return: None
        """
        if self.is_legal(column):
            player = self.get_current_player()
            row = self.find_row(column)
            self.__board[row][column] = player

        # If illegal move raise an exception
        else:
            raise Exception(self.ILLEGAL_MOVE)

    def find_winning_disks(self, col, row, direction):
        """
        When a winning hand is made, the get_winner_helper returns the
        column, row, and direction that led to the winning hand. This
        function receives these values and finds what the other winning
        disks are.
        :param col: int between 0-6 representing a column on the board
        :param row: int between 0-5 representing a row on the board
        :param direction: an int (with a Magic Number representation) that
        represents in what direction the win was made
        :return: A list of four tuples (col, row) that represent the
        spots in which there is a winning move.
        """
        if direction == self.COLUMN:
            return [(col, row), (col, row - 1), (col, row - 2), (col, row - 3)]

        if direction == self.ROW:
            return [(col, row), (col - 1, row), (col - 2, row), (col - 3, row)]

        if direction == self.DIAGONAL_DOWN_RIGHT:
            return [(col, row), (col - 1, row - 1), (col - 2, row - 2),
                    (col - 3, row - 3)]

        if direction == self.DIAGONAL_DOWN_LEFT:
            return [(col, row), (col + 1, row - 1), (col + 2, row - 2),
                    (col + 3, row - 3)]

    def find_row(self, col):
        """
        Goes through each of the rows in the given column and finds the row in
        which there is already a disk. Returns the row above the occupied spot.
        :param col: int representing the column the disk is supposed to go into
        :return: int representing the row into which the disk should be placed
        """
        for row in range(self.NUM_ROWS):
            if self.__board[row][col] is not None:
                found_row = row - 1
                return found_row

        return self.NUM_ROWS - 1

    def is_legal(self, col):
        """
        Checks if a move is out of the bounds of the board, or if the
        given column is full.
        :return: True - if the move is legal. False - if the move is illegal.
        """

        # checks if col is in the boundaries of the board
        if col >= self.NUM_COL:
            return False

        # checks if col is not full
        for row in range(self.NUM_ROWS):
            if self.__board[row][col] is None:
                return True

        return False

    def check_row_for_winner(self):
        """
        Creates strings of the rows, and then checks if there is a winning
        hand ('0000' or '1111') in the string.
        :return: If there is a winning sequence in a row, the function
        returns True and in addition returns the column and row in which the
        last disk was placed. If there are no rows that have a winning
        sequence in them, the function returns False.
        """

        for row in range(self.NUM_ROWS):
            one_row = ""
            for col in range(self.NUM_COL):
                one_row = one_row + str(self.__board[row][col])
                if self.WINNING_MOVE_PLAYER_ONE in one_row or \
                        self.WINNING_MOVE_PLAYER_TWO in one_row:
                    return True, col, row

        return False

    def check_col_for_winner(self):
        """
        Creates strings of the columns and then checks if there is a winning
        hand ('0000' or '1111') in the string. In order to create the
        strings of the columns, we go over each row, and connect the value
        at that spot to the string prefix one_col.
        :return: If there is a winning sequence in a row, the function
        returns True and in addition returns the column and row in which the
        last disk was placed. If there are no rows that have a winning
        sequence in them, the function returns False.
        """

        for col in range(self.NUM_COL):
            one_col = ""
            for row in range(self.NUM_ROWS):
                one_col = one_col + str(self.__board[row][col])
                if self.WINNING_MOVE_PLAYER_ONE in one_col or \
                        self.WINNING_MOVE_PLAYER_TWO in one_col:
                    return True, col, row

        return False

    def diagonal_to_right(self):
        """
        This function defines the search for winning situations at the board
        diagonals from upper left position to down right position. Will
        search for four similar player disks at this diagonals. Will not
        pay attention to diagonals who as less then four disks in it.
        :return: True/False if there is a winning situation and if it does,
                 it will return also the row and column of the right spot of
                 the sequence
        """

        # All the diagonals from the center to the bottom left corner
        for row in range(3):  # We only need to check until 3, since we are
            # only interested in diagonals that are at least 4 disks long.
            row_count = row
            col_count = 0  # Initialize column counter
            line = ''  # Initialize one string that will include all
            # the diagonal disks

            while row_count < self.NUM_ROWS and col_count < self.NUM_COL:
                # While we have not reach to the board boundaries
                line = line + str(self.__board[row_count][col_count])
                # Add one player disk to the final string
                row_count += 1
                col_count += 1

                if self.WINNING_MOVE_PLAYER_ONE in line or \
                        self.WINNING_MOVE_PLAYER_TWO in line:
                    # Checks if there is a winning sequence
                    return True, col_count - 1, row_count - 1

        # All the diagonals from the center to the top right corner
        for col in range(4):  # We only need to check until 4, since we are
            # only interested in diagonals that are at least 4 disks long.
            row_count = 0  # Initialize row counter
            col_count = col
            line = ''  # Initialize one string that will include all
            # the diagonal disks

            while col_count < self.NUM_COL and row_count < self.NUM_ROWS:
                # While we have not reach to the board boundaries
                line = line + str(self.__board[row_count][col_count])
                # Add one player disk to the final string
                row_count += 1
                col_count += 1

                if self.WINNING_MOVE_PLAYER_ONE in line or \
                        self.WINNING_MOVE_PLAYER_TWO in line:
                    # Checks if there is a winning sequence
                    return True, col_count - 1, row_count - 1

        return False

    def diagonal_to_left(self):
        """
        This function defines the search for winning situations at the board
        diagonals from upper right position to down left position. Will
        search for four similar player disks at this diagonals. Will not
        pay attention to diagonals who as less then four disks in it.
        :return: True/False if there is a winning situation and if it does,
                 it will return also the row and column of the right spot of
                 the sequence
        """

        # All the diagonals from the center to the bottom right corner
        for row in range(3):  # We only need to check until 3, since we are
            # only interested in diagonals that are at least 4 disks long.
            row_count = row
            col_count = self.NUM_COL - 1  # Initialize column counter from the
            # right bound of the board
            line = ''  # Initialize one string that will include all
            # the diagonal disks

            while row_count < self.NUM_ROWS and col_count >= 0:
                # While we have not reach to the board boundaries
                line = line + str(self.__board[row_count][col_count])
                # Add one player disk to the final string
                row_count += 1
                col_count -= 1

                if self.WINNING_MOVE_PLAYER_ONE in line or \
                        self.WINNING_MOVE_PLAYER_TWO in line:
                    # Checks if there is a winning sequence
                    return True, col_count + 1, row_count - 1

        # All the diagonals from the center to the top left corner
        for col in range(self.NUM_COL - 1, 2, -1):  # We only need to check
            # until 2, since we are only interested in diagonals that are
            # at least 4 disks long.
            row_count = 0  # Initialize row counter
            col_count = col
            line = ''  # Initialize one string that will include all
            # the diagonal disks

            while col_count >= 0 and row_count < self.NUM_ROWS:
                # While we have not reach to the board boundaries
                line = line + str(self.__board[row_count][col_count])
                # Add one player disk to the final string
                row_count += 1
                col_count -= 1

                if self.WINNING_MOVE_PLAYER_ONE in line or \
                        self.WINNING_MOVE_PLAYER_TWO in line:
                    # Checks if there is a winning sequence
                    return True, col_count + 1, row_count - 1

        return False

    def get_winner_helper(self):
        """
        Checks if there is a winning sequence on the board, by calling the
        function that check the rows, columns, and diagonals for a winning
        sequence.
        :return: False - if no winning sequence is on the board. If there is
        a winning sequence, it returns True, the row and column in which the
        last disk was placed (the led to the win), and the direction in
        which the win happened.
        """
        if self.check_row_for_winner():
            _, col, row = self.check_row_for_winner()
            return True, col, row, self.ROW

        elif self.check_col_for_winner():
            _, col, row = self.check_col_for_winner()
            return True, col, row, self.COLUMN

        elif self.diagonal_to_left():
            _, col, row = self.diagonal_to_left()
            return True, col, row, self.DIAGONAL_DOWN_LEFT

        elif self.diagonal_to_right():
            _, col, row = self.diagonal_to_right()
            return True, col, row, self.DIAGONAL_DOWN_RIGHT

        return False

    def get_winner(self):
        """
        Checks the status of the game for a win/lose or a draw.
        :return: If there is a win, the function returns which player the
        winner is. If there is a draw, returns that there was a draw. Else,
        returns False.
        """
        player = self.get_current_player()

        if self.get_winner_helper():
            if player == self.PLAYER_ONE:
                return self.PLAYER_TWO
            else:
                return self.PLAYER_ONE

        elif self.is_draw():
            return self.DRAW

        return None

    def is_draw(self):
        """
        The empty spots on the board are represented as None. If there are
        no more Nones in the board that means the board is full. Since
        there wasn't a win, the only other option is that the game
        situation is a draw.
        :return: True - if there is draw situation on the board. Else,
        returns False
        """
        for row in self.__board:
            for col in row:
                if col is None:
                    return False
        return True

    def get_player_at(self, row, col):
        """
        :param row: an int representing a row on the board
        :param col: an int representing a col on the board
        :return: If there is a disk on the given spot, the function returns
        the player who's disk it is. If that spot is empty, it returns None.
        """
        if self.__board[row][col] == self.PLAYER_ONE:
            return self.PLAYER_ONE

        elif self.__board[row][col] == self.PLAYER_TWO:
            return self.PLAYER_TWO

        return None

    def get_current_player(self):
        """
        To find the current player, we count how many empty spots there are
        on the board. If there are an even number of empty spots on the board,
        it means that it's player one's turn. If there are an odd number of
        empty spots on the board, it means it's player two's turn.
        :return: The player who's turn it currently is.
        """
        counter = 0
        for row in range(self.NUM_ROWS):
            for col in range(self.NUM_COL):
                if self.__board[row][col] is None:
                    counter += 1

        if counter % 2 == 0:
            return self.PLAYER_ONE

        return self.PLAYER_TWO

    def get_board(self):
        """
        :return: the game board
        """
        return self.__board
