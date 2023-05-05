import pytest
from caesar_cipher import caesar_cipher
from palindrome_index import palindrome_index, is_palindrome
from tower_breakers import tower_breakers
from zigzag_sequence import find_zigzag_sequence


class TestCaesarCipher:

    def test_inputs(self):
        assert caesar_cipher('abc', 1) == 'bcd'
        assert caesar_cipher('XYZ', 3) == 'ABC'
        assert caesar_cipher('hello world', 5) == 'mjqqt btwqi'

    def test_empty_string(self):
        assert caesar_cipher('', 3) == ''

    def test_special_characters(self):
        assert caesar_cipher('Hello World!', 5) == 'Mjqqt Btwqi!'

    def test_wrong_inputs(self):
        with pytest.raises(TypeError):
            caesar_cipher(123, 1)

        with pytest.raises(TypeError):
            caesar_cipher('Hello!', '2')


class TestPalindromeIndex:

    def test_palindrome_word(self):
        assert is_palindrome('racecar') == True

    def test_empty_string(self):
        assert is_palindrome('') == True

    def test_non_palindrome_word(self):
        assert is_palindrome('hello') == False

    def test_single_char_str(self):
        assert is_palindrome('a') == True

    def test_with_white_space(self):
        assert is_palindrome('     ') == True

    def test_mixed_char(self):
        assert is_palindrome('MaDam') == False

    def test_non_alphanumeric(self):
        assert is_palindrome('A man, a plan, a canal, Panama!') == False

    def test_palindrome_index(self):
        """
        Test palindrome_index function with a palindrome string
        :return: None
        """
        assert palindrome_index('racecar')  == -1

    def test_remove_single_char(self):
        """
        Test with a string that needs a single character to be removed to become a palindrome.
        :return: None
        """
        assert palindrome_index('abca') == 1

    def test_multiple_char_to_remove(self):
        """
        Test with a string that needs multiple characters to be removed to become a palindrome.
        :return: None
        """
        assert palindrome_index('abcd') == -1

    def test_empty_string_index(self):
        """
        Test with a empty string.
        :return: None
        """
        assert palindrome_index('') == -1

    def test_palindrome_right_removal_index(self):
        assert palindrome_index('racecarz') == 7
        assert palindrome_index('abcdedcba') == -1


class TestTowerBreakers:

    def test_num_tower_1(self):
        # only 1 tower, player 1 should always win
        assert tower_breakers(1, 2) == 1
        assert tower_breakers(1, 3) == 1
        assert tower_breakers(1, 57) == 1

    def test_height_tower_1(self):
        # towers of height 1, player 2 should always win
        assert tower_breakers(2, 1) == 2
        assert tower_breakers(5, 1) == 2
        assert tower_breakers(15, 1) == 2

    def test_even_num_towers(self):
        # even number of towers, player 1 should always lose
        assert tower_breakers(4, 2) == 2

    def test_odd_num_towers(self):
        # odd number of towers, player 2 should always lose
        assert tower_breakers(3, 2) == 1



class TestZigZagSequence:

    def test_even_length(self):
        assert find_zigzag_sequence([8, 2, 4, 1, 6, 3]) == [1, 2, 8, 6, 4, 3]

    def test_odd_length(self):
        assert find_zigzag_sequence([1, 2, 3, 4, 5]) == [1, 2, 5, 4, 3]

    def test_two_elements(self):
        assert find_zigzag_sequence([3, 7]) == [7, 3]

    def test_one_element(self):
        assert find_zigzag_sequence([5]) == [5]

    def test_empty_input(self):
        with pytest.raises(IndexError):
            find_zigzag_sequence([])
