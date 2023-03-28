"""
The code defines a function called findZigZagSequence
that takes in an array of integers a and its length n.
The function rearranges the elements of the input array
in a zig-zag sequence and prints it out.

First, the function sorts the input array a.
It then computes the index of the middle element and
swaps it with the last element of the array.

Next, the function initializes two variables st and ed
to point to the next and second-to-last elements of the array,
respectively. The function then swaps elements at these two positions,
incrementing st and decrementing ed in each iteration, until st becomes
greater than ed.

Finally, the function prints out the rearranged array in a zig-zag
sequence by iterating through it and printing each element followed
by a space, except for the last element which is printed without the space.

The code also includes a test loop that reads in the number of test cases,
the length of each input array, and the elements of each input array.
For each test case, it calls the findZigZagSequence function with the
input array and its length as arguments.
"""
def find_zigzag_sequence(a: list, n: int) -> None:
    """
    Sorts the input list in a zigzag sequence and prints it.

    Args:
        a (list): The input list to be sorted.
        n (int): The length of the input list.

    Returns:
        None: This function does not return any value.

    Notes:
        - The zigzag sequence is obtained by swapping the middle element with the last element,
          and then alternatingly swapping the rightmost and leftmost
          elements of the remaining elements.
    """
    a.sort()

    # The middle element of a sorted list is swapped with the last element.
    mid = (n - 1) // 2
    a[mid], a[n - 1] = a[n - 1], a[mid]

    # The rightmost and leftmost elements of the remaining elements are swapped alternatingly.
    st, ed = mid + 1, n - 2
    while st <= ed:
        a[st], a[ed] = a[ed], a[st]
        st += 1
        ed -= 1

    # The sorted list in zigzag sequence is printed.
    print(*a)


if __name__ == '__main__':
    # The number of test cases is read from standard input.
    test_cases = int(input())

    for _ in range(test_cases):
        # The length and elements of the input list are read from standard input.
        n = int(input())
        a = list(map(int, input().split()))

        # The zigzag sequence of the input list is obtained and printed.
        find_zigzag_sequence(a, n)
