#############################################################
# FILE : hangman.py
# WRITER : Liron Gershuny , gerliron18 , 308350503
# EXERCISE : intro2cs ex4 2017-2018
# DESCRIPTION: A program that defines "hangman" game and
# all the possible cases depending on the conditions of the
# game.
#############################################################
from hangman_helper import *  # Importing all the functions writen
# by the school
CHAR_A = 97
ALPHA = 26  # The number of letters in English alphabet


# 1
def letter_to_index(letter):
    """A function that turns a letter from the English alphabet
    to the appropriate index from 0 to 25"""
    return ord(letter.lower()) - CHAR_A


# 2
def index_to_letter(index):
    """A function that turns the index number of an English letter
    from 0 to 25 to the appropriate letter"""
    return chr(index + CHAR_A)


# 3
def update_word_pattern(word, pattern, letter):
    """A function that update the pattern as if the user
    chose the appropriate letter appears in the chosen word"""
    factors_list = list(word)  # Turn the chosen word to a list of letters
    pattern_list = list(pattern)  # Turn the pattern to a list of characters
    for i in range(len(factors_list)):  # Move trough all the
        # characters at the list
        if letter in factors_list[i]:  # Check if the user chosen letter
            # is in the word list
            pattern_list[i] = letter  # If the letter is in
            # the chosen word the pattern will update with the letter in
            # the appropriate index
            pattern = ''.join(pattern_list)  # Join the list of pattern
            # characters to one string
        else:
            continue
    return pattern


# 4
def good_choice(choosen_word, pattern, choosen_letter, messenger):
    """A function that define all the needed updates when the
    user pick the right letter appers at the chosen word"""
    pattern = update_word_pattern(choosen_word, pattern, choosen_letter)
    # Call the previous function for updating the pattern
    messenger = DEFAULT_MSG  # Update the message to the user when pick right
    return (pattern, messenger)


# 5
def bad_choice(choosen_letter, wrong_guess_lst, error_count, pattern,
               messenger):
    """A function that define all the needed updates when the
    user pick the wrong letter that not appear at the chosen word"""
    if choosen_letter in wrong_guess_lst:  # Check if the user chosen
        #  letter appears at the wrong guess list
        messenger = ALREADY_CHOSEN_MSG + choosen_letter  # Update the
        # message to the user for already chosen letter
    elif choosen_letter in pattern:  # Check if the user chosen letter
        #  already appears at the pattern
        messenger = ALREADY_CHOSEN_MSG + choosen_letter  # Update the
        # message to the user for already chosen letter
    elif choosen_letter not in wrong_guess_lst:  # Check if the user
        #  chosen letter not appears at the wrong guess list
        wrong_guess_lst += choosen_letter  # Updating the wrong guess
        #  list with the user chosen letter that not appearing
        #  at the chosen word
        error_count += 1  # Add one to the error counter
        messenger = DEFAULT_MSG  # Update the message to the user
    return (wrong_guess_lst, error_count, pattern, messenger)


# 6
def end_game(choosen_word, wrong_guess_lst, error_count, pattern):
    """A function that define what should the program do and say to the user
    when the user won or when he losses. Open a new game
    or maybe play no more"""
    if pattern == choosen_word:  # Check if the final pattern
        #  identical to the chosen word
        display_state(pattern, error_count, wrong_guess_lst, WIN_MSG,
                      ask_play=True)  # Updating the message
        # for a wining situation
    else:  # Means if the final pattern not identical to the chosen word
        display_state(pattern, error_count, wrong_guess_lst,
                      LOSS_MSG + choosen_word,
                      ask_play=True)  # Updating the message
        #  for a loss situation


# 7
def filter_words_list(words_list, pattern, wrong_guess_list):
    """This function is the first step of returning a hint to the user.
    It will filter word from the words.txt as if it appropriate
    to some definitions"""
    possible_words = []  # Make a new list where all
    # the appropriate words will append to
    for i in words_list:  # A loop that helps to check
        #  word at a time from the word list
        if check_the_word(i, pattern, wrong_guess_list):  # Check if the word
            #  is suitable to the definition
            possible_words.append(i)  # Import the filtered
            # word to the possible words list
    return possible_words


# 8
def check_the_word(one_word, pattern, wrong_guess_list):
    """A function that checks if any word from the words list is
    suitable to the definitions, will return boolean True or False"""
    if len(one_word) != len(pattern):  # Check if the length of the
        #  given word is at the length of the pattern
        return False
    for i in range(len(one_word)):  # A loop that helps
        # check any of the indexes of the given word
        if pattern[i] != '_' and one_word[i] != pattern[i]:  # Check if
            #  that index from the pattern is an underline
            #  and if is the same at the given word
            return False
        elif pattern[i] == one_word[i]:  # Check if the index from
            #  the pattern is identical to the index from the word
            if letter_counter(one_word, one_word[i]) != \
                    letter_counter(pattern, one_word[i]):  # Calling another
                #  function, will check if a letter from the pattern will
                #  not appear at the wrong index at the given word
                return False
        elif one_word[i] in wrong_guess_list:  # Check if the given
            #  word got any letter from the wrong guess list
            return False
    return True


