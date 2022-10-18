#############################################################
# FILE : ex11_backtrack.py
# WRITER : Liron Gershuny , gerliron18 , 308350503
# EXERCISE : intro2cs ex11 2017-2018
# DESCRIPTION: A program that defines a backtracking
# function that can solve a diverse of problems like
# solving a sudoku game and many more.
#############################################################

def general_backtracking(list_of_items, dict_items_to_vals, index,
                         set_of_assignments, legal_assignment_func, *args):
    """
    A function that uses backtracking method to solve a bunch of
    problems that built with trying some way and if it wont work
    till the end it will go back and try else options.
    :param list_of_items: A list of elements we would like to
           give an assignment.
    :param dict_items_to_vals: A dictionary consist keys from
           list_of_items and values of assignments from
           set_of_assignments.
    :param index: An integer represents the location in the
           list_of_items of the checked element.
    :param set_of_assignments: A list of all the legal posting
           values, will pose as the dict_items_to_vals values.
    :param legal_assignment_func: A pointer to dedicated function
           that checks the correction of one assignment.
    :param args: A list of variables that can be transported to
           this backtracking.
    :return: True/False if it find a legal solution to a problem.
    """
    if index == len(list_of_items):
        # If we got to the end of the wanted to give a placement list
        return True
    backtrack_value = dict_items_to_vals[list_of_items[index]]
    # Save the next element we would like to give an assignment value
    for assignment in set_of_assignments:
        dict_items_to_vals[list_of_items[index]] = assignment
        # Giving an assignment to the current position
        if legal_assignment_func(dict_items_to_vals, list_of_items[index],
                                 *args):
            # Check if it OK to give the current assignment to on element
            if general_backtracking(list_of_items, dict_items_to_vals,
                                    index + 1, set_of_assignments,
                                    legal_assignment_func,
                                    *args):  # Recursive call
                return True
    dict_items_to_vals[list_of_items[index]] = backtrack_value
    # If the assignment was wrong, give back the element his original value
    return False
