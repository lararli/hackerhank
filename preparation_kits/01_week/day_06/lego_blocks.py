"""
The code solves the "Lego Blocks" challenge from HackerRank,
which asks to calculate the number of ways to build a wall
with Lego blocks. The wall can have a variable height and width,
and the blocks come in four different sizes. However, there is a
constraint: no two vertical adjacent blocks can have the same length.

The code has three main steps:

Step 1: Compute the number of combinations to build a single row of
blocks of varying widths (up to the maximum width of the wall).
As there are only four kinds of block sizes, this step is relatively
straightforward. The base cases are predefined, and the code uses a loop
to compute the rest of the combinations, based on the previous four combinations.

Step 2: Compute the total number of combinations to build a wall of
varying height and width. This step uses the combinations computed in step 1,
raised to the power of the wall height (the exponentiation is done using the pow()
function). The result is stored in a list called "total."

Step 3: Compute the number of unstable wall configurations, i.e., walls that
violate the constraint of having no two vertical adjacent blocks of the same size.
This is done by dividing the wall into two parts (left and right), and computing the
number of combinations that have a vertical violation at the border between the two parts.
This is done for every possible width of the wall, using a loop that goes from 2 to the
maximum width.
The results are stored in a list called "unstable."

Finally, the code returns the number of stable wall combinations, i.e.,
the difference between the total number of wall combinations and the number
of unstable wall configurations. The result is taken modulo 10^9+7
to avoid integer overflow.
"""
import os



def lego_blocks(wall_height: int, wall_width: int) -> int:
    """
    Computes the number of ways to build a stable wall of size n x m using lego blocks.

    Args:
        wall_height (int): The height of the wall.
        wall_width (int): The width of the wall.

    Returns:
    int: The number of stable wall combinations modulo 10^9 + 7.
    """

    # Define modulo constant
    mod = 10 ** 9 + 7

    # Step 1: Calculate combinations to build a single row
    # Initialize base case values for width = 0, 1, 2, and 3
    row_combinations = [1, 1, 2, 4]

    # Build row combinations up to the given wall width
    while len(row_combinations) <= wall_width:
        # Add the sum of the previous 4 row combinations mod MOD
        row_combinations.append(sum(row_combinations[-4:]) % mod)

    # Step 2: Calculate total combinations for wall of height n
    # Compute the number of ways to build the entire wall by
    # taking the n-th power of each row combination modulo MOD
    total = [pow(c, wall_height, mod) for c in row_combinations]

    # Step 3: Find the number of unstable wall configurations
    # For each width from 2 to m, calculate the number of unstable wall configurations
    unstable = [0, 0]  # initialize base case values

    # Iterate over each possible width i of the wall
    for i in range(2, wall_width + 1):
        # For each possible left wall width j, calculate the combination of the left and right walls
        # calculate the left and right wall combinations
        wall_combinations = lambda j: (total[j] - unstable[j]) * total[i - j]  # pylint: disable=unnecessary-lambda-assignment,cell-var-from-loop
        # sum the combinations of each possible left wall width
        result = sum(map(wall_combinations, range(1, i)))
        unstable.append(result % mod)  # add the unstable configuration to the list

    # Return the number of stable wall combinations
    return (total[wall_width] - unstable[wall_width]) % mod


if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w', encoding='utf-8') as f:
        t = int(input().strip())

        for t_itr in range(t):
            first_multiple_input = input().rstrip().split()

            n = int(first_multiple_input[0])

            m = int(first_multiple_input[1])

            res = lego_blocks(n, m)

            f.write(str(res) + '\n')
