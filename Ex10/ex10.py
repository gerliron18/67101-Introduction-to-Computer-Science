#############################################################
# FILE : ex10.py
# WRITER : Liron Gershuny , gerliron18 , 308350503
# EXERCISE : intro2cs ex10 2017-2018
# DESCRIPTION: A program working with binary trees, uses
# data of illnesses and symptoms given by the user.
#############################################################
import itertools


class Node:
    """
    A class that defines a vertex in binary tree,
    gets the vertex data and information about the vertex "childes".
    3 geters functions were define so we can use all the info save in
    the according vertex.
    """

    def __init__(self, data="", pos=None, neg=None):
        self.data = data
        self.positive_child = pos
        self.negative_child = neg

    def get_data(self):
        return self.data

    def get_positive(self):
        return self.positive_child

    def get_negative(self):
        return self.negative_child


class Record:
    """
    A class that defines single record of one petient, his illness
    and the symptoms he came with to the doctor
    """

    def __init__(self, illness, symptoms):
        self.illness = illness
        self.symptoms = symptoms


def parse_data(filepath):
    """
    This function is a part of the frame given to us,
    uses to arrange data from the user to script class objects.
    :param filepath: A path for data file
    :return: A list of Record class objects
    """
    with open(filepath) as data_file:
        records = []
        for line in data_file:
            words = line.split()
            records.append(Record(words[0], words[1:]))
        return records


class Diagnoser:
    """
    A class that analyzing information about illnesses using binary
    tree functions.
    Gets a root of a tree and will calculate few things using user
    given data.
    """

    def __init__(self, root):
        self.__root = root

    def diagnose_helper(self, node, symptoms):
        """
        This function is diagnose function helper, run along the
        binary tree according to given symptoms and find the data of
        the appropriate "leaf".
        :param node: The current vertex of the tree
        :param symptoms: A list of symptoms
        :return: The data that saved at the appropriate leaf
        """
        if node.get_positive() is None:  # Base case, if we got to a leaf
            return node.get_data()
        else:
            if node.get_data() in symptoms:
                return self.diagnose_helper(node.get_positive(), symptoms)
                # Recursion call for positive child
            else:
                return self.diagnose_helper(node.get_negative(), symptoms)
                # Recursion call for negative child

    def diagnose(self, symptoms):
        """
        This function uses the tree root of the class to check,
        according to the petient symptoms, which illness does he have
        :param symptoms: A list of symptoms
        :return: The appropriate illness according to the petient symptoms
        """
        illness = self.diagnose_helper(self.__root, symptoms)
        # Calling helper function
        return illness

    def calculate_error_rate(self, records):
        """
        This function check the quality of diagnose function, means it
        will go trough all the symptoms according to ones record
        and will check how many times the data at the leaf
        does not match the records that been given
        :param records: a list of record given by the user,
               after converting it by parse_data function above
        :return: The calculated error rate
        """
        neg_counter = 0
        for record in records:
            illness = self.diagnose(record.symptoms)
            if illness not in record.illness:
                # If the illness founded by diagnose function does
                # not match the illness of one's record
                neg_counter += 1
        return neg_counter / len(records)

    def all_illnesses_helper(self, node, illnesses_lst):
        """
        This is a helper function of all_illnesses, going trough all
        the paths of a binary tree using recursion to find all the data
        saved in the tree leafs
        :param node: A one vertex of binary tree
        :param illnesses_lst: A list of all leafs data
        :return: A list of all the leafs data of a binary tree
        """
        if node.get_positive() is None:  # Base case, if we got to a leaf
            if node.get_data() not in illnesses_lst:
                # Check if the founded data haven't founded yet
                illnesses_lst.append(node.get_data())
        else:
            self.all_illnesses_helper(node.get_positive(), illnesses_lst)
            # Recursion call for positive child
            self.all_illnesses_helper(node.get_negative(), illnesses_lst)
            # Recursion call for negative child
        return illnesses_lst

    def all_illnesses(self):
        """
        This function make a list of all the data saved in all the leafs
        of a binary tree. Means all the illnesses founded.
        :return: A list of illnesses generated by a binary tree
        """
        illnesses_lst = []
        illnesses_lst = self.all_illnesses_helper(self.__root, illnesses_lst)
        # Call function helper with the tree root to find all illnesses
        sorted_lst = sorted(illnesses_lst)
        return sorted_lst

    def most_common_illness(self, records):
        """
        This function will go trough a list of given records,
        will use the diagnose function to find the illness
        and use a dictionary to find the most common illness
        of all the records
        :param records: A list of records converted by parse_data function
        :return: The most common illness of given records
        """
        illness_dic = {}
        for record in records:
            illness = self.diagnose(record.symptoms)
            # Find the illness using diagnose function
            if illness in illness_dic:
                illness_dic[illness] += 1
            else:
                illness_dic[illness] = 1
        most_common = max(zip(illness_dic.values(), illness_dic.keys()))
        # Find the max value in a dictionary and save the key at a variable
        return most_common[1]

    def paths_to_illness_helper(self, illness, start, all_paths_lst, path):
        """
        This function help the paths_to_illness function below, will check
        recursivly all possible paths to a given illness and append it to
        a given list
        :param illness: One illness given as a string
        :param start: The current node of the tree
        :param all_paths_lst: A list of all possible paths founded yet
        :param path: One path that is currently check
        :return: Noting will return from this function, it only append paths
                 to a final list
        """
        if start.positive_child is None and start.negative_child is None:
            # Base case, if we got to a leaf
            if start.get_data() == illness:
                all_paths_lst.append(path)
        else:
            self.paths_to_illness_helper(illness, start.positive_child,
                                         all_paths_lst, path + [True])
            # Recursion call for positive child with adding True to the path
            self.paths_to_illness_helper(illness, start.negative_child,
                                         all_paths_lst, path + [False])
            # Recursion call for negative child with adding False to the path

    def paths_to_illness(self, illness):
        """
        This function find all the paths to a given illness of binary tree
        using helper function above.
        :param illness: One illness given as a string
        :return: All paths to the given illness founded as a True/False path
        """
        all_paths_lst = []
        self.paths_to_illness_helper(illness, self.__root, all_paths_lst, [])
        # Call helper function with the tree root and an empty list of paths
        return all_paths_lst


