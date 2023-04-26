"""
This code defines a function find_median that
takes a list of odd length integers as an argument and returns
the median value of the input list.

The function first sorts the input list in
ascending order using the sort() method.
Then, it calculates the index of the median element in the sorted list
by dividing the length of the list by 2 and rounding down to an integer using the int() function.

Finally, it returns the median element by
indexing the sorted list with the calculated
index using square brackets.
"""


def find_median(arr: list) -> int:
    """
    Return the median of a list of odd length.

    Args:
        arr (list): A list of odd length integers.

    Returns:
        int: The median value of the input list.

    Example:
        >>> find_median([3, 5, 1, 7, 9])
        5

    """
    # Sort the input list in ascending order.

    if len(arr) % 2 == 0 or len(arr) == 0:
        raise ValueError('Input list must have an odd length.')
    arr.sort()

    # Calculate the index of the median element in the sorted list.
    index = int(len(arr) / 2)

    # Return the median element.
    return arr[index]


if __name__ == '__main__':
    n: int = int(input().strip())
    array: list = list(map(int, input().rstrip().split()))
    result = find_median(array)
    print(result)
