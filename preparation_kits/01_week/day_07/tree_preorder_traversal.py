"""
This code is a solution to the HackerRank problem
"Tree: Preorder Traversal" which asks to traverse a binary
tree in pre-order and print the value of each node visited.

The code starts with a Node class that defines a node in a binary tree.
Each node has an info attribute, which stores the node's value,
and left and right attributes that point to the left and right child nodes,
respectively.

The BinarySearchTree class is then defined, which has a root attribute that
stores the root node of the tree. The create method is used to create and add
new nodes to the tree. If the tree is empty, the method creates a new node and
sets it as the root. Otherwise, the method traverses the tree to find the correct
location to add the new node based on the node's value.

The preOrder function takes a binary tree's root node as input, traverses the tree
in pre-order and prints the value of each visited node. In pre-order traversal,
the root node is visited first, then the left subtree, and finally the right subtree.

The code then reads an integer t from input, which represents the number of nodes in
the binary tree, followed by t integers representing the values of the nodes.
The create method of the BinarySearchTree class is then called for each of the
t values to create and add the nodes to the tree.

Finally, the preOrder function is called with the root node of the binary
tree as input to traverse and print the values of each node in pre-order.
"""

class Node:
    # pylint: disable=too-few-public-methods
    """
    A class to represent a node in a binary search tree.

    ...

    Attributes
    ----------
    info : int
        the value stored in the node
    left : Node
        the left child node
    right : Node
        the right child node
    level : int
        the depth of the node in the tree

    Methods
    -------
    __str__():
        Returns the string representation of the node.
    """

    def __init__(self, info: int):
        """
        Constructs all the necessary attributes for the Node object.

        Parameters
        ----------
        info : int
            the value stored in the node
        """
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        """
        Returns the string representation of the node.

        Returns
        -------
        str
            the string representation of the node
        """
        return str(self.info)


class BinarySearchTree:
    # pylint: disable=too-few-public-methods
    """
    A class to represent a binary search tree.

    ...

    Attributes
    ----------
    root : Node
        the root node of the binary search tree

    Methods
    -------
    create(val: int):
        Inserts a new node in the binary search tree with the given value.
    """

    def __init__(self):
        """
        Constructs all the necessary attributes for the BinarySearchTree object.
        """
        self.root = None

    def create(self, val: int):
        """
        Inserts a new node in the binary search tree with the given value.

        Parameters
        ----------
        val : int
            the value to be inserted in the binary search tree
        """
        if self.root is None:
            self.root = Node(val)
        else:
            current = self.root
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


def pre_order_traversal(root: Node):
    """
    Traverses the binary search tree in pre-order (node -> left subtree -> right subtree).

    Parameters
    ----------
    root : Node
        the root node of the binary search tree

    Returns
    -------
    str
        the pre-order traversal of the binary search tree
    """
    if root is None:
        return ""
    return str(root.info) + " " + pre_order_traversal(root.left) + pre_order_traversal(root.right) # pylint: disable=line-too-long


tree = BinarySearchTree()

def execute_pre_order_traversal(arr: list[int]):
    for i in range(len(arr)):
        tree.create(arr[i])

    return pre_order_traversal(tree.root)
