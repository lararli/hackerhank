"""
This code defines a function called superDigit that takes
two parameters, n and k. The function recursively calculates
the "super digit" of a given number by adding up its digits until
a single-digit number is obtained.

The function first defines a helper function called helper(n) that
takes a string n as input. This function converts each character in n
to an integer, adds them all up, and converts the result back to a string.
If the resulting string has only one character, it is returned as the output
of the function. Otherwise, the function recursively calls itself with the new
string as input.

Next, the function multiplies the output of helper(n) by k and converts the result
to a string. It then calls helper with this new string as input, returning the final super digit.

In summary, the superDigit function calculates the super digit of a number n by adding
up its digits and recursively applying this process until a single-digit number is obtained.
It then multiplies this result by k and repeats the process until a final super digit is obtained.
"""

def superDigit(n: str, k: int) -> str:
    """
    Calculates the super digit of n*k.

    Args:
        n (str): A string representing the number whose super digit is to be calculated.
        k (int): An integer specifying the number of times to repeat n before calculating the super digit.

    Returns:
        str: A string representing the super digit of n*k.
    """

    def helper(n: str) -> str:
        """
        Recursively calculates the digital root (super digit) of a number.

        Args:
            n (str): A string representing the number whose super digit is to be calculated.

        Returns:
            str: A string representing the super digit of n.
        """

        # Convert digits to integers and sum them
        total = 0
        for num in n:
            total += int(num)

        # Convert sum back to a string
        total = str(total)

        # If length of string is greater than 1, call helper again with the sum as argument
        if len(total) == 1:
            return total
        else:
            return helper(total)

    # Call helper function to calculate super digit of n, repeat k times, and store in p
    p = str(helper(n) * k)

    # Call helper function to calculate super digit of p and return result
    return helper(p)


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)
    print(result)