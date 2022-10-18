############################################################
# Imports
############################################################
import game_helper as gh
from car import Car, Direction

############################################################
# Constants
############################################################

# place your constants here

############################################################
# Class definition
############################################################


class Board():
    """
    A class representing a rush hour board.
    """

    def __init__(self, cars, exit_board, size=6):
        """
        Initialize a new Board object.
        :param cars: A list (or dictionary) of cars.
        :param size: Size of board (Default size is 6).
        """
        self.__cars = cars
        self.__exit_board = exit_board
        self.__size = size

    def add_car(self, car):
        """
        Add a single car to the board.
        :param car: A car object
        :return: True if a car was succesfuly added, or False otherwise.
        """
        for single_car in self.__cars:
            if single_car.get_color() == car.get_color():
                return False
        for coordinate in car.get_full_location():
            current_x, current_y = coordinate
            if (current_x > self.__size) or (current_y > self.__size):
                return False
            if self.is_empty(coordinate):
                return True
        return False
    
    def is_empty(self, location):
        """
        Check if a given location on the board is free.
        :param location: x and y coordinations of location to be check
        :return: True if location is free, False otherwise
        """
        cord_list = []
        for one_car in self.__cars:
            cord_list = one_car.get_full_location()
        if location in cord_list:
            return False
        return True
    
    def move(self, car, direction):
        """
        Move a car in the given direction.
        :param car: A Car object to be moved.
        :param direction: A Direction object representing desired direction
            to move car.
        :return: True if movement was possible and car was moved, False otherwise.
        """

        # implement your code here (and then delete the next line - 'pass')
        pass
    
    def __repr__(self):
        """
        :return: Return a string representation of the board.
        """
        # implement your code here (and then delete the next line - 'pass')
        pass

    def board_size(self):
        return self.__size