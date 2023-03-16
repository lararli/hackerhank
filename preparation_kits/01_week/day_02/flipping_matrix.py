"""
Reverse any of a matrix rows and columns any number of times.
The goal is to maximixe the sum of elements in the n x n submatrix located
in the upper-left quadrant of the matrix.
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
            # goin to every single interation and checking which one of the
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
