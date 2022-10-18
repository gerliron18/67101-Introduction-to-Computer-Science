#############################################################
# FILE : ex3.py
# WRITER : Liron Gershuny , gerliron18 , 308350503
# EXERCISE : intro2cs ex3 2017-2018
# DESCRIPTION: A program that define 8 functions:
# 1. "Create list"- the function gets an input from the
#    user, will return a list of the inputs related one to
#    the other.
# 2. "Concat list"- the function gets a list of strings,
#    will return the join of the strings together.
# 3. "Average"- the function gets a list of floats and
#    will return the average value.
# 4. "Cyclic"- the function gets 2 lists from any kind,
#    checks if one is the cyclic permutation of the other,
#    will return a boolean True or False.
# 5. "Histogram"- the function gets an integer and a list
#    of integers, will return the histogram of the list
#    as a list.
# 6. "Prime factors"- The function gets an integer,
#    will return a list of the prime factors of the number.
# 7. "Cartesian"- the function gets 2 string lists,
#    will return a list of tuples represent the cartesian
#    product between them.
# 8. "Pairs"- the function gets an integer and a list of
#    integers, check all the possible pairs from the list
#    that their amount equals to the given number.
#    Will return a list of all the appropriate pairs.
#############################################################

def create_list():
    """A function that gets any kind of input from the user,
    convert it to string and insert it to a list. The loop
    will stop only for an empty input"""
    my_list = []
    user_string = str(input())
    while user_string != '':
        my_list.append(user_string)
        user_string = str(input())
    return my_list


def concat_list(str_lst):
    """A function that the user call with a list from any kind,
    the function will return the concatenation of the strings
    from the call function as a string"""
    line = ''
    for sequence in list(str_lst):
        line = line + sequence
    return line


def average(num_list):
    """A function that gets a list of real numbers
    and return their average value"""
    summery = 0  # The summery will sum-up all the given numbers
    if num_list == []:  # Check if the given list is an empty one
        return None
    else:
        for number in num_list:
            summery += number
        return summery / len(num_list)


def cyclic(lst1, lst2):
    """A function that gets 2 lists, check if the second on is a
    cycialic permutation of the first one. Will return a boolean
    True or False according to the answer"""
    if (lst1 or lst2) == []:  # Check if the given lists are empty one
        return True
    else:
        for i in range(len(lst1)):
            if lst1[i:] + lst1[:i] == lst2:  # Check if the combination \
                # between the string at the i index of the first list with \
                # the next strings is equal to the second list
                return True
    return False


def histogram(n, num_list):
    """A function that gets an integer and a list of integers,
    will return the histogram of the list"""
    final_list = [0] * n  # Define the final list with the number of integers \
    # and from now every index of the final_list will work as a counter
    for i in num_list:
        final_list[i] += 1  # Final_list at the i index will add 1
    return final_list


def prime_factors(n):
    """A function that gets a positive integer and will return a list
    of all the primary numbers the number has"""
    all_primes_list = []  # Define the list of all the final primary numbers
    if n == 1:  # Chack if the given number equal 1, will return an empty list
        return all_primes_list
    else:
        for i in range(2,
                       n):  # A for loop that gives a primary number at a time
            while n % i == 0:  # A while loop that will work only if the \
                # for loop primary number still divisible with the given \
                # number without a residue
                all_primes_list.append(i)  # Adding the primary divisible \
                # number at the end of the defined list
                n = n / i  # Dividing the given number with the primary  \
                # number founded
    return all_primes_list


def cartesian(lst1, lst2):
    """A function that gets 2 lists and calculate the cartesian product
    between them. The function will return a list of tuples"""
    cartes_list = []  # Define the final cartesian list as an empty one
    if (lst1 or lst2) == []:  # Check if the given lists are empty
        return cartes_list
    else:
        for n in range(len(lst1)):
            for r in range(len(lst2)):
                cartes_list.append(tuple([lst1[n], lst2[r]]))  # Add a \
                # cartesian product from the 'n' index from the first list \
                # and the 'n' index of the second one to the final cartesian \
                # list
        return cartes_list


def pairs(n, num_list):
    """A function that gets an integer 'n' and a integers list. Will return
    all the pairs that their amount equals the 'n' number"""
    pairs_list = []  # Define the final list of pairs as an empty one
    for i in range(len(num_list)):
        for a in range(i + 1, len(num_list)):
            if num_list[i] + num_list[a] == n:  # Check if index 'i' and \
                # index 'a' in the list amount equals the given 'n' number
                pairs_list.append([num_list[i], num_list[a]])  # If the \
                # amount equals the 'n' number this index pair added to the \
                # final pairs list
            else:
                continue
    return pairs_list
