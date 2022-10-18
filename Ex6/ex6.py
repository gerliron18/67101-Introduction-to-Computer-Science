#############################################################
# FILE : ex6.py
# WRITER : Liron Gershuny , gerliron18 , 308350503
# EXERCISE : intro2cs ex6 2017-2018
# DESCRIPTION: A script for filtering grey scale images and
# rotate pictures according to dominate angel in it
#############################################################
from ex6_helper import *
import sys
import copy
import math

BLACK = 0  # Define the value of black color pixel
WHITE = 255  # Define the value of white color pixel


def calc_avg(list_of_num):
    """A function that calculate the average value of list of numbers"""
    count = len(list_of_num)
    sum = 0
    for i in list_of_num:  # Run along the numbers from the numbers list
        sum += i
    if count == 0:  # For dividing by zero case, will return 0
        avg = 0
    else:
        avg = sum / count
    return avg, count


def mean_calc(image, candidate):
    """A function that create 2 lists of numbers according to a given number,
    one for all numbers that are less than the number and one for
    all numbers that are grater than the given number"""
    mean_back_list = []
    mean_fore_list = []
    for row in image:  # Run along the rows of given image
        for pixel in row:  # Run along the pixel of given row
            if pixel > candidate or pixel == candidate:
                # Check if the pixel value is grater or lesser
                # than the given number
                mean_fore_list.append(pixel)
            else:
                mean_back_list.append(pixel)
    mean_back, num_back = calc_avg(mean_back_list)
    mean_fore, num_fore = calc_avg(mean_fore_list)
    return mean_back, num_back, mean_fore, num_fore


def otsu(image):
    """A function that calculate the intra variance of given matrix, will
    return threshold as the max value of intra variance founded"""
    threshold = 0
    intra_variance = 0
    for candidate in range(WHITE + 1):  # Run along all possible thresholds
        mean_back, num_back, mean_fore, num_fore = mean_calc(image, candidate)
        intra_variance_candid = num_back * num_fore * \
                                (mean_back - mean_fore) ** 2
        # Calculate the intra variance
        if intra_variance < intra_variance_candid:  # Check if the caculated
            #  intra variance is bigger than the max value founded
            intra_variance = intra_variance_candid
            threshold = candidate
    return threshold


def threshold_filter(image):
    """A function that gets an image as a list of lists of numbers constitute
    the value of appropriate color of one pixel, will use otsu function to
    find the best threshold for her and return new image that gets black
    colored pixel for pixels that are lesser than the calculated threshold
    and white colored pixel for the greater than the threshold"""
    filtered_image = copy.deepcopy(image)  # Deep copy the given image
    threshold = otsu(
        image)  # Use otsu function to find the best threshold value
    for row in range(len(image)):  # Run along the rows of given image
        for pixel in range(len(image[row])):
            # Run along the pixel of given row
            if image[row][pixel] < threshold:
                # Check if the pixel value is greater than the threshold
                filtered_image[row][pixel] = BLACK
            else:  # If the pixel value is lesser than the threshold
                filtered_image[row][pixel] = WHITE
    return filtered_image


def left_up_corner(row, column, image, filter):
    """Calculate the filtered value for left up corner pixel of given image"""
    filter_value = ((filter[0][0]) * (image[row][column])) + \
                   ((filter[0][1]) * (image[row][column])) + \
                   ((filter[0][2]) * (image[row][column])) + \
                   ((filter[1][0]) * (image[row][column])) + \
                   ((filter[1][1]) * (image[row][column])) + \
                   ((filter[1][2]) * (image[row][column + 1])) + \
                   ((filter[2][0]) * (image[row][column])) + \
                   ((filter[2][1]) * (image[row + 1][column])) + \
                   ((filter[2][2]) * (image[row + 1][column + 1]))
    return filter_value


def right_up_corner(row, column, image, filter):
    """Calculate the filtered value for right up corner pixel
    of given image"""
    filter_value = ((filter[0][0]) * (image[row][column])) + \
                   ((filter[0][1]) * (image[row][column])) + \
                   ((filter[0][2]) * (image[row][column])) + \
                   ((filter[1][0]) * (image[row][column - 1])) + \
                   ((filter[1][1]) * (image[row][column])) + \
                   ((filter[1][2]) * (image[row][column])) + \
                   ((filter[2][0]) * (image[row + 1][column - 1])) + \
                   ((filter[2][1]) * (image[row + 1][column])) + \
                   ((filter[2][2]) * (image[row][column]))
    return filter_value


