def gridChallenge(grid):
    """
    Determines if it's possible to rearrange the characters in a grid such that
    each row and column is in non-decreasing order.

    Args:
    - grid (list of str): a square grid of characters, each cell containing either an uppercase letter or a blank space.

    Returns:
    - "YES" if it's possible to rearrange the grid in this way, and "NO" otherwise.
    """

    # Convert the grid of strings to a 2D list of characters
    grid = [list(row) for row in grid]

    # Sort each row in non-decreasing order
    for row in grid:
        row.sort()

    # Check if each column is in non-decreasing order
    for j in range(len(grid[0])):
        for i in range(1, len(grid)):
            if grid[i][j] < grid[i - 1][j]:
                return "NO"

    return "YES"


if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)