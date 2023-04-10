import os
class SinglyLinkedListNode:
    """
    A node in a singly linked list.

    Attributes:
        data: The data stored in the node.
        next: The next node in the linked list.
    """

    def __init__(self, node_data):
        """
        Constructs a new singly linked list node with the given data.

        Args:
            node_data: The data to be stored in the node.
        """
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    """
    A singly linked list.

    Attributes:
        head: The first node in the linked list.
        tail: The last node in the linked list.
    """

    def __init__(self):
        """
        Constructs a new empty singly linked list.
        """
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        """
        Inserts a new node with the given data at the end of the linked list.

        Args:
            node_data: The data to be stored in the new node.
        """
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node, sep=' ', fptr=None):
    """
    Prints the data stored in the nodes of a singly linked list.

    Args:
        node: The first node in the linked list.
        sep: The separator string to use between node data. Defaults to ' '.
        fptr: The file object to write the output to. Defaults to None.
    """
    while node:
        if fptr:
            fptr.write(str(node.data))
        else:
            print(node.data, end='')

        node = node.next

        if node:
            if fptr:
                fptr.write(sep)
            else:
                print(sep, end='')


def merge_lists(head1, head2):
    """
    Merges two sorted singly linked lists into a single sorted linked list.

    Args:
        head1: The first node of the first linked list.
        head2: The first node of the second linked list.

    Returns:
        The first node of the merged linked list.
    """
    # both lists are None
    if head1 is None and head2 is None:
        return None

    # only one list is None
    if head1 is None:
        return head2

    if head2 is None:
        return head1

    # general logic
    if head1.data < head2.data:
        temp = head1
        temp.next = merge_lists(head1.next, head2)

    else:
        temp = head2
        temp.next = merge_lists(head1, head2.next)

    return temp

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)

        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        llist3 = merge_lists(llist1.head, llist2.head)

        print_singly_linked_list(llist3, ' ', fptr)
        fptr.write('\n')

    fptr.close()