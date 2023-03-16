"""
Find median given an odd length list
"""


def find_median(arr: list) -> int:
    """
    Return the median of a list of odd length
    :param arr:
    :return:
    """
    arr.sort()
    index = int(len(arr) / 2)
    return arr[index]


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n: int = int(input().strip())
    array: list = list(map(int, input().rstrip().split()))
    result = find_median(array)
    print(result)

    # fptr.write(str(result) + '\n')
    # fptr.close()
