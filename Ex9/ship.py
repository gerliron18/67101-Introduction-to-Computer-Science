import math

TURN_RIGHT = 7
TURN_LEFT = -7
SHIP_RADIUS = 1


class Ship:
    """This class represents a ship in the game Asteroids. A ship is
    an object which flies around the board, can release torpedoes, and
    can crash into asteroids. A ship's characteristics include a location (x
    and y coordinates, speed (also on the x and y axis), a heading and three
    lives."""

    def __init__(self, cord_x, cord_y, speed_x=0, speed_y=0, heading=0):
        """This function initializes a ship and gives it a location
        (x, y coordinates), a speed (also on the x and y axis), and a heading
        (which is the direction the ship is facing)."""
        self.__cord_x = cord_x
        self.__speed_x = speed_x
        self.__cord_y = cord_y
        self.__speed_y = speed_y
        self.__heading = heading

    def get_cord_x(self):
        """This function gets the ship's x coordinate."""
        return self.__cord_x

    def get_cord_y(self):
        """This function gets the ship's y coordinate."""
        return self.__cord_y

    def get_speed_x(self):
        """This function gets the ship's speed on the x axis."""
        return self.__speed_x

    def get_speed_y(self):
        """This function gets the ship's speed on the y axis"""
        return self.__speed_y

    def get_heading(self):
        """This function gets the ship's heading"""
        return self.__heading

    def set_cord_x(self, cord_x):
        """This function sets the ship's x coordinate."""
        self.__cord_x = cord_x

    def set_cord_y(self, cord_y):
        """This function sets the ship's x coordinate."""
        self.__cord_y = cord_y

    def set_speed_x(self, speed_x):
        """This function sets the ship's speed on the x axis"""
        self.__speed_x = speed_x

    def set_speed_y(self, speed_y):
        """This function sets the ship's speed on the x axis"""
        self.__speed_y = speed_y

    def turn_right(self):
        """This function changes the ship's heading
        so it turns to the right."""
        self.__heading += TURN_RIGHT

    def turn_left(self):
        """This function changes the ship's heading
        so it turns to the left."""
        self.__heading += TURN_LEFT

    def accelerate(self):
        """This function accelerates the ship by changing the speed on the x
        any y axis according to the given equation."""
        new_speed_x = self.__speed_x + math.cos(math.radians(self.__heading))
        new_speed_y = self.__speed_y + math.sin(math.radians(self.__heading))
        self.set_speed_x(new_speed_x)
        self.set_speed_y(new_speed_y)

    def get_radius(self):
        """This function returns the ships radius, which does not change
        throughout the game."""
        return SHIP_RADIUS
