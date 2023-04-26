from linked_list import LinkedList, Node
import pytest

# configure the fixture with the class configure


class TestLinkedList:
    def test_insert_valid_input(self):
        linked_list = LinkedList()
        linked_list.insert(5)

        assert linked_list.head.data == 5
        assert linked_list.head.next is None


    def test_insert_none(self):
        linked_list = LinkedList()
        with pytest.raises(ValueError):
            linked_list.insert(None)


    def test_reverse_output(self, capfd):
        linked_list = LinkedList()
        linked_list.insert(1)
        linked_list.insert(2)
        linked_list.insert(3)

        linked_list.reversePrint(linked_list.head)
        captured = capfd.readouterr()
        assert captured.out == "3\n2\n1\n"


class TestNode:

    def test_node_initialization(self):
        node = Node(1)
        assert node.data == 1
        assert node.next is None

    def test_set_and_get_attribute(self):
        node = Node(1)
        node.data = 2
        assert node.data == 2
