#############################################################
# FILE : temperature.py
# WRITER : Liron Gershuny , gerliron18 , 308350503
# EXERCISE : intro2cs ex2 2017-2018
# DESCRIPTION: A program that define a function that gets
# four parameters: the min temperature the user want
# and 3 day's temperature measurements then return boolean
# True or False as if at least two of the measurements
# were higher then the min temperature without printing it.
#############################################################

def is_it_summer_yet(temp_min, day_one, day_two, day_three):
    """This function gets four parameters: the min temperature
    the user want and 3 day's temperature measurements, then
    the function check if at least two of the measurements
    were higher then the min temperature and finally return
    boolean True or False"""
    if (temp_min < day_one):
        if (temp_min < day_two):
            return True
        elif (temp_min < day_three):
            return True
        else:
            return False
    elif (temp_min < day_two):
        if (temp_min < day_three):
            return True
        else:
            return False
    else:
        return False
