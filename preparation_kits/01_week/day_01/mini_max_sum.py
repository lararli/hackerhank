"""
Calculate the minimum and maximum values as a single line of
two space-separated long integers.
"""


def mini_max_sum(arr: list) -> None:
    """
    Given five positive integers, find the minimum and maximum values that can be calculated
    by summing exactly four of the five integers.
    Then print the respective minimum and maximum values as a single line of
    two space-separated long integers.
    :param arr: an array of 5 integers
    :return: Print two space-separated long integers denoting the respective minimum and maximum
    values that can be calculated by summing exactly four of the five integers.
    (The output can be greater than a 32 bit integer.)
    """
    list_max, list_min = arr.copy(), arr.copy()
    list_min.remove(max(arr))
    list_max.remove(min(arr))
    print(f'{sum(list_min)} {sum(list_max)}')


if __name__ == '__main__':
    array = list(map(int, input().rstrip().split()))
    print(mini_max_sum(array))
