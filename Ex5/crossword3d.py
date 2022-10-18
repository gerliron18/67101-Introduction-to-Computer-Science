#############################################################
# FILE : crossword3d.py
# WRITERS : Liron Gershuny , gerliron18 , 308350503
#           Gal Batzia , gal.batzia , 313169005
# EXERCISE : intro2cs ex5 2017-2018
# DESCRIPTION:A program that find words in a 3d matrix by
# converting it to 2d matrix and than use program
# crossword.py to search the words in it.
#############################################################
from crossword import *  # Importing program that find words in 2d matrix
import sys  # Using sys to get inputs from user

DIRECTIONS_3D = ['a', 'b', 'c']


# 1
def txt_to_lists3d(f):
    """A function that convert 3d matrix in txt file to lists"""
    str_words = f.split('\n')
    new_list = []
    inner_matrix = []
    for i in range(len(str_words)):
        # Run on every line at the 3d matrix txt file,
        #  gives one line at a time
        one_letter = list(str_words[i].split(','))
        if str_words[i] == "***":
            new_list.append(inner_matrix)
            inner_matrix = []
        elif i == len(str_words) - 1:
            inner_matrix.append(one_letter)
            new_list.append(inner_matrix)
        else:
            inner_matrix.append(one_letter)
    return new_list


# 2
def get_matrix3d():
    """A function that insert txt file of 3d matrix
    given by the user to a variable"""
    matrix_file = sys.argv[2]
    with open(matrix_file, 'r') as matrix:
        mat = txt_to_lists3d(matrix.read())
    return mat


# 3
def check_the_input3d():
    """A function that check the user inputs
    if appropriate to the conditions"""
    if len(sys.argv) < 5:  # Check if all the needed parameters given
        print(
            'ERROR: invalid number of parameters. Please enter'
            ' word_file matrix_file output_file directions.')
        return False
    elif not os.path.isfile(sys.argv[1]):  # Check the propriety
        #  of the words list file
        print('ERROR: Word file word_list.txt not exist.')
        return False
    elif not os.path.isfile(sys.argv[2]):  # Check the
        #  propriety of the matrix file
        print('ERROR: Matrix file mat.txt not exist')
        return False
    else:
        for direction in sys.argv[4]:  # Run along the given
            #  directions, gives one direction at a time
            if direction not in DIRECTIONS_3D:  # Check the propriety
                #  of the given direction
                print('ERROR: invalid directions')
                return False
    return True


# 4
def depth(mat3d, words, sum_dict, directions2d):
    """A function that send a word for search in the
    given matrix at the depth dimension"""
    for i in range(len(mat3d)):  # Run along the indexes
        # at the depth dimension
        mat = mat3d[i]
        sum_dict = search_in_matrix(directions2d, words, mat, sum_dict)
        # Use search in matrix function to search the
        # current word at the current index
    return sum_dict


# 5
def length(mat3d, words, sum_dict, directions2d):
    """A function that send a word for search in the
    given matrix at the length_len dimension"""
    depth_len = len(mat3d)
    length_len = len(mat3d[0])
    for i in range(depth_len):
        # Run along the indexes at the depth_len dimension
        length_mat = []
        length_line = []
        for j in range(length_len):
            # Run along the indexes at the length_len dimension
            length_line.append(mat3d[j][i])
            length_mat.extend(length_line)
            length_line = []
        sum_dict = search_in_matrix(directions2d, words, length_mat, sum_dict)
        # Use search in matrix function to search
        # the current word at the current index
    return sum_dict


# 6
def width(mat3d, words, sum_dict, directions2d):
    """A function that send a word for search in the
    given matrix at the width dimension"""
    depth_len = len(mat3d)
    length_len = len(mat3d[0])
    width_len = len(mat3d[0][0])
    for i in range(depth_len):  # Run along the indexes
        #  at the depth dimension
        width_mat = []
        for j in range(length_len):  # Run along the indexes
            # at the length dimension
            width_line = []
            for h in range(width_len):  # Run along the indexes
                # at the width dimension
                width_letter = mat3d[h][j][i]
                width_line.extend(width_letter)
            width_mat.append(width_line)
        sum_dict = search_in_matrix(directions2d, words, width_mat, sum_dict)
        # Use search in matrix function to search
        # the current word at the current index
    return sum_dict


# 7
def navigate_directions(directions_list, words, mat3d, sum_dict, directions2d):
    """A function that get the user wanted search direction
    and send it to the specific function"""
    already_checked = []
    for direction in directions_list:  # Run along the user given directions
        if direction in already_checked:
            # Check for duplication at user input directions
            continue
        if direction == 'a':
            # Check if the user choose direction a
            sum_dict = depth(mat3d, words, sum_dict, directions2d)
            # Uses the function depth to search if the word appear there
        elif direction == 'b':
            # Check if the user choose direction b
            sum_dict = length(mat3d, words, sum_dict, directions2d)
            # Uses the function length to search if the word appear there
        elif direction == 'c':
            # Check if the user choose direction c
            sum_dict = width(mat3d, words, sum_dict, directions2d)
            # Uses the function width to search if the word appear there
        already_checked.append(direction)  # Update the already
        #  checked list to prevent duplications
    return sum_dict


# 8
def main():
    """A function that will manage all the process of this
    program from the user inputs to the program output file"""
    if check_the_input3d():  # Check for the correctness of the user input
        words = get_words()  # Insert the word list to a variable
        mat3d = get_matrix3d()  # Insert the matrix file to a variable
        output_file = sys.argv[3]
        # Insert the wanted output file to a variable
        directions = sys.argv[4]
        # Insert the user directions to a variable
        directions_list = list(directions)
        histogram_dict = {}  # Definite a dictionary as a histogram for words
        final_dict = {}  # Definite a final dictionary of words
        histogram_dict = make_dict_of_words(words, histogram_dict)
        # Use other function to insert info to histogram dictionary
        histogram_dict = navigate_directions(directions_list, words, mat3d,
                                             histogram_dict, DIRECTIONS_2D)
        # Use other function to navigate through user directions
        final_dict = sum_up(histogram_dict, final_dict)
        # Use other function to convert histogram to words dictionary
        write_to_file(final_dict, output_file)
        # form an output file with the appropriate information


if __name__ == '__main__':
    main()
