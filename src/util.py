"""
@file utility functions for program
"""
import random
def sorted_dict(d: dict) -> dict:
    """
    Sorts and returns a dictionary
    :param d: is dict to sort
    :return: sorted version of d
    """
    keys = sorted(d.keys())
    new_dict = {key:d[key] for key in keys}
    return new_dict

def shuffle() -> tuple:
    """
    Shuffles the order of words in a 2d tuple

    :param t: tuple to shuffle
    :return: shuffled tuple
    """


