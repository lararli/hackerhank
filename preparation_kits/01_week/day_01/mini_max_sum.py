"""
This code defines a function called mini_max_sum that takes a
list of 5 integers and finds the minimum and maximum values that
can be calculated by summing exactly four of the five integers.
The function doesn't return anything, but it prints the respective
minimum and maximum values as a single line of two space-separated long integers.

The function first sorts the input list in ascending order using the
sorted function and assigns the result to a new list called sorted_arr.

Next, it calculates the sum of the four smallest integers by slicing
the sorted list from the beginning up to the second-to-last element
using the [:-1] syntax and assigning the result to a variable called min_sum.
Similarly, it calculates the sum of the four largest integers by slicing the
sorted list from the second element to the end using the [1:] syntax and assigning
the result to a variable called max_sum.

Finally, it prints a tuple containing the minimum and maximum sums using the print function.
"""


def mini_max_sum(arr: list) -> None:
    """
    Given five positive integers, find the minimum and maximum values that can be calculated
    by summing exactly four of the five integers.
    Then print the respective minimum and maximum values as a single line of
    two space-separated long integers.

    Args:
        arr (list): A list of 5 integers.

    Returns:
        None: This function doesn't return anything, but it prints the respective minimum
        and maximum values that can be calculated by summing exactly four of the five integers.

    Example:
        >>> mini_max_sum([1, 2, 3, 4, 5])
        (10, 14)

    """
    # Sort the input list in ascending order.
    sorted_arr = sorted(arr)

    # Calculate the sum of the four smallest and four largest numbers.
    min_sum = sum(sorted_arr[:-1])
    max_sum = sum(sorted_arr[1:])

    # Print a tuple containing the minimum and maximum sums.
    print((min_sum, max_sum))

if __name__ == '__main__':
    array = list(map(int, input().rstrip().split()))
    print(mini_max_sum(array))
