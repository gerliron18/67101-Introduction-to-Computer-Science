#############################################################
# FILE : four_in_a_row.py
# WRITERS : Liron Gershuny , gerliron18 , 308350503
#           Chana Goldstein , c.goldstein , 316556976
# EXERCISE : intro2cs ex12 2017-2018
# DESCRIPTION: This script include the main function to
#              initialize on four in a row game. It including
#              the GUI class.
#############################################################
import tkinter as tk
from ai import AI
from game import Game
from communicator import *
import sys

PLAYER_TYPE = 1
PORT_NUM = 2
IP_NUM = 3
SERVER_NUM_ARGS = 3
CLIENT_NUM_ARGS = 4
HUMAN = "human"
AI_PLAYER = "ai"
ROOT_TITLE_SERVER = "Four In A Row (server)"
ROOT_TITLE_CLIENT = "Four In A Row (client)"
ILLEGAL_ARGS_MSG = "Illegal program arguments."

TITLE_SIZE = 90
CANVAS_WIDTH = 560
CANVAS_HEIGHT = 480
OVAL_DIAMETER = 80
MSG_SIZE = 70
MAX_PORT_NUM = 65535

WELCOME_MSG = "Welcome to the game Connect Four!"
INSTRUCTION_MSG = "It's your turn to start the game. \n Click anywhere on a " \
                  "column to insert a disk in that column."
CLIENT_START_MSG = "Waiting for other player to begin"
YOUR_TURN_MSG = "It's YOUR turn"
OPPONENT_TURN_MSG = "It's your opponent's turn"
ILLEGAL_MOVE_MSG = "Illegal move"
DISK_COLOR_TURQUOISE_MSG = "Your disks are turquoise."
DISK_COLOR_PINK_MSG = "Your disks are pink."

LOSING_MSG = "Unfortunately you lost... \n But never let defeat have the " \
             "last word."
WINNING_MSG = "Congratulations! You won the game! \n But remember - Winning " \
              "isn't getting ahead of others. \n " \
              "It's getting ahead of yourself."
DRAW_MSG = "The game ended with a draw."


