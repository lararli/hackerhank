"""
This code defines a function called lonely_integer
that takes an array of integers as input and returns
the element that occurs only once in the array.
The function iterates through each element in the input
array and checks if its count is equal to 1 using the count method.
If an element with a count of 1 is found, the function
returns that element.
If no such element is found, the function returns None.
"""
from typing import Union


def lonely_integer(arr: list) -> Union[int, None]:
    """
    Given an array of integers, where all elements but one occur twice, find the unique element.
    :param arr: an array of integers
    :return: the element that occurs only once
    """
    for value in arr:
        if arr.count(value) == 1:
            return value
    return None

