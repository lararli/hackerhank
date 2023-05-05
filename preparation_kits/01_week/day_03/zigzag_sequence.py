"""
The code defines a function called findZigZagSequence
that takes in an array of integers a and its length n.
The function rearranges the elements of the input array
in a zigzag sequence and prints it out.

First, the function sorts the input array,
It then computes the index of the middle element and
swaps it with the last element of the array.

Next, the function initializes two variables st and ed
to point to the next and second-to-last elements of the array,
respectively. The function then swaps elements at these two positions,
incrementing st and decrementing ed in each iteration, until st becomes
greater than ed.

Finally, the function prints out the rearranged array in a zigzag
sequence by iterating through it and printing each element followed
by a space, except for the last element which is printed without the space.

The code also includes a test loop that reads in the number of test cases,
the length of each input array, and the elements of each input array.
For each test case, it calls the findZigZagSequence function with the
input array and its length as arguments.
"""


def find_zigzag_sequence(list_value: list) -> list:
    """
    Sorts the input list in a zigzag sequence and prints it.

    Args:
        list_value (list): The input list to be sorted.
        len_list (int): The length of the input list.

    Returns:
        None: This function does not return any value.

    Notes:
        - The zigzag sequence is obtained by swapping the middle element with the last element,
          and then alternatingly swapping the rightmost and leftmost
          elements of the remaining elements.
    """
    len_list = len(list_value)
    list_value.sort()

    # The middle element of a sorted list is swapped with the last element.
    mid = (len_list - 1) // 2
    list_value[mid], list_value[len_list - 1] = list_value[len_list - 1], list_value[mid]

    # The rightmost and leftmost elements of the remaining elements are swapped alternatingly.
    start, end = mid + 1, len_list - 2
    while start <= end:
        list_value[start], list_value[end] = list_value[end], list_value[start]
        start += 1
        end -= 1

    # The sorted list in zigzag sequence is printed.
    return list_value
