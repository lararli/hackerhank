"""
The New Year Chaos challenge in Hackerrank is a problem that simulates a
queue of people waiting in line to enter a party. Each person is assigned
a unique number, and initially, the queue is ordered based on these numbers.
However, some people may have bribed others to get ahead in line, causing chaos.
The goal of the problem is to determine the minimum number of bribes that took place
to reach the current order of the queue or to indicate if it is not possible to
determine the number of bribes.

The input to the function minimumBribes(q) is an array q of integers, where each q[i]
represents the original position of the person with number i+1 in the queue.
The function iterates through the queue from the end to the beginning and checks
if a person has moved more than two positions forward in the queue. If a person
has moved more than two positions forward, it means that they bribed others to get ahead.
If a person has moved one position forward, it means that they bribed the person in front of them.
The function counts the number of bribes and updates the queue accordingly. If a person has moved
more than two positions forward, the function returns 'Too chaotic'.
"""


def minimum_bribes(array_int):
    """
    Takes an array q representing the original order of people in a queue and
    returns the minimum number of bribes that took place to reach the current order of the queue
    or indicates if it is not possible to determine the number of bribes.

    Args:
    q (List[int]): An array of integers representing the original order of people in the queue.

    Returns:
    None if the queue is too chaotic, otherwise the minimum number of bribes as an integer.

    """
    bribe: int = 0  # initialize bribe count to 0
    for i in range(len(array_int) - 1, 0, -1):  # iterate over the queue from end to beginning
        if array_int[i] != i + 1:  # check if current person is in their original position
            if array_int[i - 1] == i + 1:  # check if current person has moved one position forward
                bribe += 1  # increase bribe count by 1
                #  swap the positions of the two people
                array_int[i - 1], array_int[i] = array_int[i], array_int[i - 1]
            # check if current person has moved two positions forward
            elif array_int[i - 2] == i + 1:
                bribe += 2  # increase bribe count by 2
                #  swap the positions of the three people
                array_int[i - 2], array_int[i - 1], array_int[i] = array_int[i - 1], array_int[i], array_int[i - 2]  # pylint: disable=C0301
            else:
                # if the current person has moved more than two positions forward, it is too chaotic
                return 'Too chaotic'
    return bribe  # print the number of bribes
