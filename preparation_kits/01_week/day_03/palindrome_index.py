"""
This code defines two functions. The first function
is_palindrome checks whether a given word is a palindrome or not.
It takes a single string argument word and returns
True if the word is a palindrome, and False otherwise.
To determine whether the string is a palindrome,
the function compares the input string with its reverse
version obtained by slicing the string in reverse order using
the syntax word[::-1]. If the input string is equal to its reverse,
it is a palindrome and the function returns True.

The second function palindrome_index search the index of the character
that can be removed from the input string to make it a palindrome.
It takes a single string argument s and returns an integer value
representing the index of the character that can be removed.
If the string is already a palindrome, the function returns -1.
If there are multiple characters that can be removed to make the
string a palindrome, the function returns the index of the leftmost
character that can be removed.

The function first checks whether the input string is already a
palindrome by calling the is_palindrome function. If the input string is
a palindrome, the function returns -1 without further processing.

If the input string is not a palindrome, the function iterates through
the first half of the string and checks if the corresponding character
from the second half of the string is different. If the characters are different,
it removes the left and right characters one by one, and checks if the resulting
strings are palindromes by calling the is_palindrome function. If a palindrome
is found, the function returns the index of the leftmost character that was removed.

Finally, if no character is found that can be removed to make the string
a palindrome, the function returns -1.
"""


def is_palindrome(word):
    """
    Determines if a given word is a palindrome.

    Args:
        word (str): The word to be checked.

    Returns:
        bool: True if the word is a palindrome, False otherwise.
    """
    return word == word[::-1]


def palindrome_index(string_value: str):
    """
    Finds the index of the character that can be removed to make the input string a palindrome.

    Args:
        string_value (str): The input string.

    Returns:
        int: The index of the character that can be removed,
        or -1 if the string is already a palindrome.

    Notes:
        - If there are multiple characters that can be
        removed to make the string a palindrome, the function
          returns the index of the leftmost character.
    """
    if is_palindrome(string_value):
        return -1

    len_str = len(string_value)
    for i in range(len_str // 2):
        if string_value[i] != string_value[len_str - 1 - i]:
            new_s_left = string_value[:i] + string_value[i + 1:]
            new_s_right = string_value[:len_str - 1 - i] + string_value[len_str - i:]
            if is_palindrome(new_s_left):
                return i
            if is_palindrome(new_s_right):
                return len_str - i - 1

    return -1


if __name__ == '__main__':
    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        result = palindrome_index(s)