class GUI:
    MESSAGE_DISPLAY_TIMEOUT = 250

    def __init__(self, parent, game, type_player, port, ip=None):
        """
        This function initialize all the parameters that take place
        in the GUI class
        :param parent: A GUI object root
        :param game: A Game class object that manage all the game steps
        :param type_player: Defines the player type - AI or human
        :param port: The chosen port for the players to play on via the
                     network
        :param ip: Only relevant to the client who must enter the
                   server's ip to connect him
        """
        self.__parent = parent
        self.__game = game

        self.title(parent)
        self.canvas(parent)
        self.initializing_communicator(parent, port, ip)  # Calls other
        # function that initialize the connection between two players

        self.first_message(parent)

        self.__type_player = type_player

        # As long as it is not stated otherwise, AI player isn't initialize.
        self._ai = False
        # If the script called for an AI player:
        if self.__type_player == AI_PLAYER:
            self._ai = AI()
            self._ai.find_legal_move(self.__game, self.handle_event)

    def title(self, parent):
        """
        This function initialize the GUI title, will not return
        any
        :param parent: A GUI object root
        """
        self.__title = tk.Label(parent, text=WELCOME_MSG, font=TITLE_SIZE)
        self.__title.pack(side=tk.TOP)

    def canvas(self, parent):
        """
        This function initialize the GUI window as a canvas, will not return
        any
        :param parent: A GUI object root
        """
        self.__canvas = tk.Canvas(parent, width=CANVAS_WIDTH,
                                  height=CANVAS_HEIGHT,
                                  highlightbackground="Black", bg="PeachPuff2")
        self.__canvas.pack()
        self.__canvas.bind("<Button-1>", self.handle_event)
        # Define an event of one step via pressing the column on the screen
        self.create_board(parent)
        # Calling another function to draw the board as it should be

    def initializing_communicator(self, parent, port, ip):
        """
        This function initialize the communication between to players at the
        network using another script, will not return any
        :param parent: A GUI object root
        :param port: The chosen port the players would like to play at the
                     network
        :param ip: the server player ip that the client should connect to
        """
        # Check for the identity of the current player according to a given
        # or not given ip
        if ip:
            self.__player_id = Game.PLAYER_TWO
            self.__player_tag = tk.Label(parent, text=DISK_COLOR_TURQUOISE_MSG,
                                         font=MSG_SIZE, bg="turquoise3")

        else:
            self.__player_id = Game.PLAYER_ONE
            self.__player_tag = tk.Label(parent, text=DISK_COLOR_PINK_MSG,
                                         font=MSG_SIZE, bg="orchid")
        self.__player_tag.pack(side=tk.TOP)

        self.__communicator = Communicator(parent, port, ip)
        self.__communicator.connect()
        self.__communicator.bind_action_to_message(self.__handle_message)

    def first_message(self, parent):
        """
        This function defines the first massage any of the players will see
        at the bottom of the screen, should indicate instruction to the player,
        will not return any
        :param parent: A GUI object root
        """
        if self.__player_id == Game.PLAYER_ONE:
            self.turn = tk.Label(parent, text=INSTRUCTION_MSG)
            self.turn.pack(side=tk.BOTTOM)
        else:
            self.turn = tk.Label(parent, text=CLIENT_START_MSG)
            self.turn.pack(side=tk.BOTTOM)

    def close(self):
        """
        This function is to define to close the window when the player press
        at the 'exit' button, will not return any
        """
        self.__parent.destroy()

    def create_board(self, parent):
        """
        This function defines the appearance of the GUI, from the board ovals
        to the exit button, will not return any
        :param parent: A GUI object root
        """
        # Create ovals
        for row in range(Game.NUM_COL):
            for column in range(Game.NUM_ROWS):
                self.__canvas.create_oval(row * OVAL_DIAMETER,
                                          column * OVAL_DIAMETER,
                                          (row + 1) * OVAL_DIAMETER,
                                          (column + 1) * OVAL_DIAMETER,
                                          fill="White")

        # Create exit button
        self.__exit_button = tk.Button(parent, text="Exit", command=self.close)
        self.__exit_button.pack(side=tk.BOTTOM)

    def game_over(self):
        """
        This function handle the situations that the game should be ended,
        such as winning of one of the players and a draw by scanning the board
        :return: True/False if the the game is ended
        """
        # Search for a winning situation
        if self.__game.get_winner() == Game.PLAYER_ONE or \
                self.__game.get_winner() == Game.PLAYER_TWO:
            _, col, row, direction = self.__game.get_winner_helper()
            # Get the winning right spot and the winning direction using
            # another function
            list_of_winning_spots = self.__game.find_winning_disks(col, row,
                                                                   direction)
            # Get the list of all the winning spots using another function
            self.handle_winning(list_of_winning_spots)
            return True

        # Search for a draw situation
        if self.__game.get_winner() == Game.DRAW:
            self.turn.configure(text=DRAW_MSG, font=MSG_SIZE)
            return True

        return False

    def get_col_from_event(self, event, player):
        """
        This function manage the search for the column that the current player
        want to drop his disc to, also for the ai type of player
        :param event: The type of the event- pressed click on the screen or
                      string message
        :param player: The current player
        :return: The selected column for the current turn
        """
        # If player clicked
        if type(event) != str:
            if player is not self.__player_id:
                # If the one who clicked is not the current player
                return None
            if self.__type_player != "ai":
                column = event.x // OVAL_DIAMETER
            else:
                column = int(event)

        # Receive message
        else:
            column = int(event[-1])

        return column

    def change_board(self, column, row, player):
        """
        This function changes the GUI appearance (colored disks and messages)
        based on a new column that a disk was inserted into.
        :param column: The column that the step connected to
        :param row: The row that the step connected to
        :param player: The current player who does the current step
        """
        self.__game.make_move(column)
        self.draw_disk(row, column, player)
        self.turn.configure(text=YOUR_TURN_MSG)

        # Send message on the net to the other player
        if player == self.__player_id:
            self.turn.configure(text=OPPONENT_TURN_MSG)
            self.__communicator.send_message(str(column))

    def handle_event(self, event):
        """
        This function handles all the steps of what happens when there is an
        event (click or message received). This includes checking if the game
        is over, getting the column and row into which to add a disk, updating
        the GUI board, and checking for a winner. In addition, if there is an
        AI player, the function calls on it to make a move.
        :param event: Can either be a click or a message received from the
        other player
        :return: It the game is over, the function returns, this way the
        players can't continue making moves.
        """

        # check if game is over
        if self.game_over():
            return

        player = self.__game.get_current_player()

        # get column
        if self.get_col_from_event(event, player) == None:
            return
        else:
            column = self.get_col_from_event(event, player)

        # get row
        row = self.__game.find_row(column)

        # update board
        try:
            self.change_board(column, row, player)

        except Exception:
            self.turn.configure(text=ILLEGAL_MOVE_MSG)

        # if AI playing, do the next turn
        if self._ai and self.__player_id == self.__game.get_current_player():
            self._ai.find_legal_move(self.__game, self.handle_event)

        # check if after completing the move the game is now over
        if self.game_over():
            return

    def draw_disk(self, row, col, player):
        """
        Adds a colored disk to the user interface in the row and column that
        the player put in a disk
        :param row: an int representing the row in which a disk should go into
        :param col: an int representing the col in which a disk should go into
        :param player: the player who's turn it is. The color of the new disk
        added will be according to what player added it.
        """
        if player == Game.PLAYER_ONE:
            self.__canvas.create_oval(col * OVAL_DIAMETER, row * OVAL_DIAMETER,
                                      (col + 1) * OVAL_DIAMETER,
                                      (row + 1) * OVAL_DIAMETER, fill="orchid")

        else:
            self.__canvas.create_oval(col * OVAL_DIAMETER, row * OVAL_DIAMETER,
                                      (col + 1) * OVAL_DIAMETER,
                                      (row + 1) * OVAL_DIAMETER,
                                      fill="turquoise3")

    def handle_winning(self, list_of_winning_spots):
        """
        This function handles what happens when there is a winning sequence on
        the board.
        :param list_of_winning_spots: A list of four tuples that represent the
        spots on the board in which there is a winning hand.
        """
        for spot in list_of_winning_spots:
            row, col = spot
            self.__canvas.create_oval(row * OVAL_DIAMETER, col * OVAL_DIAMETER,
                                      (row + 1) * OVAL_DIAMETER,
                                      (col + 1) * OVAL_DIAMETER,
                                      fill="orange red")

        # updates winning/losing message
        player = self.__game.get_current_player()
        if player == self.__player_id:
            self.turn.configure(text=LOSING_MSG, font=MSG_SIZE)

        else:
            self.turn.configure(text=WINNING_MSG, font=MSG_SIZE)

    def __handle_message(self, text=None):
        """
        Specifies the event handler for the message getting event in the
        initializing_communicator. Prints a message when invoked (and invoked
        by the initializing_communicator when a message is received).
        The message will automatically disappear after a fixed interval.
        :param text: the text to be printed.
        """
        if text:
            self.handle_event(text)
            self.__parent.after(self.MESSAGE_DISPLAY_TIMEOUT,
                                self.__handle_message)


