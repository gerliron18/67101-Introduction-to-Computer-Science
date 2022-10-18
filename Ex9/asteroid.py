import math

SIZE_COEFFICIENT = 10
NORMALIZING_FACTOR = 5


class Asteroid:
    """This class represents an asteroid in the game Asteroids. An asteroid is
    an object which has a location, a speed, and a size. An asteroid can be
    hit either by a ship or a torpedo. If an asteroid collides with a ship,
    the asteroid disappears. If an asteroid is hit by a torpedo, it gets
    split into two asteroids, of smaller size and opposite directions. If an
    asteroid is hit once it's size 1, it disappears."""

    def __init__(self, cord_x, cord_y, speed_x, speed_y, size=3):
        """This function initializes an asteroid and gives it a location (x,
        y coordinates), a speed (also on the x and y axis), and a size."""
        self.__cord_x = cord_x
        self.__speed_x = speed_x
        self.__cord_y = cord_y
        self.__speed_y = speed_y
        self.__size = size

    def get_cord_x(self):
        """This function gets the asteroid's x coordinate."""
        return self.__cord_x

    def get_cord_y(self):
        """This function gets the asteroid's y coordinate."""
        return self.__cord_y

    def get_speed_x(self):
        """This function gets the asteroid's speed on the x axis."""
        return self.__speed_x

    def get_speed_y(self):
        """This function gets the asteroid's speed on the y axis"""
        return self.__speed_y

    def get_size(self):
        """This function gets the asteroid's size."""
        return self.__size

    def set_cord_x(self, cord_x):
        """This function sets the asteroid's speed on the x axis"""
        self.__cord_x = cord_x

    def set_cord_y(self, cord_y):
        """This function sets the asteroid's speed on the y axis"""
        self.__cord_y = cord_y

    def set_speed_x(self, speed_x):
        """This function sets the asteroid's speed on the x axis"""
        self.__speed_x = speed_x

    def set_speed_y(self, speed_y):
        """This function sets the asteroid's speed on the y axis"""
        self.__speed_y = speed_y

    def get_radius(self):
        """This function sets the asteroid's radius."""
        radius = (self.get_size() * SIZE_COEFFICIENT) - NORMALIZING_FACTOR
        return radius

    def has_intersection(self, obj):
        """This function checks if the asteroid collided with another object,
        and returns True if a crash occurred."""
        distance = math.sqrt((obj.get_cord_x() - self.__cord_x) ** 2 +
                             (obj.get_cord_y() - self.__cord_y) ** 2)
        if distance <= self.get_radius() + obj.get_radius():
            return True
        return False
