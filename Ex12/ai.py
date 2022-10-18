#############################################################
# FILE : ai.py
# WRITERS : Liron Gershuny , gerliron18 , 308350503
#           Chana Goldstein , c.goldstein , 316556976
# EXERCISE : intro2cs ex12 2017-2018
# DESCRIPTION: A class that runs the AI functionality
#              of the game Four In A Row
#############################################################
from random import randrange


class AI:
    """
    This class represents an AI player in the game Four In A Row.
    """

    CENTER_COL = 3
    AI_EXCEPTION = "No possible AI moves"

    def find_legal_move(self, g, func, timeout=None):
        """
        Attempts to find a legal move for the AI to implement. First, it tries
        to put a disk in the center column (since that is a basic strategy
        for winning a game of connect four). If not, it get's a random move.
        :param g: A game board.
        :param func: In our case it's the handle_event function from the GUI class.
        :param timeout: None. We aren't doing the bonus, so it's not
        relevant to us.
        :return: None
        """
        try:
            if self.find_center_move(g):
                func(self.CENTER_COL)
            else:
                func(self.random_move(g))
        except Exception(self.AI_EXCEPTION):
            pass

    def find_center_move(self, g):
        """
        :param g: the game board
        :return: True - if putting a disk in the center row is legal. False
        - if the move isn't legal.
        """
        if g.is_legal(self.CENTER_COL):
            return True
        return False

    def random_move(self, g):
        """
        Generates a random move for the AI to implement. If the column it
        generates is not legal, it calls itself recursively and a legal
        column is generated.
        :param g: The game board
        :return: An int representing the column for a disk to be placed.
        """
        col = randrange(0, g.NUM_COL)
        if g.is_legal(col):
            return col
        else:
            return self.random_move(g)
