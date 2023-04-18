"""
This code defines a singly linked list data structure and
provides a function to insert a node at a specified position
in the linked list.

The SinglyLinkedListNode class represents a single node in the
linked list. It has two attributes: data which stores the node's data,
and next which is a reference to the next node in the list.
The SinglyLinkedList class represents the entire linked list. It has
two attributes: head which is a reference to the first node in the list,
and tail which is a reference to the last node in the list.

The insert_node method of SinglyLinkedList takes a node_data parameter and
inserts a new node with this data at the end of the linked list. It first creates
a new SinglyLinkedListNode object with the provided data. If the linked list is empty,
it sets the new node as the head. Otherwise, it sets the next attribute of the current tail
node to the new node and updates the tail reference to point to the new node.

The print_singly_linked_list function takes a reference to the head node of a linked
list, a separator string sep, and a file pointer fptr, and prints out the
linked list
separated by the separator string. It iterates over the linked list starting
from the head node,
writing out each node's data to the file pointer followed by the separator
string, except
for the last node.

The insertNodeAtPosition function takes a reference to the head node of a linked
list, an integer
data, and an integer position, and inserts a new node with the given data at the
specified position
in the linked list. It first creates a new SinglyLinkedListNode object with the
provided data.
If the head pointer is None, it sets the new node as the head.
Otherwise, it iterates through the linked
list using a temporary node temp and a counter count, skipping nodes until
it reaches the position to insert
the new node. It then updates the next attribute of the new node to point to
the next node after temp, and
the next attribute of temp to point to the new node, effectively inserting the
new node at the specified
position in the list. Finally, it returns the head node of the modified linked list.

Singly linked lists are commonly used data structures in computer science and software engineering.
Here are a few examples of real-world scenarios where a singly linked list implementation like this
could be useful:

Implementing a playlist: A playlist of songs can be represented as a linked list where each node
contains the song name and a reference to the next song. A singly linked list implementation would
allow for easy insertion and removal of songs from the playlist.

Implementing undo-redo functionality in a text editor: A text editor could use a singly linked list
to store the changes made to a document. Each node in the list would
represent a change, and the next
reference would point to the next change. This would allow for efficient
undo and redo functionality by
simply traversing the linked list in reverse or forward order.

Implementing a queue: A queue is a data structure that allows for efficient
insertion and removal of
elements in a First-In-First-Out (FIFO) manner. A singly linked list
implementation would allow for easy
insertion at the end of the list and removal from the beginning of the list, making it an efficient
implementation for a queue.

Implementing a hash table: A hash table is a data structure that allows for
efficient lookup, insertion,
and deletion of key-value pairs. A singly linked list implementation can be
used to handle collisions
that occur when multiple keys hash to the same index in the table. Each index
in the table can store a
linked list of key-value pairs, with efficient insertion and removal of
elements.

These are just a few examples of how a singly linked list implementation can be used
in real-world scenarios.
The flexibility and efficiency of the data structure make it a useful tool for a variety of
applications in software engineering and computer science.
"""
import os


class SinglyLinkedListNode:
    # pylint: disable=too-few-public-methods
    """
    Represents a single node in a singly linked list.
    """

    def __init__(self, node_data):
        """
        Creates a new node with the provided data.

        Args:
            node_data: The data to be stored in the node.
        """
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    # pylint: disable=too-few-public-methods
    """
    Represents a singly linked list.
    """

    def __init__(self):
        """
        Initializes an empty linked list with no head or tail.
        """
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        """
        Inserts a new node with the provided data at the end of the linked list.

        Args:
            node_data: The data to be stored in the new node.
        """
        node = SinglyLinkedListNode(node_data)  # create a new node with the provided data

        if not self.head:  # if the list is empty
            self.head = node  # set the head to the new node
        else:
            self.tail.next = node  # set the next pointer of the current tail to the new node

        self.tail = node  # set the tail to the new node


def print_singly_linked_list(node, sep, file_object):
    """
    Traverses the linked list, starting at the provided node, and writes each node's data to a file.

    Args:
        node: The node to start the traversal from.
        sep: The separator to use between each node's data.
        file_object: A file object to write the data to.
    """
    while node:
        file_object.write(str(node.data))  # write the data of the current node to the file

        node = node.next  # move to the next node in the list

        if node:
            file_object.write(sep)  # write the separator to the file if there are more nodes


def insert_node_at_position(head, new_node_data, node_position):
    """
    Inserts a new node with the provided data at the specified position in a linked list.

    Args:
        head: The head node of the linked list.
        new_node_data: The data for the new node to be inserted.
        node_position: The index (starting at 0) of the position to insert the new node.

    Returns:
        The head node of the updated linked list.
    """
    # create a new node with the provided data
    node = SinglyLinkedListNode(new_node_data)

    # handle the case where the linked list is empty (head pointer is NULL)
    if head is None:
        head = node
    else:
        temp = head
        # skip the nodes to reach the position to insert the new node
        count = 1
        while temp is not None and count < node_position:
            temp = temp.next
            count += 1

        # insert the new node
        node.next = temp.next
        temp.next = node


    return head  # return the head node of the updated linked list


if __name__ == '__main__':
    fptr_path = os.environ['OUTPUT_PATH']

    with open(fptr_path, 'w', encoding='UTF-8') as fptr:
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        data = int(input())

        position = int(input())

        llist_head = insert_node_at_position(llist.head, data, position)

        print_singly_linked_list(llist_head, ' ', fptr)
        fptr.write('\n')
