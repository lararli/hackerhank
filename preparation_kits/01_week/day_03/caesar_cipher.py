"""
This is a Python function that performs a Caesar Cipher
on a string passed as the first argument. A Caesar Cipher
is a simple encryption technique that shifts each character
in the plaintext by a fixed number of positions down the alphabet.

The function takes two arguments: a string to be encoded and
an integer representing the amount of shift to be applied to
each character.

The function first initializes an empty string to hold the result of the encoding.

It then iterates over each character in the input string,
checks if it is an alphabetic character, and then performs the
shift on it. If it is not an alphabetic character,
it is simply appended to the result string without being shifted.

The shift is performed by first determining whether the character
is uppercase or lowercase. This is done by using the isupper()
and islower() methods of the string object.

If the character is uppercase, it is shifted by subtracting the
ASCII value of 'A' and adding the shift amount to it.
The resulting value is then converted back to a character
using the chr() function.

If the character is lowercase, the same process is followed,
but using the ASCII value of 'a' instead of 'A'.

The shift amount is then taken modulo 26 to ensure that
the shift "wraps around" the alphabet.

Finally, the shifted character is appended to the result string.

The resulting encoded string is then returned.
"""


def caesar_cipher(string_value: str, shift_amount: int) -> str:
    """
    This function takes a string s and an integer
    shift_amount as input, and returns the Caesar cipher
    encrypted string of s using shift_amount.
    A Caesar cipher is a simple encryption technique where
    each letter in the original string is replaced with
    another letter that is a fixed number of positions
    down the alphabet.

    Args:
    st (str): A string to be encrypted
    shift_amount (int): The number of positions by which each
    letter in the original string should be shifted in the alphabet
    to produce the encrypted string.

    Returns:
    str: The encrypted string of s using shift_amount.

    Example:
    >>> caesar_cipher('abc',1)
    'bcd'
    >>> caesar_cipher('XYZ',3)
    'ABC'
    """
    res = ""

    for char in string_value:
        if char.isalpha():
            if char.isupper():
                shifted_char = chr(ord('A') + (ord(char) - ord('A') + shift_amount) % 26)
            else:
                shifted_char = chr(ord('a') + (ord(char) - ord('a') + shift_amount) % 26)
            res += shifted_char
        else:
            res += char

    return res
