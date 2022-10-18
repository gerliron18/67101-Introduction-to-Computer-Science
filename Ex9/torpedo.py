TORPEDO_RADIUS = 4


class Torpedo:
    """This class represents a torpedo in the game Asteroids. A torpedo is
    an object which is released by a ship object, flies around the
    board, and can crash into asteroids. A torpedo's starting location,
    speed, and direction are all based upon the ship's data at the point the
    torpedo is created. A torpedo has a life time that is limited to 200
    rounds of the game loop. Once it's life time is depleted, the torpedo
    disappears."""

    def __init__(self, cord_x, cord_y, speed_x, speed_y, heading,
                 life_time=200):
        """This function initializes a torpedo and gives it a location (x,
        y coordinates), a speed (also on the x and y axis), a heading,
        and a life time."""
        self.__cord_x = cord_x
        self.__speed_x = speed_x
        self.__cord_y = cord_y
        self.__speed_y = speed_y
        self.__heading = heading
        self.__life_time = life_time

    def get_radius(self):
        """This function returns the radius of the torpedo (which always
        stays the same)."""
        return TORPEDO_RADIUS

    def get_cord_x(self):
        """This function gets the torpedo's x coordinate."""
        return self.__cord_x

    def get_cord_y(self):
        """This function gets the torpedo's y coordinate."""
        return self.__cord_y

    def get_speed_x(self):
        """This function gets the torpedo's speed on the x axis."""
        return self.__speed_x

    def get_speed_y(self):
        """This function gets the torpedo's speed on the y axis."""
        return self.__speed_y

    def get_heading(self):
        """This function gets the torpedo's heading."""
        return self.__heading

    def get_life_time(self):
        """This function gets the torpedo's life time."""
        return self.__life_time

    def set_speed_x(self, speed_x):
        """This function sets the torpedo's speed on the x axis."""
        self.__speed_x = speed_x

    def set_speed_y(self, speed_y):
        """This function sets the torpedo's speed on the y axis"""
        self.__speed_y = speed_y

    def set_cord_x(self, cord_x):
        """This function sets the torpedo's x coordinate."""
        self.__cord_x = cord_x

    def set_cord_y(self, cord_y):
        """This function sets the torpedo's y coordinate."""
        self.__cord_y = cord_y

    def set_life_time(self, life_time):
        """This function sets the torpedo's life time"""
        self.__life_time = life_time
