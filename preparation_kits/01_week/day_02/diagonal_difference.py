def diagonal_diff(arr: list) -> object:
    """
    Given a square matrix, calculate the absolute difference between the sums of its diagonals.
    :rtype: object
    :param arr: an array of integers
    :return:
    """
    left_to_right = []
    right_to_left = []
    for v in arr:
        if arr.index(v) == 0:
            left_to_right.append(v[0])
            right_to_left.append(v[2])
        elif arr.index(v) == 1:
            left_to_right.append(v[1])
            right_to_left.append(v[1])
        elif arr.index(v) == 2:
            left_to_right.append(v[2])
            right_to_left.append(v[0])
    print(left_to_right, right_to_left)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result: object = diagonal_diff(arr)
    print(result)

    # fptr.write(str(result) + '\n')
    # 
    # fptr.close()
