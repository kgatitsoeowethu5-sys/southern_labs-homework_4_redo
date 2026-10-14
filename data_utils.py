#Author: OWETHU


def calculate_average(val_1, val_2, val_3, val_4,val_5):
    """
    A utility module providing general purpose helper functions for mathematical
    computations and data formatting

    :param: a list of floats or ints avaraged
    :return: average calculated number in the list returns as 0.0 if list empty
    """

    total = (val_1 + val_2 + val_3 + val_4 + val_5)/ 5

    return total



def format_currency(amount):

    """
    formats a numerical amount into a currency string format

    :param: amount(int/float): the financial value to format
    :return: str: formatted currency string (e.g., R150.50)
    """

    return "R" + str(round(amount,2))
# southern_labs-homework_4_redo main_app.py
