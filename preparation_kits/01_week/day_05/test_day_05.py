import pytest
from balanced_brackets import is_balanced
from linked_list_mod import print_singly_linked_list, merge_lists, SinglyLinkedList
from pairs import pairs
from queue_two_stacks import queue_two_stacks
import io
import sys


class TestBalancedBrackets:
    def test_balanced_brackets(self):
        assert is_balanced('()') == 'YES'
        assert is_balanced('(())') == 'YES'
        assert is_balanced('()[]{}') == 'YES'
        assert is_balanced('[{()}]') == 'YES'
        assert is_balanced('({[]})') == 'YES'
        assert is_balanced('(]') == 'NO'
        assert is_balanced('[(])') == 'NO'
        assert is_balanced('(})') == 'NO'
        assert is_balanced('{[()]}(') == 'NO'
        assert is_balanced('') == 'YES'
        assert is_balanced('None') == 'NO'

class TestLinkedList:

    def test_merge_empty_lists(self):
        """
        Test Case 1:
        Merging two empty lists should return None.
        """
        list1 = SinglyLinkedList()
        list2 = SinglyLinkedList()
        merged_list = merge_lists(list1.head, list2.head)
        assert merged_list == None

    def test_merge_empty_with_nonempty(self):
        """
        Test Case 2:
        Merging an empty list with a non-empty list should return the non-empty list.
        """
        list1 = SinglyLinkedList()
        list2 = SinglyLinkedList()
        list2.insert_node(1)
        list2.insert_node(3)
        list2.insert_node(5)

        merged_list = merge_lists(list1.head, list2.head)
        assert merged_list.data == 1
        assert merged_list.next.data == 3
        assert merged_list.next.next.data == 5
        assert merged_list.next.next.next == None

    def test_merge_lists_with_same_value(self):
        """
        Test Case 3:
        Merging two lists with the same values should return a merged list with all values in sorted order.
        """
        list1 = SinglyLinkedList()
        list1.insert_node(1)
        list1.insert_node(3)
        list1.insert_node(5)

        list2 = SinglyLinkedList()
        list2.insert_node(1)
        list2.insert_node(3)
        list2.insert_node(5)

        merged_list = merge_lists(list1.head, list2.head)

        assert merged_list.data == 1
        assert merged_list.next.data == 1
        assert merged_list.next.next.data == 3
        assert merged_list.next.next.next.data == 3
        assert merged_list.next.next.next.next.data == 5
        assert merged_list.next.next.next.next.next.data == 5
        assert merged_list.next.next.next.next.next.next == None

    def test_merge_lists_with_different_values(self):
        """
        Test Case 4:
        Merging two lists with different values should return a merged list with all values in sorted order.
        """
        list1 = SinglyLinkedList()
        list1.insert_node(2)
        list1.insert_node(4)
        list1.insert_node(6)

        list2 = SinglyLinkedList()
        list2.insert_node(1)
        list2.insert_node(3)
        list2.insert_node(5)

        merged_list = merge_lists(list1.head, list2.head)

        assert merged_list.data == 1
        assert merged_list.next.data == 2
        assert merged_list.next.next.data == 3
        assert merged_list.next.next.next.data == 4
        assert merged_list.next.next.next.next.data == 5
        assert merged_list.next.next.next.next.next.data == 6
        assert merged_list.next.next.next.next.next.next == None

    def test_print_singly_linked_list(self):
        # create linked list
        linked_list = SinglyLinkedList()
        linked_list.insert_node(1)
        linked_list.insert_node(2)
        linked_list.insert_node(3)

        # create file object for writing
        file_obj = io.StringIO()

        # print linked list to file object
        print_singly_linked_list(linked_list.head, file_obj=file_obj)

        # check output
        file_obj.seek(0)
        assert file_obj.read() == "1 2 3"

    def test_singly_linked_list_file_obj(self):

        # create linked list
        linked_list = SinglyLinkedList()
        linked_list.insert_node(1)
        linked_list.insert_node(2)
        linked_list.insert_node(3)

        # create file object for writing
        file_obj = io.StringIO()

        # print linked list to file object
        print_singly_linked_list(linked_list.head, file_obj=file_obj)

        # check output
        file_obj.seek(0)
        assert file_obj.read() == '1 2 3'

class TestPairs:

    def test_pairs(self):

        assert pairs(1, [1, 2, 3, 4, 5]) == 4
        assert pairs(2, [1, 3, 4, 7]) == 1
        assert pairs(3, [3, 3, 3, 3]) == 0
        assert pairs(0, [1, 2, 3, 4, 5]) == 5
        assert pairs(1, [1, 1, 1, 2, 2]) == 1

class TestQueueTwoStacks:

    def test_queue_two_stacks_push(self):
        """
        The first test case checks if an element is added to the stackpush
        list when the queue_two_stacks() function is called with stack_list
        containing the string '1' (indicating a push operation) and the value '5'.
        """
        stack_list = ['1', '5']
        num_queries = 1
        stackpush = []
        stackdelete = []
        queue_two_stacks(stack_list, num_queries, stackpush, stackdelete)
        assert stackpush == ['5']

    def test_queue_two_stacks_dequeue(self):
        """
        The second test case checks if an element is removed from
        the stackdelete list when the queue_two_stacks() function is
        called with stack_list containing the string '2'
        (indicating a dequeue operation) and stackdelete
        containing elements '5', '3', and '4'.
        """
        stack_list = ['2']
        num_queries = 1
        stackpush = []
        stackdelete = ['5', '3', '4']
        queue_two_stacks(stack_list, num_queries, stackpush, stackdelete)
        assert stackdelete == ['5', '3']

    def test_queue_two_stacks_front(self):
        """
        The third test case checks if the front element of the queue is
        correctly returned by the queue_two_stacks() function when
        stack_list contains the string '3' (indicating a front operation)
        and stackdelete containing elements '5', '3', and '4'
        """
        stack_list = ['2']
        num_queries = 1
        stackpush = []
        stackdelete = ['5', '3', '4']
        queue_two_stacks(stack_list, num_queries, stackpush, stackdelete)
        assert stackdelete == ['5', '3']

    def test_queue_two_stacks(self):
        stack_list = ['2']
        num_queries = 1
        stackpush = [1, 2, 3, 4]
        stackdelete = []

        queue_two_stacks(stack_list, num_queries, stackpush, stackdelete)

        assert stackpush == []
        assert stackdelete == [4, 3, 2]

    def test_queue_two_stacks_else(self):
        stack_list = ['3']
        stackpush = ['1', '2', '3']
        stackdelete = []
        expected_output = '1\n'

        # Redirect stdout to a StringIO object
        stdout = io.StringIO()
        sys.stdout = stdout

        # Call the function with test inputs
        queue_two_stacks(stack_list, 1, stackpush, stackdelete)

        # Get the printed output
        actual_output = stdout.getvalue()

        # Assert that the output matches the expected output
        assert actual_output == expected_output

        # Reset stdout
        sys.stdout = sys.__stdout__