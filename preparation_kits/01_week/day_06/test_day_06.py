import pytest
from breadth_first_search import bfs
from jesse_and_cookies import cookies
from lego_blocks import lego_blocks
from simple_text_editor import simulate_operations


class TestBFS:

    def test_bfs(self):
        # Test case 1
        num_nodes = 4
        num_edges = 2
        edges = [(1, 2), (1, 3)]
        starting_node = 1
        expected_output = [0, 6, 6, -1]
        assert bfs(num_nodes, num_edges, edges, starting_node) == expected_output

        # Test case 2
        num_nodes = 5
        num_edges = 4
        edges = [(1, 2), (1, 3), (2, 4), (2, 5)]
        starting_node = 2
        expected_output = [6, 0, 12, 6, 6]
        assert bfs(num_nodes, num_edges, edges, starting_node) == expected_output

        # Test case 3
        num_nodes = 3
        num_edges = 1
        edges = [(1, 2)]
        starting_node = 3
        expected_output = [-1, -1, 0]
        assert bfs(num_nodes, num_edges, edges, starting_node) == expected_output

class TestJesseandCookies:

    def test_cookies(self):
        # Test case 1
        minimum_req = 7
        array_int = [1, 2, 3, 9, 10, 12]
        expected_output = -1
        assert cookies(minimum_req, array_int) == expected_output

        # Test case 2
        minimum_req = 10
        array_int = [2, 4, 6, 8]
        expected_output = -1
        assert cookies(minimum_req, array_int) == expected_output

        # Test case 3
        minimum_req = 3
        array_int = [1, 1, 1, 2, 2, 2, 3, 3, 3]
        expected_output = -1
        assert cookies(minimum_req, array_int) == expected_output

        # Test case 4
        minimum_req = 5
        array_int = [5]
        expected_output = 0
        assert cookies(minimum_req, array_int) == expected_output

        # Test case 5
        minimum_req = 78
        array_int = [1, 2, 3, 4, 5, 6, 7, 8]
        expected_output = -1
        assert cookies(minimum_req, array_int) == expected_output

class TestLegoBlocks:

    def test_minimum_wall_size(self):
        assert lego_blocks(1, 1) == 1

    def test_wall_with_equal_wh(self):
        assert lego_blocks(2, 2) == 3

    def wall_with_diff_wh(self):
        assert lego_blocks(3, 4) == 9


class TestSimpleTextEditor:

    def test_simulate_operations(self):
        # Test Case 1
        input_str = "4\n1 abc\n3 3\n2 2\n4\n"
        expected_output = ['c']
        assert simulate_operations(input_str) == expected_output

        # Test Case 2
        input_str = "3\n1 programming\n2 6\n3 2\n"
        expected_output = ['r']
        assert simulate_operations(input_str) == expected_output

        # Test Case 3
        input_str = "2\n1 python\n4\n"
        expected_output = []
        assert simulate_operations(input_str) == expected_output