def up_level(row, column, image, filter):
    """Calculate the filtered value for first row pixels without corners
    of given image"""
    filter_value = ((filter[0][0]) * (image[row][column])) + \
                   ((filter[0][1]) * (image[row][column])) + \
                   ((filter[0][2]) * (image[row][column])) + \
                   ((filter[1][0]) * (image[row][column - 1])) + \
                   ((filter[1][1]) * (image[row][column])) + \
                   ((filter[1][2]) * (image[row][column + 1])) + \
                   ((filter[2][0]) * (image[row + 1][column - 1])) + \
                   ((filter[2][1]) * (image[row + 1][column])) + \
                   ((filter[2][2]) * (image[row + 1][column + 1]))
    return filter_value


def left_down_corner(row, column, image, filter):
    """Calculate the filtered value for left down corner pixel
    of given image"""
    filter_value = ((filter[0][0]) * (image[row][column])) + \
                   ((filter[0][1]) * (image[row - 1][column])) + \
                   ((filter[0][2]) * (image[row - 1][column + 1])) + \
                   ((filter[1][0]) * (image[row][column])) + \
                   ((filter[1][1]) * (image[row][column])) + \
                   ((filter[1][2]) * (image[row][column + 1])) + \
                   ((filter[2][0]) * (image[row][column])) + \
                   ((filter[2][1]) * (image[row][column])) + \
                   ((filter[2][2]) * (image[row][column]))
    return filter_value


def right_down_corner(row, column, image, filter):
    """Calculate the filtered value for right down corner pixel
    of given image"""
    filter_value = ((filter[0][0]) * (image[row - 1][column - 1])) + \
                   ((filter[0][1]) * (image[row - 1][column])) + \
                   ((filter[0][2]) * (image[row][column])) + \
                   ((filter[1][0]) * (image[row][column - 1])) + \
                   ((filter[1][1]) * (image[row][column])) + \
                   ((filter[1][2]) * (image[row][column])) + \
                   ((filter[2][0]) * (image[row][column])) + \
                   ((filter[2][1]) * (image[row][column])) + \
                   ((filter[2][2]) * (image[row][column]))
    return filter_value


def down_level(row, column, image, filter):
    """Calculate the filtered value for last row pixels without corners
    of given image"""
    filter_value = ((filter[0][0]) * (image[row - 1][column - 1])) + \
                   ((filter[0][1]) * (image[row - 1][column])) + \
                   ((filter[0][2]) * (image[row - 1][column + 1])) + \
                   ((filter[1][0]) * (image[row][column - 1])) + \
                   ((filter[1][1]) * (image[row][column])) + \
                   ((filter[1][2]) * (image[row][column + 1])) + \
                   ((filter[2][0]) * (image[row][column])) + \
                   ((filter[2][1]) * (image[row][column])) + \
                   ((filter[2][2]) * (image[row][column]))
    return filter_value


def left_level(row, column, image, filter):
    """Calculate the filtered value for first column pixels without corners
    of given image"""
    filter_value = ((filter[0][0]) * (image[row][column])) + \
                   ((filter[0][1]) * (image[row - 1][column])) + \
                   ((filter[0][2]) * (image[row - 1][column + 1])) + \
                   ((filter[1][0]) * (image[row][column])) + \
                   ((filter[1][1]) * (image[row][column])) + \
                   ((filter[1][2]) * (image[row][column + 1])) + \
                   ((filter[2][0]) * (image[row][column])) + \
                   ((filter[2][1]) * (image[row + 1][column])) + \
                   ((filter[2][2]) * (image[row + 1][column + 1]))
    return filter_value


