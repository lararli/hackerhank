"""
This code defines a function called plus_minus that takes
a list of integers arr and prints the ratios of its positive,
negative, and zero elements, with 6 decimal places.

First, the function initializes three variables count_pos,
count_neg, and count_zero to 0. Then, it iterates over each
element of the input list arr and increments the corresponding
count variable based on the value of the element: if the element is zero,
count_zero is incremented, if it's positive, count_pos is incremented,
and if it's negative, count_neg is incremented.

After counting the number of positive, negative, and zero elements
in the input list, the function calculates the ratio of each type
of element using list comprehension, stores them in a list called
ratios, and then prints each value of the list with 6 decimal places
using a formatted string.

In the main block, the code reads the size of the array n from input
and reads the elements of the array from input as well using map
and list functions. Then, it calls the plus_minus function with
the input array as an argument.
"""


def plus_minus(arr: list) -> list:
    """
    Given an array of integers, calculate the ratios of its elements
    that are positive, negative, and zero.
    Print the decimal value of each fraction on a new line with 6 places after the decimal.
    :param arr: list of integers
    :return: None
    """
    count_pos, count_neg, count_zero = 0, 0, 0
    for num in arr:
        if num == 0:
            count_zero += 1
        elif num > 0:
            count_pos += 1
        else:
            count_neg += 1

    ratios = [count_pos, count_neg, count_zero]
    result = []
    n = len(arr)
    for value in ratios:
        result.append(f'{value/n:.6f}')

    return result

if __name__ == '__main__':
    # size of array
    n = int(input().strip())

    # array
    array = list(map(int, input().rstrip().split()))

    plus_minus(array)
