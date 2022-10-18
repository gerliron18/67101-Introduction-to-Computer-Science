###############################################################
# FILE : math_print.py
# WRITER : Liron Gershuny , gerliron18 , 308350503
# EXERCISE : intro2cs ex1 2017-2018
# DESCRIPTION: A program that define printing functions
# to the result of mathematical calculations and print them.
###############################################################
import math


def golden_ratio():
    """This function print the golden ratio"""
    print((1 + math.sqrt(5)) / 2)


def six_square():
    """This function print the result of 6 raised
    to the power of 2"""
    print(math.pow(6, 2))


def hypotenuse():
    """This function print the length of the hypotenuse
    of right triangle with legs length of 5 and 12"""
    print(math.sqrt(math.pow(5, 2) + math.pow(12, 2)))


def pi():
    """This function print the value of Pi"""
    print(math.pi)


def e():
    """This function print the value of
     the mathematical constant e"""
    print(math.e)


def squares_area():
    """This function print the area of squares
    with 1 to 10 edge length"""
    print(int(math.pow(1, 2)), int(math.pow(2, 2)), int(math.pow(3, 2)),
          int(math.pow(4, 2)), int(math.pow(5, 2)), int(math.pow(6, 2)),
          int(math.pow(7, 2)), int(math.pow(8, 2)), int(math.pow(9, 2)),
          int(math.pow(10, 2)))


golden_ratio()
six_square()
hypotenuse()
pi()
e()
squares_area()
