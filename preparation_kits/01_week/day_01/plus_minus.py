"""
This challenge introduces precision problems.
https://www.naukri.com/learning/articles/precision-handling-in-python/
"""


def plus_minus(arr: list) -> None:
    """
    Given an array of integers, calculate the ratios of its elements
    that are positive, negative, and zero.
    Print the decimal value of each fraction on a new line with  places after the decimal
    :param arr:
    :return: n space-separated integers that describe arr[n]
    """
    count_pos, count_neg, count_zero = 0, 0, 0
    for num in arr:
        if num == 0:
            count_zero += 1
        elif num > 0:
            count_pos += 1
        else:
            count_neg += 1

    ratios = [count_pos, count_neg, count_zero]
    for value in ratios:
        print(f'{value/n:.6f}')


if __name__ == '__main__':
    # size of array
    n = int(input().strip())

    # array
    array = list(map(int, input().rstrip().split()))

    plus_minus(array)
