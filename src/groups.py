"""
@file containing lists of 'connected' words and methods to get those lists
"""


import random


word_lists = (
    ("animals from Africa", "giraffe", "elephant", "lion", "mouse"),
    ("relationship or association between people, things, or ideas", "connection", "tie", "bond", "link"),
    ("verbs meaning to join", "connect", "attach", "link", "fasten"),
    ("group of people connected socially or professionally", "network", "circle", "clique", "cohort"),
    ("technical components involved in electrical, computer, or network systems", "circuit", "node", "port", "interface"),
    ("pathway through which something moves or is communicated", "channel", "line", "medium", "route"),
    ("logical or statistical relationships between variables or events", "correlation", "association", "linkage", "dependence"),
    ("items arranged or connected in order", "chain", "series", "string", "sequence"),
    ("informal terms for influence or the ability to get things done through connections", "leverage", "access", "reach", "pull")
)
"""
tuple of tuples containing the four connecting words. The first index contains the reason for each selection
"""

def get_groups(group = word_lists) -> tuple:
    """
    Gets 4 random groups from the passed list, defaulting to word_lists

    :param: tuple of objects to get 4 of

    :return: tuple of 4 items from passed list
    """
    return tuple(random.sample(group, 4))


