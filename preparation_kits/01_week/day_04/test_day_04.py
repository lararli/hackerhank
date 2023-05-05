import pytest
from grid_challenge import grid_challenge
from new_year_chaos import minimum_bribes
from recursive_digit_sum import super_digit
from truck_tour import truck_tour


class TestGridChallenge:

    def test_grid(self):
        # Test with different inputs

        # Test case 01
        grid = ['ab', 'ba']
        assert grid_challenge(grid) == 'YES'

        # Test case 02
        grid = ['cba', 'fed', 'igh']
        assert grid_challenge(grid) == 'YES'

        # Test case 03
        grid = ['aa', 'bb']
        assert grid_challenge(grid) == 'YES'

        # Test case 04
        grid = ['ab', 'ba']
        assert grid_challenge(grid) == 'YES'

        # Test case 05
        grid = ['abcd', 'bcde', 'cdef', 'defg']
        assert grid_challenge(grid) == 'YES'

        grid = ['abc', 'def', 'ghi', 'hia']
        assert grid_challenge(grid) == 'NO'

    def test_with_different_length(self):
        grid = ['abcd', 'bcdef']
        with pytest.raises(ValueError):
            grid_challenge(grid)

    def test_with_integers(self):
        grid = [123, 543]
        with pytest.raises(TypeError):
            grid_challenge(grid)


class TestNewYearChaos:

    def test_normal_execution(self):
        # test case 01
        assert minimum_bribes([1, 2, 3, 4, 5]) == 0

        # test case 02
        assert minimum_bribes([1, 2, 3, 5, 4]) == 1

        # test case 03
        assert minimum_bribes([1, 2, 5, 3, 4]) == 2

    def test_too_chaotic_execution(self):
        # test case 01
        assert minimum_bribes([2, 5, 1, 3, 4]) == 'Too chaotic'

        # test case 02
        assert minimum_bribes([1, 2, 7, 3, 4, 5, 6]) == 'Too chaotic'

        # test case 03
        assert minimum_bribes([5, 4, 3, 2, 1]) == 'Too chaotic'

        # test case 04
        assert minimum_bribes([4, 1, 2, 3, 4]) == 'Too chaotic'

    def test_boundary_conditions(self):
        # single element list
        assert minimum_bribes([1]) == 0

        # list of 2 elements
        assert minimum_bribes([1, 2]) == 0

        # list of 3 elements with 1 bribe
        assert minimum_bribes([1, 3, 2]) == 1

        # list of 3 elements with too chaotic
        assert minimum_bribes([4, 1, 2, 3]) == 'Too chaotic'


class TestRecursiveDigitSum:

    def test_super_digit(self):
        assert super_digit('148', 3) == '3'
        assert super_digit('9875', 4) == '8'
        assert super_digit('123', 2) == '3'

    def test_wrong_inputs(self):
        with pytest.raises(TypeError):
            super_digit(148, 3)
        with pytest.raises(TypeError):
            super_digit(148, '3')


class TestTruckTour:

    def test_truck_tour(self):
        petrol_pumps = [(4, 6), (6, 5), (7, 3), (4, 5)]
        assert truck_tour(petrol_pumps) == 1

        petrol_pumps = [(6, 5), (7, 3), (4, 5), (4, 6)]
        assert truck_tour(petrol_pumps) == 0

        petrol_pumps = [(7, 3), (4, 5), (4, 6), (6, 5)]
        assert truck_tour(petrol_pumps) == 0

        petrol_pumps = [(4, 5), (4, 6), (6, 5), (7, 3)]
        assert truck_tour(petrol_pumps) == 2