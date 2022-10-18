#############################################################
# FILE : calculate_mathematical_expression.py
# WRITER : Liron Gershuny , gerliron18 , 308350503
# EXERCISE : intro2cs ex2 2017-2018
# DESCRIPTION: A program that define 2 different functions:
# 1. A calculator for basic mathematical expressions and
# return result without printing it.
# 2. A function that gets a string, split it by types and
# call the first function.
#############################################################
addition = "+"  # represent an addition operation
subtraction = "-"  # represent a subtraction operation
multiplication = "*"  # represent a multiplication operation
division = "/"  # represent a division operation
spacing = " "  # represent a one space character


def calculate_mathematical_expression(num1, num2, operation):
    """This function gets 2 numerical values and
    1 mathematical function, do the math and return
    the result"""
    if operation == addition:
        return num1 + num2
    elif operation == multiplication:
        return num1 * num2
    elif operation == subtraction:
        return num1 - num2
    elif operation == division:
        if num2 == 0:
            return None
        else:
            return num1 / num2
    else:
        return None


def calculate_from_string(sms):
    """This function gets a string, take from it
    2 numerical values and 1 mathematical function
    and then call the previous function"""
    num_one, operation, num_two = (sms.split(spacing))
    return calculate_mathematical_expression(float(num_one), float(num_two),
                                             operation)
