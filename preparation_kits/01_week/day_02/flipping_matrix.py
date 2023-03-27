"""
The flipping_matrix function receives a square matrix
as input and returns the sum of the elements in the
matrix's upper-left quadrant, after the rows and columns
of each matrix have been reversed in the best possible way.

The function iterates over the first half of the rows and
columns in the matrix, and for each element in the upper-left
quadrant, it finds the maximum value between the element, its
corresponding element on the same row but on the opposite side of the matrix,
its corresponding element on the same column but on the opposite side of the matrix,
and its corresponding element on the opposite row and column.
It then adds the maximum value to a running sum.

The function does not modify the original input matrix but only
computes and returns a value.
"""

def flipping_matrix(matrix):
    """
    Given the initial configurations for q matrices, reverse the rows
    and columns of each matrix in the best possible way so that the sum
    of the elements in the matrix's upper-left quadrant is maximal.
    :param matrix:
    :return:
    """
    n_mtx = len(matrix)
    sum_values = 0

    # getting the top left
    for i in range(n_mtx // 2):  # start at 0

        for j in range(n_mtx // 2):  # start at 0
            # going to every single interation and checking which one of the
            # mirror values is the biggest one.
            sum_values += max(
                matrix[i][j],
                matrix[i][n_mtx - j - 1],
                matrix[n_mtx - i - 1][j],
                matrix[n_mtx - i - 1][n_mtx - j - 1]
            )
    return sum_values

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        mtx = []

        for _ in range(2 * n):
            mtx.append(list(map(int, input().rstrip().split())))

        result = flipping_matrix(mtx)

    #     fptr.write(str(result) + '\n')
    #
    # fptr.close()
