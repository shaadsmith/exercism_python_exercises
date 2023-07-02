# Task 1
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

#Task 2
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.
 
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.
 
    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time
    
#Task 3
def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation for given number of layers.
 
    :param number_of_layers: int - the number of layers used for preparation
    :return: int - the amount of time it takes to prepare given number of layers
 
    Function that takes the amount of layers to prepare and computes the amount of time it takes
    to prepare them.
    """
    return number_of_layers * PREPARATION_TIME

#Task 4
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total amount of time the lasagna is cooking.
 
    :param number_of_layers: int - the number of layers used for preparation
    :param elapsed_bake_time: int - how long the lasagna is cooking
    :return: int - the amount of time it takes to prepare given number of layers
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time