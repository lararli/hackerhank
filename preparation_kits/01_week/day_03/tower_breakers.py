"""
This code determines which player wins the game of
Tower Breakers, given the number of towers and their height.
The game involves two players and a number of towers with
various heights. On each turn, a player chooses a tower and
removes any number of blocks from it. The player who removes
the last block from a tower wins the game.

The function tower_breakers takes in two arguments:

num_towers: an integer representing the number of towers in the game.
tower_height: an integer representing the height of the towers in the game.
The function returns an integer, either 1 or 2, depending
on which player wins the game.

The function includes the following notes:

If the number of towers is 1, player 1 always wins.
If the height of the towers is 1, player 2 always wins.
If the number of towers is even, player 1 always loses.
If the number of towers is odd, player 2 always loses.
The code checks if the height of the towers is equal to 1 or if the
number of towers is even. If either of these conditions is true,
player 2 wins (represented by returning 2). Otherwise,
player 1 wins (represented by returning 1).
"""


def tower_breakers(num_towers: int, tower_height: int) -> int:
    """
    Determines which player wins the game of Tower Breakers.

    The game involves two players and a number of towers with various heights.
    On each turn, a player chooses a tower and removes any number of blocks from it.
    The player who removes the last block from a tower wins the game.

    Args:
        num_towers (int): The number of towers in the game.
        tower_height (int): The height of the towers in the game.

    Returns:
        int: 1 if player 1 wins, 2 if player 2 wins.

    Notes:
        - If the number of towers is 1, player 1 always wins.
        - If the height of the towers is 1, player 2 always wins.
        - If the number of towers is even, player 1 always loses.
        - If the number of towers is odd, player 2 always loses.
    """

    if tower_height == 1 or num_towers % 2 == 0:
        return 2
    return 1
