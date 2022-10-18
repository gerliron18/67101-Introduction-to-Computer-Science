#############################################################
# FILE : crossword.py
# WRITERS : Liron Gershuny , gerliron18 , 308350503
#           Gal Batzia , gal.batzia , 313169005
# EXERCISE : intro2cs ex5 2017-2018
# DESCRIPTION:this program gets a matrix, a list of words and directions,
#             and creates a file wihch holds all the words that show up
#             at least once in the matrix, by searching them following
#             the given directions
#############################################################
import os
import sys

DIRECTIONS_2D = ['u', 'd', 'r', 'l', 'w', 'x', 'y', 'z']


# 1
def txt_to_lists(f):
    """this function gets a txt file and makes a txt file and makes a list
    out of it.the functions splits the txt
    in every slash n and every common"""
    str_words = (f.split("\n"))
    for index, word in enumerate(str_words):
        str_words[index] = word.split(',')
        for i in range(len(str_words[index])):
            str_words[index][i]=str_words[index][i].lower()
    return str_words


# 2
def counting_word(word, sequence):
    """this function gets a word and a list of chars(sequence)
    and returns how many times the word is shown up in the given list"""
    counter = 0
    # lower list is a list of all the letters in the sequence, turned into
    # lower case letter, as required in the ex's instructions
    lower_list = [l.lower() for l in sequence]
    # going through all the sequence, checking for each letter if we can find
    # the given word from it.
    for i in range(len(lower_list)):
        # is finished tells us the reason why we broke
        # out of the loop in line 38
        is_finished = True
        # left_to check tells us how many letters we have to
        # the end of the sequence if we have less than the sequence's
        # length-1, we can break out of the loop
        left_to_check = len(lower_list) - i
        if left_to_check < len(word):
            break
        for j in range(len(word)):
            # i+j is the spot we want to check because we need to start
            # comparing the letters from the spesific letter
            # and not from the beginning
            if lower_list[i + j] != word[j]:
                is_finished = False
                break
        if is_finished:
            counter += 1
    return counter


# 3
def down(mat, word):
    """this function gets a matrix and a word and goes through the matrix
    vertically for each column (from the left column to the right one)
    from above to the bottom"""
    column = len(mat[0])
    row = len(mat)
    counter = 0
    for i in range(column):
        # collecting each letter to a list, which we'll compare to the given
        # word eventually
        down_list = []
        for j in range(row):
            down_list.append(mat[j][i])
            # comparing the word to the sequence we collected
        counter = counter + counting_word(word, down_list)
    return counter


# 4
def up(mat, word):
    """this function gets a matrix and a word and goes through the matrix
    vertically for each column (from the left column to the right one)
    from below to the upper spot of each column"""
    column = len(mat[0])
    row = len(mat)
    counter = 0
    for i in range(0, column):
        # collecting each letter to a list, which we'll compare to the given
        # word eventually
        up_list = []
        # we go from down to -1 because we want the checking to collect
        # the letter on spot 0 in each column as well
        for j in range(row - 1, -1, -1):
            up_list.append(mat[j][i])
            # comparing the word to the sequence we collected
        counter = counter + counting_word(word, up_list)
    return counter


# 5
def right(mat, word):
    """this function gets a matrix and a word and goes through the matrix
    horizontally for each row (from the upper row to the bottom one)
    from the left to the right of each row"""
    column = len(mat[0])
    row = len(mat)
    counter = 0
    for i in range(row):
        # collecting each letter to a list, which we'll compare to the given
        # word eventually
        right_list = []
        for j in range(column):
            right_list.append(mat[i][j])
            # comparing the word to the sequence we collected
        counter = counter + counting_word(word, right_list)
    return counter


# 6
def left(mat, word):
    """this function gets a matrix and a word and goes through the matrix
    horizontally for each row (from the upper row to the bottom one)
    from the right to the left of each row"""
    column = len(mat[0])
    row = len(mat)
    counter = 0
    for i in range(row):
        # collecting each letter to a list, which we'll compare to the given
        # word eventually
        left_list = []
        # we go to -1 because we want to add spot zero on each column as well
        for j in range(column - 1, -1, -1):
            left_list.append(mat[i][j])
            # comparing the word to the sequence we collected
        counter = counter + counting_word(word, left_list)
    return counter


