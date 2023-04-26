from find_median import find_median
from min_max_sum import min_max_sum
from plus_minus import plus_minus
from time_conversion import time_conversion
import pytest

class TestFindMedian:

    def test_find_median_odd(self):
        array: list = [1, 2, 5, 4, 3]
        assert find_median(array) == 3

    def test_find_median_even(self):
        array: list = [1, 2, 3, 4]
        with pytest.raises(ValueError):
            find_median(array)

    def test_input_str(self):
        array: list = [1, 2, 3, 4, 'n', 5, 7]
        with pytest.raises(TypeError):
            find_median(array)

    def test_empty_list(self):
        array: list = []
        with pytest.raises(ValueError):
            find_median(array)

class TestMiniMaxSum:

    def test_min_max_sum_odd(self):
        array: list = [1, 2, 3, 4, 5]
        assert min_max_sum(array) == (10, 14)

    def test_min_max_sum_even(self):
        array: list = [1, 2, 3, 4]
        assert min_max_sum(array) == (6, 9)

    def test_unique_value(self):
        array: list = [1]
        with pytest.raises(ValueError):
            min_max_sum(array)

    def test_empty_array(self):
        array: list = []
        with pytest.raises(ValueError):
            min_max_sum(array)

    def test_two_values(self):
        array: list = [1, 2]
        assert min_max_sum(array) == (1, 2)

class TestPlusMinus:

    def test_plus_min(self):
        array: list = [1, 1, 0, -1, -1]
        assert plus_minus(array) == ['0.400000', '0.400000', '0.200000']

    def test_unique_value(self):
        array: list = [7]
        assert plus_minus(array) == ['1.000000', '0.000000', '0.000000']

    def test_empty_array(self):
        array: list = []
        with pytest.raises(ZeroDivisionError):
            plus_minus(array)

class TestTimeConversion:

    def test_time_conversion_am(self):
        time_to_convert: str = '12:34:54AM'
        assert time_conversion(time_to_convert) == '00:34:54'

    def test_time_conversion_pm(self):
        time_to_convert: str = '09:30:15PM'
        assert time_conversion(time_to_convert) == '21:30:15'

    def test_invalid_format(self):
        time_to_convert: str = '15:00:00AM'
        assert time_conversion(time_to_convert) == '15:00:00'