def check_input(args):
    """
    Checks if the input called in the command line is valid.
    :param args: the arguments that were entered in the command line
    :return True - if all arguments are valid, else, returns False
    """

    if len(args) != CLIENT_NUM_ARGS and len(args) != SERVER_NUM_ARGS:
        print(ILLEGAL_ARGS_MSG)
        return False

    elif int(args[PORT_NUM]) > MAX_PORT_NUM:
        print(ILLEGAL_ARGS_MSG)
        return False

    elif args[PLAYER_TYPE] != HUMAN and args[PLAYER_TYPE] != AI_PLAYER:
        print(ILLEGAL_ARGS_MSG)
        return False

    return True


def main(args):
    """
    The function that initializes the the game class and the GUI (by creating
    root)
    :param args: the arguments entered into the command line
    """
    if check_input(args):
        root = tk.Tk()
        game = Game()

        is_human = args[PLAYER_TYPE]
        port = int(args[PORT_NUM])
        if len(args) < CLIENT_NUM_ARGS:
            GUI(root, game, is_human, port)
            root.title(ROOT_TITLE_SERVER)

        else:
            ip = args[IP_NUM]
            GUI(root, game, is_human, port, ip)
            root.title(ROOT_TITLE_CLIENT)
        root.mainloop()


if __name__ == '__main__':
    main(sys.argv)
