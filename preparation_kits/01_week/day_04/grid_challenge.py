"""
The function takes a single argument grid,
which is a list of strings representing a square grid of characters.
It returns "YES" if it's possible to rearrange the grid such that
each row and column is in non-decreasing order, and "NO" otherwise.

The function first converts the grid of strings to a 2D list of
characters using a list comprehension. Then it sorts each row in
non-decreasing order using a simple for loop with row.sort().
Finally, it checks each column by iterating over each column index j
using range(len(grid[0])), and then comparing the current element in
the current row with the previous element in the previous row using a
nested for loop with 'i' starting from 1. If a column is not in non-decreasing order,
the function immediately returns "NO". If all rows and columns are in non-decreasing order,
the function returns "YES".
"""


def grid_challenge(grid_value):
    """
    Determines if it's possible to rearrange the characters in a grid such that
    each row and column is in non-decreasing order.

    Args:
    - grid (list of str): a square grid of characters, each cell containing either
    an uppercase letter or a blank space.

    Returns:
    - "YES" if it's possible to rearrange the grid in this way, and "NO" otherwise.
    """

    # Convert the grid of strings to a 2D list of characters
    same_length = all(len(x) == len(grid_value[0]) for x in grid_value)
    if not same_length:
        raise ValueError('All elements in the list must have the same length')
    grid_value = [list(row) for row in grid_value]

    # Sort each row in non-decreasing order
    for row in grid_value:
        row.sort()

    # Check if each column is in non-decreasing order
    for j in range(len(grid_value[0])):
        for i in range(1, len(grid_value)):
            if grid_value[i][j] < grid_value[i - 1][j]:
                return "NO"

    return "YES"
