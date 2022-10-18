#############################################################
# FILE : ex7.py
# WRITER : Liron Gershuny , gerliron18 , 308350503
# EXERCISE : intro2cs ex7 2017-2018
# DESCRIPTION: A program that define few linear recursion
# and un-linear recursion functions.
#############################################################
# 1
def print_to_n(n):
    """A function that print all integers from 1 to given n"""
    if n >= 1:  # As long as n is greater or equal to n
        print_to_n(n - 1)
        print(n)
    return


# 2
def print_reversed(n):
    """A function that print all integers from given n to 1"""
    if n >= 1:  # As long as n is greater or equal to n
        print(n)
        print_reversed(n - 1)
    return


# 3
def has_divisor_smaller_than(n, i):
    """A function that check if given n as a divisor lesser then given i"""
    if i == 1:  # Base case
        return True
    else:  # If i greater then 1
        return n % i != 0 and has_divisor_smaller_than(n, i - 1)


# 4
def is_prime(n):
    """A function that check if given integer is prime number"""
    if n <= 1:  # Check if given integer is lesser or equal to 1
        return False
    return has_divisor_smaller_than(n, n - 1)
    # Call previous function to search for divisors


# 5
def divisors_helper(n, divisor, output_list):
    """A function that helps divisors function find the divisors"""
    if divisor <= n:  # Base case - Check if the given divisor is
        # lesser or equal to given integer
        if n % divisor == 0:  # Check if given integer divides by given number
            output_list.append(divisor)  # Add the divisor to the list
        divisors_helper(n, divisor + 1, output_list)
        # Recursion call with greater divisor
    return output_list


# 6
def divisors(n):
    """A function that make a list of divisors of given integer"""
    output_list = []
    n = abs(n)
    divisor = 1  # Define the first divisor as 1
    output_list = divisors_helper(n, divisor, output_list)
    # Call helper function above
    return output_list


# 7
def factorial(n):
    """A function that calculate the factorial value of an integer"""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# 8
def calc_exp(n, x):
    """A function that calculate x at the power of given number
    divise the factorial given number"""
    x = x ** n  # Calc numerator
    n = factorial(n)  # Calc denominator
    calc = x / n
    return calc


# 9
def exp_n_x(n, x):
    """A function that calculate the exponential summing
    of given integer and real number"""
    if n == 0:  # Base case
        return 1
    return calc_exp(n, x) + exp_n_x(n - 1, x)
    # Call previous function  to calc the summing and recursion call


# 10
def play_hanoi(hanoi, n, src, dest, temp):
    """A function that solve the hanoi game. Called by hanoi_game.py script"""
    if n <= 0:
        return
    elif n == 1:  # Base case
        hanoi.move(src, dest)
    else:
        play_hanoi(hanoi, n - 1, src, temp, dest)
        # Move all disc without the last one to the temporary rod
        play_hanoi(hanoi, 1, src, dest, temp)
        # Move the last disc to the destination rod
        play_hanoi(hanoi, n - 1, temp, dest, src)
        # Move all disc at the temporary rod to the destination rod


# 11
def generate_binary(n, temp_list):
    """A function that generate all the possible binary
    combinations in length n"""
    if n == 0:  # Base case
        return temp_list
    else:
        if len(temp_list) == 0:  # If the given list is empty
            return generate_binary(n - 1, ["0", "1"])
            # Recursive call for last character
        else:  # If the given list is not empty
            return generate_binary(n - 1,
                                   [i + "0" for i in temp_list] + [i + "1" for
                                                                   i in
                                                                   temp_list])
            # Recursive call to generate sequence


# 12
def print_binary_sequences(n):
    """A function that print all binary combinations in length n"""
    final_list = []  # Define final list of combinations
    if n == '' or n == 0:
        print()
    else:
        final_list = generate_binary(n, final_list)
        # Call previous function to generate all possible combinations
        for i in final_list:  # Run along all the final list to print each one
            print(i)


# 13
def find_sequences(n, char_list):
    """A function that generate all possible sequences
    of characters in length n"""
    if n <= 0:
        # Base case - return an empty list if given n is lesser or equal to 0
        return [[]]
    else:  # If n is greater then 0
        result = []  # Define a new list that will contain all combinations
    for temp_letter in find_sequences(n - 1, char_list):
        # Run recursivlly along all the given characters and in range n
        for letter in char_list:  # Run along all given characters
            result.append([letter] + temp_letter)
            # Append to list the combination
    return result


# 14
def print_sequences(char_list, n):
    """A function that print all the possible combinations
    of given characters in length n"""
    final_list = find_sequences(n, char_list)
    # Call previous function to generate all combinations
    for sequence in final_list:  # Run along all the possible combinations
        print("".join(sequence))  # Print from list


# 15
def print_no_repetition_sequences_with_prefix(prefix, char_list, n):
    """A function that generate all possible combinations without
    repetition by given prefix, char list and length n"""
    if len(prefix) == n - 1:
        # Base case - Check if the prefix length is almost in length n
        for letter in char_list:
            # Run along all the letters at the given char_list
            if letter not in prefix:
                # Check if the letter is in the given prefix
                print(prefix + letter)
        return
    for letter in char_list:  # Run along all letters at the given char_list
        if letter not in prefix:  # Check if the letter is in the given prefix
            print_no_repetition_sequences_with_prefix(prefix + letter,
                                                      char_list, n)
            # Recursive call with the new prefix


# 16
def print_no_repetition_sequences(char_list, n):
    """A function that print all the possible combinations of given
    characters in length n with no repetition"""
    if n == 0:  # Check if given integer equals 0
        print("")
    elif n == 1:  # Check if the given integer is 1
        for letter in char_list:  # Run along all letters in given char_list
            print(letter)
        return
    for letter in char_list:
        # If the length n is longer than 1 run along all letters in char_list
        print_no_repetition_sequences_with_prefix(letter, char_list, n)
        # Call previous function to generate all possible combinations


# 17
def no_repetition_sequences_list_with_prefix(prefix, char_list, n):
    """A function that generate all possible combinations of words
    in length n by given prefix and given char_list.
    Will return list of strings"""
    temp_list = []  # Define temporary list
    if len(prefix) == n - 1:  # Check if the given prefix is almost in length n
        for letter in char_list:  # Run along all letters in char_list
            if letter not in prefix:  # Check if the letter is in the prefix
                temp_list.append((prefix + letter))
                # Add the prefix eith the letter to the temporary list
        return temp_list
    for letter in char_list:  # Run along all letters in char_list
        if letter not in prefix:  # Check if the letter is in the prefix
            temp_list.extend(
                no_repetition_sequences_list_with_prefix(prefix + letter,
                                                         char_list, n))
            # Extend the temporary list by recursive
            # call to generate combination
    return temp_list


# 18
def no_repetition_sequences_list(char_list, n):
    """A function that return a list of strings of all possible
    combinations by given char_list and given length n with no repetitions"""
    final_list = []  # Define final list
    if n == 0:  # Check if the given length equal 0
        return [""]
    elif n == 1:  # Check if the given length equal 1
        for letter in char_list:  # Run along all letters in char_list
            final_list.append(letter)
            # Append the final list the checked letter
        return final_list
    for letter in char_list:
        # If length n is greater then 1, reun along
        # all the letters in char_list
        final_list.extend(
            no_repetition_sequences_list_with_prefix(letter, char_list, n))
        # Extend the temporary list by calling to previous
        # function to generate combinations
    return final_list