# 7
def left_to_right_down(mat, word):
    """this function from left to right and down
     it gets a matrix and a word and goes through the matrix
       diagonally from the upper left corner down and to the right
       the checking is built on two parts:
       1) going through the left column diagonally for each spot on it
       2) going through the upper row diagonally for each spot on it"""
    column = len(mat[0])
    row = len(mat)
    counter = 0
    # part 1 of checking sequences. we go down on the first column and make
    # "a" start at a more progressed spot each time, while "b" starts at zero
    # each time (which means going through every spot on the left column
    for i in range(row):
        a = i
        b = 0
        # collecting each letter to a list, which we'll compare to the given
        # word eventually
        diagonal_list1 = []
        # this loop is running while "a" haven't got to its
        # end (the lower row) and while "b" haven't got to its
        # end (the rightest column
        while a < row and b < column:
            diagonal_list1.append(mat[a][b])
            # making them grow by one each time and by that making the adding
            # diagonal
            a += 1
            b += 1
        counter = counter + counting_word(word, diagonal_list1)
    # part 2 of checking sequences. we go down on the first row and make
    # "a" start at a zero each time, while "b" starts at
    # every column's upper spot each time (which means going through
    # every spot on the upper row
    for j in range(1, column):
        a = 0
        b = j
        # collecting each letter to a list, which we'll compare to the given
        # word eventually
        diagonal_list2 = []
        # this loop is running while "a" haven't got to
        # its end (the lower row), and while "b" haven't got to
        # its end (the rightest column
        while b < column and a < row:
            diagonal_list2.append(mat[a][b])
            a += 1
            b += 1
        counter = counter + counting_word(word, diagonal_list2)
    return counter


# 8
def right_to_left_down(mat, word):
    """this function goes from right to left and down.
     it gets a matrix and a word and goes through the matrix
       diagonally from the upper right corner down and to the left
       the checking is built on two parts:
       1) going through the right column diagonally for each spot on it
       2) going through the upper row diagonally for each spot on it"""
    column = len(mat[0])
    row = len(mat)
    counter = 0
    # part 1 of checking sequences. we go down on the rightest column and make
    # "a" start at a more progressed spot each time, while "b" starts at
    # the last column's spot. this happens each time
    # (which means going through every spot on the rightest column)
    for i in range(row):
        diagonal_list1 = []
        a = i
        b = column - 1
        # this loop is running while "a" haven't got to
        # its end (the lower row) and while "b" haven't got to
        # its end (the left column)
        while a < row and b >= 0:
            diagonal_list1.append(mat[a][b])
            a += 1
            # "b" goes smaller each time because it goes form the end
            # to the beginning
            b -= 1
        counter = counter + counting_word(word, diagonal_list1)
    # part 2 of checking sequences. we go left on the first row,
    # from the end to the beginning, and make "a" start at a zero each time,
    #  while "b" starts at every column's upper spot, and gets smaller by 1
    # each time (which means going through every spot on the upper row)
    for j in range(column - 2, -1, -1):
        a = 0
        b = j
        diagonal_list2 = []
        # this loop is running while "a" haven't got to
        # its end (the lower row) and while "b" haven't got to
        # its end (the left column)
        while b >= 0 and a < row:
            diagonal_list2.append(mat[a][b])
            a += 1
            b -= 1
        counter = counter + counting_word(word, diagonal_list2)
    return counter


