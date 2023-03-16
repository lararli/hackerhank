"""
Calculate the absolute difference between the sums of its diagonals given a square matrix
"""

def diagonal_diff(arr: list) -> object:
    """
    Given a square matrix, calculate the absolute difference between the sums of its diagonals.
    :rtype: object
    :param arr: an array of integers
    :return:
    """
    left_to_right = []
    right_to_left = []
    for column in range(0, n):
        for row in range(0, n):
            print(f'row: {row}, column: {column}')
            if column == row:
                print('column is equal to row, so im going to add into left_to_right diagonal')
                left_to_right.append(arr[column][row])
            if column == (n - row - 1):
                print(f'columns is equal the number of rows({n}) \n'
                      f'minus the index of the row({row}) minus 1, \n'
                      f'so im gonna to add to right_to_left diagonal')
                right_to_left.append(arr[column][row])
    print(sum(left_to_right), sum(right_to_left))
    return abs(sum(left_to_right) - sum(right_to_left))



    #     for _ in range(n):
    #         print('_', _)
    #     if arr.index(v) == 0:
    #         left_to_right.append(v[0])
    #         right_to_left.append(v[2])
    #     elif arr.index(v) == 1:
    #         left_to_right.append(v[1])
    #         right_to_left.append(v[1])
    #     elif arr.index(v) == 2:
    #         left_to_right.append(v[2])
    #         right_to_left.append(v[0])
    # print(left_to_right, right_to_left)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = []

    for _ in range(n):
        a.append(list(map(int, input().rstrip().split())))

    result: object = diagonal_diff(a)
    print(result)

    # fptr.write(str(result) + '\n')
    # fptr.close()