def right_level(row, column, image, filter):
    """Calculate the filtered value for last column pixels without corners
    of given image"""
    filter_value = ((filter[0][0]) * (image[row - 1][column - 1])) + \
                   ((filter[0][1]) * (image[row - 1][column])) + \
                   ((filter[0][2]) * (image[row][column])) + \
                   ((filter[1][0]) * (image[row][column - 1])) + \
                   ((filter[1][1]) * (image[row][column])) + \
                   ((filter[1][2]) * (image[row][column])) + \
                   ((filter[2][0]) * (image[row + 1][column - 1])) + \
                   ((filter[2][1]) * (image[row + 1][column])) + \
                   ((filter[2][2]) * (image[row][column]))
    return filter_value


def normal_pixels(row, column, image, filter):
    """Calculate the filtered value for pixels that are not at the borders
    of given image"""
    filter_value = ((filter[0][0]) * (image[row - 1][column - 1])) + \
                   ((filter[0][1]) * (image[row - 1][column])) + \
                   ((filter[0][2]) * (image[row - 1][column + 1])) + \
                   ((filter[1][0]) * (image[row][column - 1])) + \
                   ((filter[1][1]) * (image[row][column])) + \
                   ((filter[1][2]) * (image[row][column + 1])) + \
                   ((filter[2][0]) * (image[row + 1][column - 1])) + \
                   ((filter[2][1]) * (image[row + 1][column])) + \
                   ((filter[2][2]) * (image[row + 1][column + 1]))
    return filter_value


def occurrence_filter(row, column, length, width, image, filter):
    """A function that check the occurrence of given row and column, will call
    the appropriate function above to get the filtered pixel value"""
    if row == 0:
        if column == 0:  # Check for left up corner case
            filter_value = left_up_corner(row, column, image, filter)
        elif column + 1 == width:  # Check for right up corner case
            filter_value = right_up_corner(row, column, image, filter)
        else:  # Check for first row pixels case
            filter_value = up_level(row, column, image, filter)
    elif row + 1 == length:
        if column == 0:  # Check for left down corner case
            filter_value = left_down_corner(row, column, image, filter)
        elif column + 1 == width:  # Check for right down corner case
            filter_value = right_down_corner(row, column, image, filter)
        else:  # Check for last row pixels case
            filter_value = down_level(row, column, image, filter)
    else:
        if column == 0:  # Check for first column pixels case
            filter_value = left_level(row, column, image, filter)
        elif column + 1 == width:  # Check for last column pixels case
            filter_value = right_level(row, column, image, filter)
        else:  # Check for not at the borders pixels case
            filter_value = normal_pixels(row, column, image, filter)
    return filter_value


def left_up_corner_edge(row, column, image, num_list):
    """Calculate the edged value for left up corner pixel of given image"""
    for i in range(5):
        num_list.append(image[row][column])
    num_list.append(image[row][column + 1])
    num_list.append(image[row + 1][column])
    num_list.append(image[row + 1][column + 1])
    edges_value = calc_avg(num_list)
    return edges_value


def right_up_corner_edge(row, column, image, num_list):
    """Calculate the edged value for right up corner pixel of given image"""
    for i in range(5):
        num_list.append(image[row][column])
    num_list.append(image[row][column - 1])
    num_list.append(image[row + 1][column])
    num_list.append(image[row + 1][column - 1])
    edges_value = calc_avg(num_list)
    return edges_value


def up_level_edge(row, column, image, num_list):
    """Calculate the edged value for first row pixels without corners
    of given image"""
    for i in range(3):
        num_list.append(image[row][column])
    num_list.append(image[row][column - 1])
    num_list.append(image[row][column + 1])
    num_list.append(image[row + 1][column - 1])
    num_list.append(image[row + 1][column])
    num_list.append(image[row + 1][column + 1])
    edges_value = calc_avg(num_list)
    return edges_value


def left_down_corner_edge(row, column, image, num_list):
    """Calculate the edged value for left down corner pixel of given image"""
    for i in range(5):
        num_list.append(image[row][column])
    num_list.append(image[row - 1][column])
    num_list.append(image[row - 1][column + 1])
    num_list.append(image[row][column + 1])
    edges_value = calc_avg(num_list)
    return edges_value


