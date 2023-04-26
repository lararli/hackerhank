"""
Given a list, repeat each element in the list (n)
amount of times. The input and output portions will be handled
automatically by the grader. You need to write a function with the
recommended method signature.

Input Format

The first line contains the integer (S) where (S) is the number
of times you need to repeat the elements.
The next  lines each contain an integer. These are the (X)
elements in the array.

Output Format

Output each element of the original list (S) times, each on a
separate line. You have to return the list/vector/array of (S * X) integers.
The relative positions of the values should be the same as the original
list provided in the input.
"""


def replicate_list(num: int, arr: list[int]) -> None:
    """
    Replicates each value in a list a specified number of times and prints the replicated values.

    Args:
    - num (int): The number of times to replicate each value in the list
    - arr (list[int]): The list of integers to replicate

    Returns:
    None

    Example Usage:
    >>> replicate_list(2, [1, 2])
    1
    1
    2
    2
    """
    if not isinstance(arr, list) or not isinstance(num, int):
        raise TypeError('Num should be an integer and arr should be a list')
    for value in arr:
        list_values = str(value) * num
        for num_str in list_values:
            print(num_str)


# replicate_list(2, [1, 2, 3, 4])