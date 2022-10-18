#############################################################
# FILE : quadratic_equation.py
# WRITER : Liron Gershuny , gerliron18 , 308350503
# EXERCISE : intro2cs ex2 2017-2018
# DESCRIPTION: A program that define two functions:
# a function that gets three coefficients of quadratic
# equation, calculate and return her result/s without
# printing them. A function that gets the three
# coefficients of quadratic equation input from the user
# and uses the first function to do the math then print
# the solution.
#############################################################
import math

FIRST_SOLUTION = 0
SECOND_SOLUTION = 1


def quadratic_equation(a, b, c):
    """A function that gets three coefficients of
    quadratic equation and return her result/s.
    Will return None, None if the user try to divide by zero"""
    delta = (math.pow(b, 2) - 4 * a * c)
    # Refers only to the expression within the square root
    if ((2 * a) == 0):  # Refers to division by zero
        return None, None
    elif delta > 0:
        solve1 = ((-b) + math.sqrt(delta)) / (2 * a)
        solve2 = ((-b) - math.sqrt(delta)) / (2 * a)
        return solve1, solve2
    elif delta == 0:
        one_solve = ((-b) / (2 * a))
        return one_solve, None
    else:
        return None, None


def quadratic_equation_user_input():
    """A function that ask the user to choose 3 coefficients of
    quadratic equation and then use the previous function to do
    the math and print the solution"""
    param1, param2, param3 = (input('Insert coefficients a, b, and c: ')) \
        .split(" ")
    param1 = float(param1)
    param2 = float(param2)
    param3 = float(param3)
    call = quadratic_equation(param1, param2, param3)
    if call[FIRST_SOLUTION] and call[SECOND_SOLUTION]:
        print('The equation has 2 solutions: ', call[FIRST_SOLUTION], 'and ',
              call[SECOND_SOLUTION])
    elif (call[FIRST_SOLUTION]):
        print('The equation has 1 solution: ', call[FIRST_SOLUTION])
    else:
        print('The equation has no solutions')