def path_checker(symptoms, path):
    """
    This function check if one path is compatible with a list of symptoms.
    :param symptoms: A list of symptoms
    :param path: One path of binary tree given as a list of lists
    :return: True/False according to the compatibility between the symptoms
             list and the current path
    """
    for symptom in path:  # Going trough all the nodes of the path
        if symptom[1]:  # If the petient have this symptom
            if symptom[0] in symptoms:
                continue
            else:
                return False
        else:  # If the petient does not have this symptom
            if not (symptom[0] in symptoms):
                continue
            else:
                return False
    return True


def most_common_illness_in_path(records, path):
    """
    This function is very familiar to the most_common_illness function
    that in the Diagnose class but now we will find the most common
    illness for one path in a binary tree
    :param records: A list of records converted by parse_data function
    :param path: The current path as a list of lists
    :return: The most common illness of given path
    """
    illness_dic = {}
    for record in records:
        if record.illness not in illness_dic:
            # Add another key to the dictionary and zero his value
            illness_dic[record.illness] = 0
        if path_checker(record.symptoms, path):
            # Use previous function to find the current path illness
            illness_dic[record.illness] += 1
    return max(zip(illness_dic.values(), illness_dic.keys()))[1]
    # Find the max value in a dictionary and return his key


def build_tree_helper(records, symptoms, path, symptom_count):
    """
    This function is a helper function for build_tree function,
    will build the binary tree recursivly using given symptoms.
    :param records: A list of records converted by parse_data function
    :param symptoms: A list of symptoms
    :param path: The current path founded as a list of tuples
    :param symptom_count: A counter of symptoms that help to check
                          if we gone trough all the symptoms
    :return: The root node of the built tree
    """
    if symptom_count == len(symptoms):  # Base case, if we are out of symptoms
        leaf_value = most_common_illness_in_path(records, path)
        # Call previous function to find the illness of one path
        return Node(leaf_value)  # Generate new node for leaf in the tree
    else:
        current_symptom = symptoms[symptom_count]
        positive_child = build_tree_helper(records, symptoms,
                                           path + [[current_symptom, True]],
                                           symptom_count + 1)
        # Recursion call for positive child with adding True to the path
        negative_child = build_tree_helper(records, symptoms,
                                           path + [[current_symptom, False]],
                                           symptom_count + 1)
        # Recursion call for negative child with adding False to the path
        return Node(symptoms[symptom_count], positive_child, negative_child)
        # Generate new node for the tree root


def build_tree(records, symptoms):
    """
    This function will build a binary tree according to a given lists
    of records and symptoms.
    :param records: A list of records converted by parse_data function
    :param symptoms: A list of symptoms
    :return: The root of the built tree
    """
    root = build_tree_helper(records, symptoms, [], 0)
    # Call helper function above with the records and symptoms list
    # empty list and zeroed counter
    return root


def optimal_tree(records, symptoms, depth):
    """
    This function will build binary trees for any of the combinations
    possible from a list of symptoms and will check for the error rate of any
    of those trees. Then it will chose the lowest error rated tree
    from final list of trees and will return this tree root.
    :param records: A list of records converted by parse_data function
    :param symptoms: A list of symptoms
    :param depth: The number of wanted to check floors at a binary tree
    :return: The root of the chosen binary tree
    """
    sub_symptoms = itertools.combinations(symptoms, depth)
    # Find all combinations using itertools module
    trees_rate_lst = []
    for single_sub_symptom in sub_symptoms:
        tree_root = build_tree(records, single_sub_symptom)
        # Building tree for the current symptom and save his root in
        # a variable
        diagnose = Diagnoser(tree_root)
        # Generate a new Diagnoser class object for this tree
        error_rate = diagnose.calculate_error_rate(records)
        # Calculate error rate using inner Diagnoser class function
        trees_rate_lst.append([tree_root, error_rate])
    optimal_pair = min(trees_rate_lst, key=lambda x: x[1])
    # Find the min value list in a list of lists and save it in a variable
    return optimal_pair[0]


if __name__ == "__main__":
    # Manually build a simple tree.
    #                cough
    #          Yes /       \ No
    #        fever           healthy
    #   Yes /     \ No
    # influenza   cold

    flu_leaf = Node("influenza", None, None)
    cold_leaf = Node("cold", None, None)
    inner_vertex = Node("fever", flu_leaf, cold_leaf)
    healthy_leaf = Node("healthy", None, None)
    root = Node("cough", inner_vertex, healthy_leaf)

    diagnoser = Diagnoser(root)

    # Simple test
    # diagnosis = diagnoser.diagnose(["cough"])
    # if diagnosis == "cold":
    #     print("Test passed")
    # else:
    #     print("Test failed. Should have printed cold, printed: ", diagnosis)

    # Add more tests for sections 2-7 here.
    # records = parse_data("Data/big_data.txt")
    # print(diagnoser.calculate_error_rate(records))
    # print(diagnoser.all_illnesses())
    # print(diagnoser.most_common_illness(records))
    # print(diagnoser.paths_to_illness('cold'))
    # print(build_tree(records,['sore_throat','muscle_ache', 'headache']))
    # print(optimal_tree(records,['sore_throat','muscle_ache', 'headache'],2))
