"""
The function diagonal_diff takes a square matrix (a list of lists) as an input,
and returns the absolute difference between the sums of its two diagonals.
The function first initializes two empty lists,
left_to_right and right_to_left, which will store the diagonal elements
from left-to-right and right-to-left, respectively.

Then, the function iterates through each element of the matrix using nested loops,
and checks if the current element belongs to either diagonal.
If the element is on the left-to-right diagonal (which corresponds to the indices
where the row and column numbers are equal), it is added to left_to_right.
If it is on the right-to-left diagonal
(which corresponds to the indices where the column number is equal to n - row - 1,
where n is the size of the matrix and row is the current row index),
it is added to right_to_left.

After both diagonals have been extracted,
the function returns the absolute difference between the sums of the two lists.
"""


def diagonal_diff(arr: list) -> float:
    """
    Given a square matrix, calculate the absolute difference between the sums of its diagonals.
    :rtype: object
    :param arr: an array of integers
    :return:
    """
    left_to_right = []
    right_to_left = []
    for column in range(0, len(arr)):
        for row in range(0, len(arr)):
            print(f'row: {row}, column: {column}')
            if column == row:
                print('column is equal to row, so im going to add into left_to_right diagonal')
                left_to_right.append(arr[column][row])
            if column == (len(arr) - row - 1):
                print(f'columns is equal the number of rows({len(arr)}) \n'
                      f'minus the index of the row({row}) minus 1, \n'
                      f'so im gonna to add to right_to_left diagonal')
                right_to_left.append(arr[column][row])
    print(sum(left_to_right), sum(right_to_left))
    return abs(sum(left_to_right) - sum(right_to_left))
