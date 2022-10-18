#############################################################
# FILE : ex11_improve_backtrack.py
# WRITER : Liron Gershuny , gerliron18 , 308350503
# EXERCISE : intro2cs ex11 2017-2018
# DESCRIPTION: A program that define functions that should
# improve solving problems of backtracking method.
#############################################################
import ex11_map_coloring as ex11


# from map_coloring_gui import color_map
# uncomment if you installed the required libraries


def back_track_degree_heuristic(adj_dict, colors):
    """
    A function that solve the graph coloring problem in an efficient way
    using backtracking method.
    :param adj_dict: A dictionary that has country's as keys and the neighbors
           of the current country as her value.
    :param colors: A list of colors the problem want to be solve with
    :return: A dictionary of all the color assignments as values for country
             keys or None if the problem can't be solved.
    """
    if len(colors) == 1:  # The case if the user gave one color only,
        # so that the problem has no legal solution
        return None
    list_of_items = sorted(adj_dict, key=lambda k: len(adj_dict[k]),
                           reverse=True)
    # Sort the given adjecents file from the key that has
    # the longest list of neighbors to the shortest
    color_dict = {}
    set_of_assignments = colors
    for country in list_of_items:
        # Give blank assignment to all of the countries
        color_dict[country] = "Blank"
    if ex11.general_backtracking(list_of_items, color_dict, 0,
                                 set_of_assignments,
                                 ex11.check_legal_placement,
                                 adj_dict):
        # Call for general backtracking function from anouther program
        return color_dict
    return None


############################################################################

def back_track_MRV(adj_dict, colors):
    """
    This function manage the search for the country that did not
    get any assignment and has the lowest amount of possible
    ones, this neighbor country should get the next assign.
    :param adj_dict: A dictionary that has country's as keys and the neighbors
                     of the current country as her value.
    :param colors: A list of colors the problem want to be solve with
    :return: A dictionary of all the color assignments as values for country
             keys or None if the problem can't be solved.
    """
    color_amount = len(colors)
    if color_amount == 1:  # Base case, If we are out of colors to check
        return None
    list_of_countries = ex11.create_list_of_items(adj_dict)
    set_of_assignments = colors
    color_dict = {}  # Initiates a color_dict
    for country in list_of_countries:
        color_dict[country] = None
    if MRV_backtracking(sorted(list_of_countries), color_dict, color_amount,
                        set_of_assignments, ex11.check_legal_placement,
                        adj_dict):
        # Call the backtrack function for this function
        return color_dict
    return None


def create_dict_of_legal_assignment_amount(num_of_colors, color_dict,
                                           adj_dict):
    """
    This function check at any loop what is the amount of assignment
    left.
    :param num_of_colors: The amount of colors the problem
           want to be solve with
    :param color_dict: A dictionary of country's and there possible
                       color assignments. If the current country as no
                       possible assignment, it will get None value.
    :param adj_dict: A dictionary that has country's as keys and the neighbors
                     of the current country as her value.
    :return: Creates a dictionary where the keys are the names of countries,
             and the values are an int of the amount of legal
             assignments the country has.
    """
    amount_of_legal_assignment_left = {}
    for country, neighbors_list in adj_dict.items():
        neighbor_colors = set()
        count = len(neighbor_colors)
        for neighbor in neighbors_list:
            if color_dict[neighbor] is not None:
                neighbor_colors.add(color_dict[neighbor])
        if color_dict[country] is None:
            amount_of_legal_assignment_left[country] = num_of_colors - count
    return amount_of_legal_assignment_left


def next_country_founder(amount_of_legal_assignment_left):
    """
    This function search for the next country that should be assigned
    according to the condition of the one who has the lowest amount of
    assignments left.
    :param amount_of_legal_assignment_left: A dictionary where the
           keys are the names of countries,
           and the values are an int of the amount of legal
           assignments the country has.
     :return: the country with the lowest amount of legal assignments.
    """
    next_country_to_color = min(amount_of_legal_assignment_left,
                                key=amount_of_legal_assignment_left.get)
    return next_country_to_color