def right_down_corner_edge(row, column, image, num_list):
    """Calculate the edged value for right down corner pixel
    of given image"""
    for i in range(5):
        num_list.append(image[row][column])
    num_list.append(image[row - 1][column])
    num_list.append(image[row - 1][column - 1])
    num_list.append(image[row][column - 1])
    edges_value = calc_avg(num_list)
    return edges_value


def down_level_edge(row, column, image, num_list):
    """Calculate the edged value for last row pixels without corners
    of given image"""
    for i in range(3):
        num_list.append(image[row][column])
    num_list.append(image[row][column - 1])
    num_list.append(image[row][column + 1])
    num_list.append(image[row - 1][column - 1])
    num_list.append(image[row - 1][column])
    num_list.append(image[row - 1][column + 1])
    edges_value = calc_avg(num_list)
    return edges_value


def left_level_edge(row, column, image, num_list):
    """Calculate the edged value for first column pixels without corners
    of given image"""
    for i in range(3):
        num_list.append(image[row][column])
    num_list.append(image[row - 1][column])
    num_list.append(image[row - 1][column + 1])
    num_list.append(image[row][column + 1])
    num_list.append(image[row + 1][column])
    num_list.append(image[row + 1][column + 1])
    edges_value = calc_avg(num_list)
    return edges_value


def right_level_edge(row, column, image, num_list):
    """Calculate the edged value for last column pixels without corners
    of given image"""
    for i in range(3):
        num_list.append(image[row][column])
    num_list.append(image[row - 1][column])
    num_list.append(image[row - 1][column - 1])
    num_list.append(image[row][column - 1])
    num_list.append(image[row + 1][column])
    num_list.append(image[row + 1][column - 1])
    edges_value = calc_avg(num_list)
    return edges_value


def normal_pixels_edge(row, column, image, num_list):
    """Calculate the edged value for pixels that are not at the borders
    of given image"""
    num_list.append(image[row - 1][column])
    num_list.append(image[row - 1][column - 1])
    num_list.append(image[row - 1][column + 1])
    num_list.append(image[row][column - 1])
    num_list.append(image[row][column + 1])
    num_list.append(image[row + 1][column])
    num_list.append(image[row + 1][column - 1])
    num_list.append(image[row + 1][column + 1])
    edges_value = calc_avg(num_list)
    return edges_value


def occurrence_edges(row, column, length, width, image):
    """A function that check the occurrence of given row and column, will call
    the appropriate function above to get the edged pixel value"""
    num_list = []
    if row == 0:
        if column == 0:  # Check for left up corner case
            edges_value = left_up_corner_edge(row, column, image, num_list)
        elif column + 1 == width:  # Check for right up corner case
            edges_value = right_up_corner_edge(row, column, image, num_list)
        else:  # Check for first row pixels case
            edges_value = up_level_edge(row, column, image, num_list)
    elif row + 1 == length:
        if column == 0:  # Check for left down corner case
            edges_value = left_down_corner_edge(row, column, image, num_list)
        elif column + 1 == width:  # Check for right down corner case
            edges_value = right_down_corner_edge(row, column, image, num_list)
        else:  # Check for last row pixels case
            edges_value = down_level_edge(row, column, image, num_list)
    else:
        if column == 0:  # Check for first column pixels case
            edges_value = left_level_edge(row, column, image, num_list)
        elif column + 1 == width:  # Check for last column pixels case
            edges_value = right_level_edge(row, column, image, num_list)
        else:  # Check for not at the borders pixels case
            edges_value = normal_pixels_edge(row, column, image, num_list)
    return edges_value


def apply_filter(image, filter):
    """A function that get an image as a list of lists of numbers and a filter
    matrix, will use the occurrence function above to calculate filtered value
    of any pixel. Will return filtered image at the same size"""
    new_image = copy.deepcopy(image)  # Deep copy the given image
    length = len(image)
    width = len(image[0])
    for row in range(length):  # Run along the rows of given image
        for column in range(width):  # Run along the columns of given row
            filter_value = occurrence_filter(row, column, length, width, image,
                                             filter)  # Call previous function
            if filter_value != int:
                # Check if the filtered value is not an integer
                filter_value = int(filter_value)
                if filter_value < BLACK:
                    # Check if the filtered value is less than zero
                    filter_value = abs(filter_value)
                    # Filter value will get the absolute value of itself
                    if filter_value > WHITE:
                        # Check if the filtered value is greater than 255
                        new_image[row][column] = WHITE
                        # Filter value will get the white value
                elif filter_value > WHITE:
                    # Check if the filtered value is greater than 255
                    new_image[row][column] = WHITE
                    # Filter value will get the white value
                else:  # For case of appropriate value between zero and 255
                    new_image[row][column] = filter_value
    return new_image