# 9
def right_to_left_up(mat, word):
    """this function goes from right to left and up
     it gets a matrix and a word and goes through the matrix
           diagonally from the lower right corner up and to the left
           the checking is built on two parts:
           1) going through the lower row diagonally for each spot on it
           2) going through the right column diagonally for each spot on it"""
    column = len(mat[0])
    row = len(mat)
    counter = 0
    # part 1 of checking sequences. we go left on the lowest row and make
    # "a" start at the lowest spot each time, while "b" starts at
    # the last column's last spot. this happens each time
    # (which means going through every spot on the rightest column)
    # we go down to -1 because we want to check spot zero as well
    for i in range(column - 1, -1, -1):
        a = row - 1
        b = i
        diagonal_list1 = []
        # this loop is running while "a" haven't got to its end (above row 0),
        # and while "b" haven't got to its end (the left column)
        # we go from right to left so we're making "a"
        # and "b" smaller each time
        while b < column and b >= 0 and a >= 0:
            diagonal_list1.append(mat[a][b])
            a -= 1
            b -= 1
        counter = counter + counting_word(word, diagonal_list1)
    # part 2 of checking sequences. we go up on the last column,
    # from the end to the beginning, and make "a" start at
    #  the last row's last spot each time,
    #  while "b" starts at the last column each time
    # (which means going through every spot on the upper row)
    for j in range(row - 2, -1, -1):
        a = j
        b = column - 1
        diagonal_list2 = []
        # this loop is running while "a" haven't got to its end (above row 0),
        # and while "b" haven't got to its end (left to column o)
        # we go from right to left so we're making "a" and
        # "b" smaller each time
        while a >= 0 and b >= 0:
            diagonal_list2.append(mat[a][b])
            a -= 1
            b -= 1
        counter = counter + counting_word(word, diagonal_list2)
    return counter


# 10
def left_to_right_up(mat, word):
    """this function goes from left to right and up
    it gets a matrix and a word and goes through the matrix
    diagonally from the lower left corner up and to the right
    the checking is built on two parts:
    1) going through the left column diagonally for each spot on it
    2) going through the lowest row diagonally for each spot on it"""
    column = len(mat[0])
    row = len(mat)
    counter = 0
    # part 1 of checking sequences. we go up on the left column and make
    # "a" start at the lowest spot each time, while "b" starts at
    # the last column's last spot. this happens each time
    # (which means going through every spot on the left column)
    for i in range(column - 1):
        a = row - 1
        b = i
        diagonal_list1 = []
        # this loop is running while "a" haven't got to its end (above row 0),
        # and while "b" haven't got to its end (the left column)
        # we go from down to up we're making "a" smaller each time
        while a >= 0 and b < column:
            diagonal_list1.append(mat[a][b])
            a -= 1
            b += 1
        counter = counter + counting_word(word, diagonal_list1)
    # part 2 of checking sequences. we go right on the lowest row,
    # from the beginning to the end, and make "a" start at
    # the a spot in the last row each time,
    # while "b" starts at 0 each time
    # (which means going through every spot on the upper row)
    for j in range(row - 2, -1, -1):
        a = j
        b = 0
        diagonal_list2 = []
        # this loop is running while "a" haven't got to its end (above row 0),
        # and while "b" haven't got to its end (right to the lest column)
        # we go from down to up so we're making "a" smaller each time
        while a >= 0 and b < column:
            diagonal_list2.append(mat[a][b])
            a -= 1
            b += 1
        counter = counter + counting_word(word, diagonal_list2)
    return counter


# 11
def check_the_input():
    """this uses the info which is kept in "sys.argv" for knowing if we
    got any wrong data"""
    # this if is for knowing if we don't have all the files we need
    if len(sys.argv) < 5:
        print('ERROR: invalid number of parameters. Please enter '
              'word_file matrix_file output_file directions.')
        return False
    # this if is for knowing if we got the words file or not
    elif not os.path.isfile(sys.argv[1]):
        print('ERROR: Word file word_list.txt not exist.')
        return False
    # this if is for knowing if we got the matrix file
    elif not os.path.isfile(sys.argv[2]):
        print('ERROR: Matrix file mat.txt not exist')
        return False
    else:
        # this loop is for going through all the directions list kept in
        # sys.argv and checking if we have any letters witch aren't proper
        # for our program, or if we don't have any letters at all
        for letter in sys.argv[4]:
            if letter not in DIRECTIONS_2D:
                print('ERROR: invalid directions')
                return False
    return True


