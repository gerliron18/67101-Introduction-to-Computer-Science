#############################################################
# FILE : ex11_map_coloring.py
# WRITER : Liron Gershuny , gerliron18 , 308350503
# EXERCISE : intro2cs ex11 2017-2018
# DESCRIPTION: A program that uses backtracking method
# to solve problem of graph coloring.
#############################################################
from ex11_backtrack import general_backtracking

# from map_coloring_gui import color_map
# #uncomment if you installed the required libraries

COLORS = ['red', 'blue', 'green', 'magenta', 'yellow', 'cyan']


def read_adj_file(adjacency_file):
    """
    A function that read a file with information sent by the user
    and converted it to a dictionary the program can work with.
    :param adjacency_file: A text file including info about one
           element and the other elements conected to.
    :return: A dictionary that has country's as keys and the neighbors
             of the current country as her value.
    """
    neighbor_dic = {}
    with open(adjacency_file) as neighbors_list:
        for single_line in neighbors_list:
            single_line = single_line.split("\n")
            single_line = single_line[0].split(":")
            country = single_line[0]
            single_line = single_line[1].split(",")
            neighbors = single_line
            if neighbors == [""]:
                neighbors = []
            neighbor_dic[country] = neighbors
    return neighbor_dic


def check_legal_placement(dict_of_colors, country, dict_of_neighbors):
    """
    A function that work with a dictionary and check if one assignment
    is legitimacy.
    :param dict_of_colors: A dictionary includes all the colors
           one country can get as an assignment.
    :param country: The current country that should be assigned.
    :param dict_of_neighbors: A dictionary includes all the neighbors
           of the current country.
    :return: True/False according of the legitimacy of one assignment.
    """
    color = dict_of_colors[country]
    neighbors = dict_of_neighbors[country]
    for neighbor in neighbors:
        color_of_neighbor = dict_of_colors[neighbor]
        if color == color_of_neighbor:
            return False
    return True


def create_list_of_items(dict_of_countries):
    """
    A function that generate list of the elements that should get an
    assignment from the dictionary of country's.
    :param dict_of_countries: A dictionary include the defualt countries
           as keys and it neighbors as values.
    :return: A list of all the countries that should get an assignment.
    """
    list_of_items = []
    for country in dict_of_countries.keys():
        list_of_items.append(country)
    return list_of_items


def run_map_coloring(adjacency_file, num_colors=4, map_type=None):
    """
    The main function that should search for a solution to the
    map coloring problem using backtracking method.
    :param adjacency_file: A file of given neighbors wanted to be solved
    :param num_colors: the number of colors the user want
           to solve the problem with
    :param map_type: The type of map want to be solve.
    :return: A dictionary of all the color assignments as values for country
             keys or None if the problem can't be solved.
    """
    if num_colors == 1:  # The case if the user gave one color only,
        # so that the problem has no legal solution
        return None
    dict_of_neighbors = read_adj_file(adjacency_file)
    list_of_items = create_list_of_items(dict_of_neighbors)
    color_dict = {}
    set_of_assignments = COLORS[:num_colors]
    for country in list_of_items:
        # Give blank assignment to all of the countries
        color_dict[country] = "Blank"
    if general_backtracking(sorted(list_of_items), color_dict, 0,
                            set_of_assignments, check_legal_placement,
                            dict_of_neighbors):
        # Call the backtracking function method for trying to solve the problem
        return color_dict
    return None


def chack_world(country_color_dict, country_neighbers_dict):
    """
    Self check function.
    :param country_color_dict: A dictionary include the defualt countries
           as keys and it neighbors as values.
    :param country_neighbers_dict: A file of given neighbors
           wanted to be solved
    :return: True/False and a print if the check passed or not
    """
    for country in country_color_dict.keys():
        color = country_color_dict[country]
        neighbers = country_neighbers_dict[country]
        for neighber in neighbers:
            if country_color_dict[neighber] == color:
                print("you failed")
                return False
    print("passed")
    return True
