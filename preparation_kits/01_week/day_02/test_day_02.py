from counting_sort import counting_sort
from diagonal_difference import diagonal_diff
from flipping_matrix import flipping_matrix
from lonely_integer import lonely_integer
import pytest

class TestCountingSort:

    def test_counting_sort(self):
        array: list = [1, 2, 2, 4]
        assert counting_sort(array) == '0 1 2 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0'

    def test_with_index_over_than_20(self):
        array: list = [1, 2, 3, 4, 5, 6, 20]
        with pytest.raises(IndexError):
            counting_sort(array)

    def test_empty_array(self):
        array: list = []
        assert counting_sort(array) == '0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0'

class TestDiagonalDifference:

    def test_diagonal_difference(self):
        matrix: list = [[1, 2], [1, 2]]
        assert diagonal_diff(matrix) == 0

    def test_not_square(self):
        matrix: list = [[1], [1, 2]]
        with pytest.raises(IndexError):
            diagonal_diff(matrix)

    def test_with_negative_values(self):
        matrix: list = [[1, -67, 8], [1, 2, 4], [1, 3, 5]]
        assert diagonal_diff(matrix) == 3

    def test_with_not_int(self):
        matrix: list = [[1, 'n'], ['1', 2]]
        with pytest.raises(TypeError):
            diagonal_diff(matrix)

class TestFlippingMatrix:

    def test_flipping_matrix(self):
        matrix: list = [[5, 5], [5, 5]]
        assert flipping_matrix(matrix) == 5

    def test_flipping_matrix_not_square(self):
        matrix: list = [[1, 2, 3, 4], [2, 3, 4, 5], [1, 2, 3, 4]]
        assert flipping_matrix(matrix) == 3

    def test_invalid_input(self):
        matrix: list = [[1, 2], ['1', 2]]
        with pytest.raises(TypeError):
            flipping_matrix(matrix)

    def test_empty_list(self):
        matrix: list = []
        assert flipping_matrix(matrix) == 0

    def test_empty_sub_lists(self):
        matrix: list = [[], []]
        with pytest.raises(IndexError):
            flipping_matrix(matrix)

class TestLonelyInteger:

    def test_find_lonely_integer(self):
        array: list = [1, 2, 2, 3, 3]
        assert lonely_integer(array) == 1

    def test_find_more_than_one_lonely_integer(self):
        array: list = [1, 2, 3, 3, 4, 4]
        assert lonely_integer(array) == 1

    def test_empty_array(self):
        array: list = []
        assert lonely_integer(array) is None