# 9
def letter_counter(check_word, check_letter):
    """A function that count how many times the given
    letter appears in the filtered word, help to check if a given word
    is appropriate to be a hint"""
    counter = 0  # Define a counter
    for i in check_word:  # A loop that will go trough any
        #  of the letters from the given word
        if check_letter == i:  # Check if a letter from the
            # word is identical to a given letter
            counter += 1  # Counter add 1
    return counter


# 10
def choose_letter(possible_words, pattern):
    """A function that gets a list of filtered words for a hint,
    will return one letter that will be print back to the user
    as a hint. Works as a histogram"""
    final_list = [0] * ALPHA  # Define a new list of
    # numbers as long as the English alphabet
    list_of_letters = word_to_list(possible_words)  # Make a new list
    #  that gets all the letters from the given word list
    for i in list_of_letters:  # A loop that helps going
        # trough all the letters from the list
        if i in pattern:  # Check if the letter appears in the pattern
            num = letter_to_index(i)  # Define a variable of number
            #  using the function from school to convert the letter
            final_list[num] = 0  # final list at the index of the
            #  letter will be resetting so it won't be chosen as a hint
        else:  # If the letter not appear at the pattern
            num = letter_to_index(i)  # Define a variable of number
            #  using the function from school to convert the letter
            final_list[num] += 1  # The index of the letter from
            # the final list will be update plus 1
    final_letter = index_to_letter(final_list.index(max(final_list)))
    # Choose the final hint letter by choosing the maximum appearing
    # letter from a filter word list, using a function from school
    # to convert index to letter
    return final_letter


# 11
def word_to_list(possible_words):
    """A function that helps convert a given word to a list of the letters
    appears at the word. Get a list of words, will return a list of letters"""
    list_of_letters = []  # Define a list of letters
    for i in possible_words:  # A loop helps go trough all
        #  the words from the list
        for j in i:  # A loop helps to go trough all the
            #  letters from the word
            list_of_letters.append(j)  # The letter will append
            #  to the list of letters
    return list_of_letters


# 12
def run_single_game(words_list):
    """This function will run a single game of hangman, uses all the
    previous functions. Will get a words list"""
    choosen_word = get_random_word(words_list)  # Define a variable
    #  for the chosen game word
    error_count = 0  # Define a counter for errors done by the user
    wrong_guess_lst = []  # Define a new list of strings for
    # the wrong guesses of the user
    pattern = len(choosen_word) * "_"  # Define the pattern to be as
    #  long as the chosen word with only underlines
    messenger = DEFAULT_MSG  # Define a variable to be the
    #  messenger to the user
    while (pattern != choosen_word) and (error_count < MAX_ERRORS):
        # The loop will be continue only if the pattern is not identical
        #  to the chosen word and the user errors not above
        #  the max error limit
        display_state(pattern, error_count, wrong_guess_lst, messenger)
        # Will print the state of this part of the game to the
        # user using a function from school
        type_of_choice, choosen_letter = get_input()  # Define variables to
        #  the given user input
        if type_of_choice == HINT:  # Check if the user want hint
            possible_words = filter_words_list \
                (words_list, pattern, wrong_guess_lst)  # Call a previous
            #  function that will filter words
            best_hint = choose_letter(possible_words, pattern)  # Call a
            # previous function to get a hint letter
            messenger = HINT_MSG + best_hint  # Updating the message
            #  with the hint letter
        else:
            if (len(choosen_letter) != 1) or choosen_letter.isupper() \
                    or (not (choosen_letter.isalpha())):  # Check if the
                #  user input is not an appropriate letter
                messenger = NON_VALID_MSG  # Updating the message with
                #  a non valid one
            elif choosen_letter in choosen_word:  # Check if the input
                #  letter appears at the chosen word
                pattern, messenger = good_choice \
                    (choosen_word, pattern, choosen_letter, messenger)
                # Call a previous function for updating both the pattern
                #  with the input letter and the message
            elif choosen_letter not in choosen_word:  # Check if the user
                #  input was a letter that not appear at the chosen word
                wrong_guess_lst, error_count, pattern, messenger = \
                    bad_choice(choosen_letter, wrong_guess_lst, error_count,
                               pattern, messenger)  # Call a previous
                # function for updating the wrong guess list
    end_game(choosen_word, wrong_guess_lst, error_count, pattern)


# 13
def main():
    run_single_game(load_words())  # Call a previous function
    #  for a single hangman game
    if get_input()[1]:  # Check if the user wants another
        #  round of hangman game
        main()


if __name__ == "__main__":
    start_gui_and_call_main(main)
    close_gui()
