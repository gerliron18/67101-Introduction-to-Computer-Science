#############################################################
# FILE : shapes.py
# WRITER : Liron Gershuny , gerliron18 , 308350503
# EXERCISE : intro2cs ex2 2017-2018
# DESCRIPTION: A program that define a function that gets
#  input from the user about geometric shape and its
#  characteristics and then return the shape area
# without printing it.
#############################################################
import math


def shape_area():
    """This function ask the user to choose geometry shape,
    waits for the user to enter the chosen shape characteristics
    and finally return the shape area"""
    user_choice = input('Choose shape (1=circle, 2=rectangle, 3=trapezoid): ')
    if user_choice == '1':
        radius = float(input())
        return ((math.pi) * (math.pow(radius, 2)))
    elif user_choice == '2':
        width = float(input())
        length = float(input())
        return (width * length)
    elif user_choice == '3':
        first_base = float(input())
        second_base = float(input())
        height = float(input())
        return (((first_base + second_base) / 2) * height)
    else:
        return None
