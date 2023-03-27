"""
The code defines a function called counting_sort
that takes a list of integers as an argument and
returns a string with space-separated counts representing
the number of times each value appears in the input array.
The function first creates a list called count with 100 elements
set to 0. It then iterates through each element in the input
array and increments the count of the corresponding index in the
count list. After counting the occurrences of each value, the
function converts the elements of the count list to strings and
stores them in a new list called res. Finally, the function joins
the elements of the res list with a space separator and returns the
resulting string.

The code then checks if the script is being run as the main program,
and if so, it prompts the user to input the length of the list of
integers and the integers themselves. It converts the input integers
to a list of integers and passes it as an argument to the counting_sort function.
"""


def counting_sort(arr):
    """
    Given a list of integers, count and return the number of times each value
    appears as an array of integers.

    Args:
        arr (list): A list of integers.

    Returns:
        str: A space-separated string of counts, where each count represents the
        number of times a particular value appears in the input array.

    Example:
        >>> counting_sort([3, 2, 1, 2, 3, 1, 1, 5, 5, 5])
        '3 2 3 0 0 3 0 ... 0'

    """
    # Create a list of size 100 with all elements set to 0.
    count = [0] * 100

    # Iterate through each element in the input array and increment the count of
    # the corresponding index in the count list.
    for num in arr:
        count[num] += 1

    # Convert the elements of the count list to strings and store them in the res list.
    res = [str(v) for v in count]

    # Join the elements of the res list with a space separator and return the resulting string.
    return ' '.join(res)


if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    print(counting_sort(a))
