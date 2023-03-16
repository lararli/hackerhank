"""
Find the unique element in an array of integers.
"""

def lonely_integer(arr: list) -> object:
    """
    Given an array of integers, where all elements but one occur twice, find the unique element.
    :param arr: an array of integers
    :return: the element that occurs only once
    """
    for value in arr:
        if arr.count(value) == 1:
            return value
        return None

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonely_integer(a)
    print(result)