def MRV_backtracking(list_of_items, color_dict, color_amount,
                     set_of_assignments, legal_assignment_func,
                     dict_of_neighbors):
    """
    A backtrack function for the improved search by the lowest
    amount of assignments left for the neighbor country.
    :param list_of_items: A list of elements we would like to
                          give an assignment.
    :param color_dict: A dictionary of country's and there possible
                       color assignments. If the current country as no
                       possible assignment, it will get None value.
    :param color_amount: The color amount that the problem should
            be solved with
    :param set_of_assignments: A list of all the legal posting
                               values means all the colors,
                               will pose as the dict_items_to_vals values.
    :param legal_assignment_func: A pointer to dedicated function
                                  that checks the correction of one assignment.
    :param dict_of_neighbors: A dictionary that has country's as keys
            and the neighbors of the current country as her value.
    :return: True/False if it find a legal solution to a problem.
    """
    if None not in color_dict.values():  # Base case
        return True
    legal_assignment_amount = create_dict_of_legal_assignment_amount(
        color_amount, color_dict, dict_of_neighbors)
    next_country_to_color = next_country_founder(legal_assignment_amount)
    backtrack_value = color_dict[next_country_to_color]
    for color in set_of_assignments:
        color_dict[next_country_to_color] = color
        if legal_assignment_func(color_dict, next_country_to_color,
                                 dict_of_neighbors):
            if MRV_backtracking(list_of_items, color_dict, color_amount,
                                set_of_assignments, legal_assignment_func,
                                dict_of_neighbors):
                return True
    color_dict[next_country_to_color] = backtrack_value
    return False


##############################################################################

def back_track_FC(adj_dict, colors):
    """
    This function check not only the country that got an assignment
    but if the assignment cause a situation where anouther country
    left with no legal assignment at all.
    This improvment call "forward checking".
    :param adj_dict: A dictionary that has country's as keys and the neighbors
                     of the current country as her value.
    :param colors: A list of colors the problem want to be solve with
    :return: A dictionary of all the color assignments as values for country
             keys or None if the problem can't be solved.
    """
    color_amount = len(colors)
    if color_amount == 1:  # Base case, If we are out of colors to check
        return None
    list_of_items = ex11.create_list_of_items(adj_dict)
    color_dict = {}
    set_of_assignments = colors
    for country in list_of_items:
        color_dict[country] = None
    if ex11.general_backtracking(sorted(list_of_items), color_dict, 0,
                                 set_of_assignments, FC_check_legal_helper,
                                 adj_dict, color_amount):
        return color_dict
    return False


def FC_check_legal_helper(color_dict, country, dict_of_neighbors,
                          color_amount):
    """
    A function that check for the legit of the forward checking.
    :param color_dict: A dictionary of country's and there possible
                       color assignments. If the current country as no
                       possible assignment, it will get None value.
    :param country: The current country wanted to b checked
    :param dict_of_neighbors: A dictionary that has country's as keys
            and the neighbors of the current country as her value.
    :param color_amount: The amount of colors the problem want to be solve with
    :return: True/False if the condition of forward checking function is legal
    """
    if ex11.check_legal_placement(color_dict, country, dict_of_neighbors):
        if forward_checking(color_dict, country, dict_of_neighbors,
                            color_amount):
            return True
    return False


def forward_checking(color_dict, country, dict_of_neighbors, color_amount):
    """

    :param color_dict:
    :param country: The current country wanted to b checked
    :param dict_of_neighbors:  A dictionary that has country's as
            keys and the neighbors of the current country as her value.
    :param color_amount: The amount of colors the problem want to be solve with
    :return: True/False if the condition of is legal
    """
    color_set = set()
    color_set.add(color_dict[country])
    for neighbor_of_A in dict_of_neighbors[country]:
        for neighbor_of_B in dict_of_neighbors[neighbor_of_A]:
            if color_dict[neighbor_of_B] is not None:
                color_set.add(color_dict[neighbor_of_B])
        if len(color_set) == color_amount:
            return False
    return True


###############################################################################

def back_track_LCV(adj_dict, colors):
    """
    This function runs the LCV backtrack which attempts to improve the
    general_backtrack function, by "hinting" what color should be chosen next.
    It does so by figuring out what color will leave the neighbors with the
    most amount of options to be colored, and then sending the colors in
    that order to the backtracking function.
    :param adj_dict: A dictionary with keys as countries and values as a
    list of the country's neighbors.
    :param colors: A list of colors to assign to each country
    :return: A dictionary where the keys are countries and the values are a
    color assigned to each country, so no two neighboring countries have
    the same color.
    """
    num_colors = len(colors)

    if num_colors == 1:
        return None

    dict_of_neighbors = adj_dict
    list_of_items = ex11.create_list_of_items(dict_of_neighbors)
    color_dict = {}
    set_of_assignments = colors

    for i in list_of_items:
        color_dict[i] = None

    if LCV_backtracking(sorted(list_of_items), color_dict, 0,
                        colors, ex11.check_legal_placement,
                        dict_of_neighbors, colors):
        return color_dict
    return None


