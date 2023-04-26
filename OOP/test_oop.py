from linked_list import LinkedList
import pytest

# configure the fixture with the class configure
def test_insert_valid_input():
    linked_list = LinkedList()
    linked_list.insert(5)

    assert linked_list.head.data == 5
    assert linked_list.head.next is None


def test_insert_none():
    linked_list = LinkedList()
    with pytest.raises(ValueError):
        linked_list.insert(None)


def test_reverse_output(capfd):
    linked_list = LinkedList()
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)

    linked_list.reversePrint(linked_list.head)
    captured = capfd.readouterr()
    assert captured.out == "3\n2\n1\n"