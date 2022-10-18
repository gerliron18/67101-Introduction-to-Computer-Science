#############################################################
# FILE : convert_spoon_to_cup.py
# WRITER : Liron Gershuny , gerliron18 , 308350503
# EXERCISE : intro2cs ex2 2017-2018
# DESCRIPTION: A program that define a function that gets
# number of spoons needed by the user, calculate the
# equivalent value in cups and return it without printing it.
#############################################################
CONVERSION = 3.5  # Represent the conversion from spoons to cups


def convert_spoon_to_cup(quantity):
    """This function get the number of spoons and calculate
    the amount of cups it's fit without printing it"""
    return quantity / CONVERSION