def detect_edges(image):
    """A function that get an image as a list of lists of numbers,
    will use the occurrence function above to calculate edged value
    of any pixel by finding the average value of all rounded pixels.
    Will return edged image at the same size"""
    new_image = copy.deepcopy(image)  # Deep copy the given image
    length = len(image)
    width = len(image[0])
    for row in range(length):  # Run along the rows of given image
        for column in range(width):  # Run along the columns of given row
            edges_value = occurrence_edges(row, column, length, width, image)
            # Call previous function
            edges_value = image[row][column] - int(edges_value[0])
            if edges_value < BLACK:
                # Check if the edged value is less than zero
                edges_value = abs(edges_value)
                # Edges value will get the absolute value of itself
                if edges_value > WHITE:
                    # Check if the filtered value is greater than 255
                    new_image[row][column] = WHITE
                    # Edges value will get the white value
            elif edges_value > WHITE:
                # Check if the edges value is greater than 255
                new_image[row][column] = WHITE
                # Edges value will get the white value
            else:  # For case of appropriate value between zero and 255
                new_image[row][column] = edges_value
    return new_image


def downsample_by_3(image):
    """A function that get an image as list of lists of numbers, will use
    the filtering function above to sample the given image by 3. Will
    return new sampled image as list of lists of numbers"""
    new_image = []
    width_list = []  # Define new list for one row in the sampled image
    length = len(image)
    width = len(image[0])
    filter_mat = [[(1 / 9)] * 3] * 3
    # Define a filtering matrix that will help calculate the average value
    for row in range(1, length, 3):
        # Run along the rows from 1 to the length of the image at steps of 3
        for column in range(1, width, 3):
            # Run along the columns from 1 to the width
            # of the image at steps of 3
            width_list.append(int(
                occurrence_filter(row, column, length, width, image,
                                  filter_mat)))
            # Add the filtered value to the row list of the new sampled image
        new_image.append(width_list)
        # The sampled image gets one final row after filtering
        width_list = []  # Equate to zero the list to be ready for next row
    return new_image


def downsample(image, max_diagonal_size):
    """A function that get an image as list of lists of numbers and max value
    of diagonal, will use the downsample_by_3 function above to sample the
    given image till its diagonal won't be greater then the given
    diagonal size. Will return new sampled image as list of lists of numbers"""
    new_image = copy.deepcopy(image)  # Deep copy the given image
    length = len(image)
    width = len(image[0])
    while (math.sqrt((length ** 2) + (width ** 2))) > max_diagonal_size:
        # A while loop that will executed till the new diagonal size
        # will be lesser than the given max diagonal size
        new_image = downsample_by_3(image)  # Call previous function
        length = len(new_image)
        width = len(new_image[0])
    return new_image


def pair_distance(start_codon, stop_codon):
    """A function that calculate the range between 2 given pixels"""
    pair_distance = math.sqrt((((stop_codon[0]) - (start_codon[0])) ** 2) + (
        ((stop_codon[1]) - (start_codon[1])) ** 2))
    return pair_distance


