############################################################
# Helper class
############################################################


class Direction:
    """
    Class representing a direction in 2D world.
    You may not change the name of any of the constants (UP, DOWN, LEFT, RIGHT,
     NOT_MOVING, VERTICAL, HORIZONTAL, ALL_DIRECTIONS), but all other
     implementations are for you to carry out.
    """
    UP = 8
    DOWN = 2
    LEFT = 4
    RIGHT = 6

    NOT_MOVING = 5

    VERTICAL = 0
    HORIZONTAL = 1

    ALL_DIRECTIONS = (UP, DOWN, LEFT, RIGHT)

############################################################
# Class definition
############################################################


class Car:
    """
    A class representing a car in rush hour game.
    A car is 1-dimensional object that could be laid in either horizontal or
    vertical alignment. A car drives on its vertical\horizontal axis back and
    forth until reaching the board's boarders. A car can only drive to an empty
    slot (it can't override another car).
    """

    def __init__(self, color, length, location, orientation):
        """
        A constructor for a Car object
        :param color: A string representing the car's color
        :param length: An int in the range of (2,4) representing the car's length.
        :param location: A tuple representing the car's head (x, y) location
        :param orientation: An int representing the car's orientation
        """
        self.__color = color
        self.__length = length
        self.__location = location
        self.__orientation = orientation

    def get_color(self):
        return self.__color

    def get_full_location(self):
        cord_list = []
        current_x, current_y = self.__location
        if self.__orientation == 0:
            for i in range(self.__length):
                cord_list.append((current_x + i, current_y))
        elif self.__orientation == 1:
            for i in range(self.__length):
                cord_list.append((current_x, current_y + i))
        return cord_list

    def get_length(self):
        return self.__length

    def get_location(self):
        return self.__location

    def get_orientation(self):
        return self.__orientation
