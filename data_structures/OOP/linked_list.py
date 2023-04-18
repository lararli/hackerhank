"""This module provides a LinkedList class for creating and manipulating linked lists.

Classes:
- LinkedList: A class for creating and manipulating singly-linked lists.

Example usage:
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.reversePrint(ll.head) # prints "3 2 1"
"""


class Node:
    """
    A class representing a node in a linked list.

    Attributes:
        data (Any): The data stored in the node.
        next (Node): A reference to the next node in the list.
    """

    def __init__(self, data):
        """
        Initializes a new instance of the Node class.

        Args:
            data (Any): The data to be stored in the node.
        """
        self.data = data
        self.next = None


class LinkedList:
    """
    A class representing a singly linked list.

    Attributes:
        head (Node): The first node in the list.
    """

    def __init__(self):
        """
        Initializes a new instance of the LinkedList class.
        """
        self.head = None

    def insert(self, data):
        """
        Inserts a new node with the specified data at the end of the list.

        Args:
            data (Any): The data to be stored in the new node.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def reversePrint(self, node):
        """
        Prints the data of the nodes in the list in reverse order, starting from the specified node.

        Args:
            node (Node): The starting node for the reverse traversal.
        """
        if node is None:
            return
        self.reversePrint(node.next)
        print(node.data)


if __name__ == "__main__":

    ll = LinkedList()  # Create a new instance of the LinkedList class

    # Insert three new nodes with data 1, 2, and 3 into the list
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)

    # Print the data of the nodes in the list in reverse order, starting from the head node
    ll.reversePrint(ll.head)