def find_in_line(image, cordinate_list):
    """A function that get an image as list of lists of numbers and a list of
    coordinates of pixels at one row. Will check for consecutive white colored
    pixels, calculate the range of each white section at the given row. Will
    return the total white range of given row"""
    total_distance = 0  # Define variable for calculated total range of white
    #  color at a single line
    start_codon = None  # Define start coordinate of white color pixel
    for pixel in cordinate_list:  # Run along all the pixels at the given line
        if image[pixel[0]][pixel[1]] == WHITE:
            # Check if the pixel color is white
            if start_codon is None:  # Check if the start coordinate is empty
                start_codon = pixel
            stop_codon = pixel
        else:  # If the pixel color is not white
            if start_codon is None:  # Check if the start coordinate is empty
                continue
            elif pair_distance(pixel, stop_codon) < 2:
                # Check if the distance between the checked pixel
                # and the stop coordinate is lesser than 2 by using
                # previous function
                continue
            else:  # If we found a start coordinate and stop coordinate that
                # have only white color between one to the other and
                # the distance between them is more than 2
                total_distance += (pair_distance(start_codon, stop_codon)) ** 2
                # Calculate the distance of single white section and add it
                # to the total white distance of the line
                start_codon = None
                # Empty the start coordinate for a new search
    if start_codon != None:
        # Check if the last pixel is an end of white section at the line
        total_distance += (pair_distance(start_codon, stop_codon)) ** 2
        # Calculate the distance of single white section and add it
        # to the total white distance of the line
    return total_distance


def get_angle(image):
    """A function that get an image as a list of lists of numbers, search for
    the dominate angle in it. Will return the dominate angle"""
    length = len(image)  # Calculate the length of the original image
    width = len(image[0])  # Calculate the width of the original image
    diagonal = int(math.sqrt((length ** 2) + (width ** 2)))
    # Calculate the distance of the original image diagonal
    total_distance = 0  # Equate to zero a variable that will get the
    # total white color range at one line
    choosen_angle = 0  # Equate to zero a variable that will get the
    # best founded angle
    for angle in range(180):
        # Run along all the possible angles between 0 to 179
        diagonal_distance = 0  # Equate to zero a variable that will get the
        # total white color range at one diagonal
        for distance in range(diagonal + 1):  # Run along the all the
            # distances between zero to the diagonal of the priginal image
            if 0 < angle < 90:
                pixel_up_list = pixels_on_line(image, math.radians(angle),
                                               distance)
                # Call helper script to get al list of coordinates
                # in one down diagonal
                distance_up = find_in_line(image, pixel_up_list)
                # Call previous function to get the range of white
                # color in one single line
                pixel_down_list = pixels_on_line(image, math.radians(angle),
                                                 distance, False)
                # Call helper script to get al list of coordinates
                # in one upper diagonal
                distance_down = find_in_line(image, pixel_down_list)
                # Call previous function to get the range of white
                # color in one single line
                diagonal_distance += distance_up + distance_down
                # The total diagonal distance of white color for this
                # angle will be the sum of two caculated ranges above
            else:  # If the angle is zero or above 90 degrees
                cordinate_list = pixels_on_line(image, math.radians(angle),
                                                distance)
                # Call helper script to get al list of coordinates
                # in one down diagonal
                diagonal_distance += find_in_line(image, cordinate_list)
                # Add the founded white range to total diagonal distance
        if total_distance < diagonal_distance:  # Check if at the current
            # angle we found a range of white color that is greater
            # than previous angle
            total_distance = diagonal_distance  # Update the total distance
            #  to the greater white range founded
            choosen_angle = angle  # Update the choosen angle to
            # the dominate angle founded
    return choosen_angle


def black_image(length, width, angle):
    """A function that return a new image matrix according to original length
    and width that will rotate at a given angle"""
    blank_image = []  # create a new list that will get the new image matrix
    if angle < 90:  # If the given angle is lesser than 90 degrees
        angle = math.radians(angle)
        # Convert the given angle from degrees to radians
        blank_length = int(
            abs((width * math.sin(angle))) + abs(length * math.cos(angle)))
        # Calculate the new matrix length according to a given formula
        blank_width = int(
            abs((width * math.cos(angle))) + abs(length * math.sin(angle)))
        # Calculate the new matrix width according to a given formula
    elif angle > 90:  # If the given angle is greater than 90 degrees
        angle = math.radians(angle)
        # Convert the given angle from degrees to radians
        blank_length = int(
            abs((length * math.sin(angle))) + abs(width * math.cos(angle)))
        # Calculate the new matrix length according to a given formula
        blank_width = int(
            abs((length * math.cos(angle))) + abs(width * math.sin(angle)))
        # Calculate the new matrix width according to a given formula
    else:  # If the given angle is exactly 90 degrees
        blank_length = length  # The new length will be exactly as the original
        blank_width = width  # The new width will be exactly as the original
    return blank_image, blank_length, blank_width