# 12
def get_words():
    """making the words_list file into a variable"""
    word_file = sys.argv[1]
    with open(word_file, 'r') as words_list:
        words = txt_to_lists(words_list.read())
    return words


# 13
def get_matrix():
    """making the mat file into a variable"""
    matrix_file = sys.argv[2]
    with open(matrix_file, 'r') as matrix:
        mat = txt_to_lists(matrix.read())
    return mat


# 14
def sum_up(sum_dict, new_dict):
    """moving all the relevant words, the words which have been found in the
    matrix, to a new dictionary, like required in the ex's instructions"""
    for i in sum_dict:
        if sum_dict[i] == 0:
            continue
        else:
            new_dict[i] = sum_dict[i]
    return new_dict


# 15
def write_to_file(new_dict, output_file):
    """sorting the dictionary alphabetically"""
    with open(output_file, 'w') as output:
        to_write = ""
        for j in sorted(new_dict):
            to_write += j + ',' + str(new_dict[j]) + '\n'
        output.write(to_write.strip())


# 16
def make_dict_of_words(words, sum_dict):
    """moving all the words from the words list into a dictionary"""
    for i in words:
        word = i[0]
        sum_dict[word] = 0
    return sum_dict


# 17
def search_in_matrix(directions_list, words, mat, sum_dict):
    """this function uses all the searching functions above"""
    # already checked is a list which holds every letter we checked in the
    # given directions, so we won't check a letter twice, like required.
    already_checked_direction = []
    for direction in directions_list:
        if direction in already_checked_direction:
            continue
        # checking up
        if direction == 'u':
            for word in words:
                word = word[0]
                counter = up(mat, word)
                # updating the current word's shows in the checking
                sum_dict[word] += counter
        # checking down
        elif direction == 'd':
            for word in words:
                word = word[0]
                counter = down(mat, word)
                # updating the current word's shows in the checking
                sum_dict[word] += counter
        # checking right
        elif direction == 'r':
            for word in words:
                word = word[0]
                counter = right(mat, word)
                # updating the current word's shows in the checking
                sum_dict[word] += counter
        # checking left
        elif direction == 'l':
            for word in words:
                word = word[0]
                counter = left(mat, word)
                # updating the current word's shows in the checking
                sum_dict[word] += counter
        # checking up and right
        elif direction == 'w':
            for word in words:
                word = word[0]
                counter = left_to_right_up(mat, word)
                # updating the current word's shows in the checking
                sum_dict[word] += counter
        # checking up and left
        elif direction == 'x':
            for word in words:
                word = word[0]
                counter = right_to_left_up(mat, word)
                # updating the current word's shows in the checking
                sum_dict[word] += counter
        # checking down and right
        elif direction == 'y':
            for word in words:
                word = word[0]
                counter = left_to_right_down(mat, word)
                # updating the current word's shows in the checking
                sum_dict[word] += counter
        # checking and left
        elif direction == 'z':
            for word in words:
                word = word[0]
                counter = right_to_left_down(mat, word)
                # updating the current word's shows in the checking
                sum_dict[word] += counter
        already_checked_direction.append(direction)
    return sum_dict


# 18
def main():
    """running the whole checking"""
    # checking that the input is fine
    if check_the_input():
        # from files to variables
        words = get_words()
        mat = get_matrix()
        output_file = sys.argv[3]
        directions = sys.argv[4]
        directions_list = list(directions)
        # sum dict is for all the words
        sum_dict = {}
        # new dict is for the words which show up at least once (from sum dict)
        new_dict = {}
        # putting all the words from words list in sum dict
        sum_dict = make_dict_of_words(words, sum_dict)
        # running the test
        sum_dict = search_in_matrix(directions_list, words, mat, sum_dict)
        # moving sum dict into new dict
        new_dict = sum_up(sum_dict, new_dict)
        write_to_file(new_dict, output_file)


if __name__ == '__main__':
    main()
