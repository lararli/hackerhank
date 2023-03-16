"""
Return the number of times each value appears as an array of integers
"""

def counting_sort(arr):
    """
    Given a list of integers, count and return the number of times each value
    appears as an array of integers.
    :param arr:
    :return:
    """
    count = [0] * 100

    for num in arr:
        # add the count of the number in the index.
        # example: if the num in array is 63, it's going to add 1 in arr[63]
        count[num] += 1

    res = [str(v) for v in count]

    return ' '.join(res)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    counting_sort(a)

    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')
    #
    # fptr.close()