def get_set_of_assingments_LCV(country, color_dict, neighbor_dict, colors):
    """
    This function finds what colors the backtracking function should try by
    giving each color a score (in the score_dict) and then returning a list of
    the colors in order in which the color with the highest score appears
    first.
    :param country: A string representing a country which will get the next
    color assignment.
    :param color_dict: A dictionary where the key are all the countries and
    the values are the colors of the county. If the country is not colored,
    it's value is None.
    :param neighbor_dict: a dictionary where the keys are names of
    countries and the values are a list of all that countries neighbors. If
    the country has no neighbors, it's value is an empty list.
    :param colors: A list of the given colors
    :return: A list of colors in descending order based on their score.
    """
    score_dict = {}
    for color in colors:
        score_dict[color] = get_color_score(color, country, color_dict,
                                            neighbor_dict, colors)

    sorted_colors = []
    for key in sorted(score_dict, key=lambda key: (score_dict[key]),
                      reverse=True):
        sorted_colors.append(key)
    return sorted_colors


def get_color_score(color, country, color_dict, neighbor_dict, colors):
    """

    :param color: A string representing a color that we are getting its score
    :param country: The next country which will be assigned a color.
    :param color_dict: A dictionary where the key are all the countries and
    the values are the colors of the county. If the country is not colored,
    it's value is None.
    :param neighbor_dict: A dictionary where the keys are names of
    countries and the values are a list of all that countries neighbors. If
    the country has no neighbors, it's value is an empty list.
    :return: The color's score (which is based on the amount of colors its
    neighbors can get. The higher the score the fewer restrictions assinging
    that color will cause.)
    """
    color_dict[country] = color

    score = 0

    for neighbor in neighbor_dict[country]:
        neighbor_score = num_of_potential_colors(neighbor_dict, color_dict,
                                                 neighbor, colors)
        score += neighbor_score
    return score


def num_of_potential_colors(neighbor_dict, color_dict, country, colors):
    """
    This function calculates the number of potential colors a country can
    get, based on its neighbors colors.
    :param neighbor_dict: A dictionary where the keys are names of
    countries and the values are a list of all that countries neighbors. If
    the country has no neighbors, it's value is an empty list.
    :param color_dict: A dictionary where the key are all the countries and
    the values are the colors of the county. If the country is not colored,
    it's value is None.
    :param country: The country which is next on line to be colored.
    :param colors: A list of the legal colors.
    :return: An int representing the number of colors that country can
    potentially have.
    """

    potential_color = set()
    neighbor_colors = []

    for neighbor in neighbor_dict[country]:
        if color_dict[neighbor] != None:
            neighbor_colors.append(color_dict[neighbor])

    for color in colors:
        if color not in neighbor_colors:
            potential_color.add(color)

    return len(potential_color)


def LCV_backtracking(list_of_items, color_dict, index,
                     colors, legal_assignment_func,
                     *args):
    """
    :param list_of_items: list of countries/states we want to color
    :param color_dict: A dictionary where the key are all the countries and
    the values are the colors of the county. If the country is not colored,
    it's value is None.
    :param index: int that represents the place of the item (from the
    list_of_items) that we are trying to update at any given point during
    the recursion.
    :param set_of_assignments: A list of colors to assign to a country.
    This list is updated inside this function.
    :param legal_assignment_func: a pointer to a function that checks if a
    placement is legal.
    :param args: other parameters that may be added
    :return: If a solution was found, the function will return the
    dictioanry of colors. If not solution was found, the function will
    return None.
    """

    neighbor_dict = args[0]

    if index > len(list_of_items) - 1:
        return True

    backtrack_value = color_dict[list_of_items[index]]

    set_of_assignments = get_set_of_assingments_LCV(list_of_items[index],
                                                    color_dict,
                                                    neighbor_dict, colors)

    for i in set_of_assignments:
        color_dict[list_of_items[index]] = i
        if legal_assignment_func(color_dict, list_of_items[index],
                                 neighbor_dict):
            if LCV_backtracking(list_of_items, color_dict,
                                index + 1, set_of_assignments,
                                legal_assignment_func, *args):
                return True
    color_dict[list_of_items[index]] = backtrack_value
    return None


##############################################################################

def fast_back_track(adj_dict, colors):
    """
    Bonus function.
    :param adj_dict:
    :param colors:
    :return:
    """
    pass
