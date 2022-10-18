#############################################################
# FILE : largest_and_smallest.py
# WRITER : Liron Gershuny , gerliron18 , 308350503
# EXERCISE : intro2cs ex2 2017-2018
# DESCRIPTION: A program that define a function who gets
# three numbers and return the highest number and the
# lowest number without printing any.
#############################################################

def largest_and_smallest(num1, num2, num3):
    """A function that gets three numbers, check
    who is the highest and who is the lowest and
    return it"""
    if (num1 > num2) and (num1 > num3):
        if (num2 > num3):
            return num1, num3
        elif (num3 > num2):
            return num1, num2
        else:
            return num1, num2
    elif (num2 > num1) and (num2 > num3):
        if (num1 > num3):
            return num2, num3
        elif (num3 > num1):
            return num2, num1
        else:
            return num2, num1
    elif (num3 > num1) and (num3 > num2):
        if (num1 > num2):
            return num3, num2
        elif (num2 > num1):
            return num3, num1
        else:
            return num3, num1
    else:
        return num1, num2
