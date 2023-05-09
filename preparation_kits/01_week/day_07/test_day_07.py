import pytest
from no_prefix_set import execute_process
from tree_huffman_decoding import execute_decodeHuff
from tree_preorder_traversal import execute_pre_order_traversal


class TestNoPrefixSet:

    def test_empty_list(self, capfd):
        words_tree = []
        execute_process(words_tree)
        captured = capfd.readouterr()
        assert captured.out == 'GOOD SET\n'

    def test_list_with_no_prefix_matches(self, capfd):
        words_tree = ['apple', 'banana', 'cherry', 'date']
        execute_process(words_tree)
        captured = capfd.readouterr()
        assert captured.out == 'GOOD SET\n'

    def test_list_with_prefix_match(self, capfd):
        words_tree = ['apple', 'app', 'banana', 'cherry', 'date']
        execute_process(words_tree)
        captured = capfd.readouterr()
        assert captured.out ==  'BAD SET\napple\n'

    def test_with_multiple_prefix_matches(self, capfd):
        words_tree = ['apple', 'app', 'banana', 'cherry', 'date']
        execute_process(words_tree)
        captured = capfd.readouterr()
        assert captured.out ==  'BAD SET\napple\n'

    def test_list_with_duplicates(self, capfd):
        words_tree = ['apple', 'banana', 'cherry', 'date', 'banana']
        execute_process(words_tree)
        captured = capfd.readouterr()
        assert captured.out == 'BAD SET\napple\n'

    def test_list_with_empty_subtree(self, capfd):
        words_tree = ['apple']
        execute_process(words_tree)
        captured = capfd.readouterr()
        assert captured.out == 'BAD SET\napple\n'

class TestTreeHuffmanDecoding:

    def test_execute_decodeHuff_single_character(self):
        ip = '0101010101'
        decoded_str = execute_decodeHuff(ip)
        assert decoded_str == '0101010101'

    def test_execute_decodeHuff_unique_characters(self):
        ip = 'abcde'
        decoded_str = execute_decodeHuff(ip)
        assert decoded_str == 'abcde'

    def test_execute_decodeHuff_repeating_characters(self):
        ip = 'aaabbbcccdddeee'
        decoded_str = execute_decodeHuff(ip)
        assert decoded_str == 'aaabbbcccdddeee'

    def test_execute_decodeHuff_mixed_characters(self):
        ip = 'abcdeabcdeabcde'
        decoded_str = execute_decodeHuff(ip)
        assert decoded_str == 'abcdeabcdeabcde'

class TestTreePreorderTraversal:

    def test_empty_input(self):
        arr = []
        result = execute_pre_order_traversal(arr)
        assert result == ''

    def test_single_element(self):
        arr = [5]
        result = execute_pre_order_traversal(arr)
        assert result == '5 '

    def test_multiple_elements_in_sorted_order(self):
        arr = [1, 2, 3, 4, 5]
        result = execute_pre_order_traversal(arr)
        assert result == '5 1 2 3 4 '

    def test_multiple_elements_in_reverse_order(self):
        arr = [5, 4, 3, 2, 1]
        result = execute_pre_order_traversal(arr)
        assert result == '5 1 2 3 4 '