def rotate(image, angle):
    """A function that get an image as a list of lists of numbers and a
    dominate image angle. Will return a rotated new image that will be aligned
    by the dominte angle of the original image"""
    origin_length = len(image)
    origin_width = len(image[0])
    blank_image, blank_length, blank_width = black_image(origin_length,
                                                         origin_width, angle)
    # Call a previous function to get new blanked image matrix and her extents
    rad_angle = math.radians(angle)
    # Convert the given angle from degrees to radians
    origin_center_point = [origin_length // 2, origin_width // 2]
    # Find the original image center point coordinates
    blank_center_point = [blank_length // 2, blank_width // 2]
    # Find the blanked new image center point coordinates
    for blank_row in range(blank_length):
        # Run along all the rows of the new blanked image
        one_row = []  # Define new list that will get the desirable
        # pixels from the original image matrix
        for blank_column in range(blank_width):
            # Run along all the columns of the new blanked image
            row = math.sin(rad_angle) * (
                blank_column - blank_center_point[0]) + math.cos(rad_angle) * (
                blank_row - blank_center_point[1])
            # Use the rotation formula from center point for rows
            column = math.cos(rad_angle) * (
                blank_column - blank_center_point[0]) - math.sin(rad_angle) * (
                blank_row - blank_center_point[1])
            # Use the rotation formula from center point for columns
            row = int(row + origin_center_point[0])
            # Add to the calculation of rows the original
            # center point coordinate
            column = int(column + origin_center_point[1])
            # Add to the calculation of columns the original
            # center point coordinate
            if (0 <= row < origin_length) and (0 <= column < origin_width):
                # If the current position is at the extent of
                # the original image matrix
                one_row.append(image[row][column])
                # Appending the value of pixel from the original image
            else:  # If the current position is not at the extent
                #  of the original image matrix
                one_row.append(BLACK)  # The new image matrix at current
                #  position gets black color value
        blank_image.append(one_row)  # Appending one build row to
        #  the new blank matrix
    return blank_image


def make_correction(image, max_diagonal):
    """A function that manage all the script by calling previous functions
    in a certein order to get the final product of rotated new image. Get
    an original image as a list of lists of numbers and max diagonal range"""
    mini_image = downsample(image, max_diagonal)
    # Downsample the original image by given max diagonal distance
    filtered_image = threshold_filter(mini_image)
    # Filter the downsampled image by founded threshold to get an B/W image
    edged_image = detect_edges(filtered_image)
    # Create edged image from the filtered image by founded edge value
    filtered_edged_image = threshold_filter(edged_image)
    # Filter the filtered edged image by founded threshold to get an B/W image
    dominate_angle = get_angle(filtered_edged_image)
    # Find the dominate angle of the filtered image
    new_image = rotate(image, dominate_angle)
    # Rotate the original image by the founded dominate angle
    # of her filtered image
    return new_image


def check_the_input():
    """A function that check the user input, will return ERROR messages by
    the appropriate case"""
    if len(sys.argv) < 4:
        # Check if all the inputs the script need is given by the user
        print('ERROR: wrong number of parameters. The correct usage is: '
              'ex6.py<image_file><output><max_diagonal>')
        return False
    elif not os.path.isfile(sys.argv[1]):
        # Check if the user image is proper file
        print('ERROR: image file not exist.')
        return False
    return True


def main():
    """A main function that manage the script, will call previous functions
    in appropriate order. Will return a new rotated image as the program
    final product"""
    if check_the_input():  # Call previous function to check the user inputs
        image = load_image(sys.argv[1])
        # The user input image is inserted to a new variable
        output_file = sys.argv[2]
        # The user wanted final output file is inserted to a new variable
        max_diagonal = float(sys.argv[3])
        # The user input max diagonal range is inserted to a new variable
        new_image = make_correction(image, max_diagonal)
        # Call previous function that manage all the processing
        # on the given image
        save(new_image, output_file)
        # Call function from the helper script that will save
        # an output file of the final product


if __name__ == '__main__':
    main()
