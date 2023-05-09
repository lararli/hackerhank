from list_replication import replicate_list
import pytest


# valid input
def test_valid_input(capfd):
    num = 2
    arr = [1, 2, 3]

    replicate_list(num=num, arr=arr)
    captured = capfd.readouterr()
    assert captured.out == "1\n1\n2\n2\n3\n3\n"


def test_invalid_input():
    invalid_inputs = [
        ('2', [1, 2, 3]),
        (1, '234'),
        (1.0, [2, 3, 4]),
        (None, [2, 3, 4])
    ]

    for num, arr in invalid_inputs:
        with pytest.raises(TypeError):
            replicate_list(num, arr)
