"""
Huffman coding is a lossless data compression algorithm that
uses variable-length code words to represent symbols in the input data.
It is a prefix code in which no code word is a prefix of any other code word.
The algorithm builds a binary tree based on the frequency of each symbol in the
input data, with the most frequent symbols near the root of the tree and less
frequent symbols near the leaves of the tree. Then, it assigns shorter bit
patterns to more frequent symbols and longer bit patterns to less frequent symbols,
such that no two symbols have the same bit pattern.

The given code is an implementation of Huffman decoding, which is the reverse
process of Huffman coding. The code takes as input a string ip, which represents
the compressed data obtained using Huffman coding. The code first calculates the
frequency of each character in the input string and builds a Huffman tree using the
huffman_hidden() function. The huffman_hidden() function uses a priority queue to
build the tree, where each node in the queue has a frequency and a data field.
The dfs_hidden() function performs a depth-first search of the tree to generate
the Huffman code for each character.

The decodeHuff() function takes as input the root of the Huffman tree and the
compressed data s. The function performs a traversal of the Huffman tree to decode
the compressed data. For each bit in the compressed data, the function moves left
if the bit is 0 and right if the bit is 1. If the function reaches a leaf node
(a node with no children), it appends the character associated with that node to an
array and jumps back to the root of the tree. Finally, the function prints the characters
in the array to obtain the decompressed data.

"""

import queue as Queue

cntr = 0

class Node:
    def __init__(self, freq, data):
        """
        Initializes a Node with its frequency and data.

        Args:
            freq (int): The frequency of the node.
            data (str): The data contained in the node.
        """
        self.freq = freq
        self.data = data
        self.left = None
        self.right = None
        global cntr
        self._count = cntr
        cntr = cntr + 1

    def __lt__(self, other):
        """
        Defines the less than (<) operator for comparison of two nodes.
        Used to prioritize nodes in the priority queue.
        """
        if self.freq != other.freq:
            return self.freq < other.freq
        return self._count < other._count


def huffman_hidden():
    """
    Builds the Huffman tree using a priority queue and returns the root of the tree.
    """
    q = Queue.PriorityQueue()

    for key in freq:
        q.put((freq[key], key, Node(freq[key], key)))

    while q.qsize() != 1:
        a = q.get()
        b = q.get()
        obj = Node(a[0] + b[0], '\0')
        obj.left = a[2]
        obj.right = b[2]
        q.put((obj.freq, obj.data, obj))

    root = q.get()
    root = root[2]  # contains root object
    return root


def dfs_hidden(obj, already):
    """
    Performs depth-first search on the Huffman tree to obtain the binary code for each character.
    """
    if (obj == None):
        return
    elif (obj.data != '\0'):
        code_hidden[obj.data] = already

    dfs_hidden(obj.right, already + "1")
    dfs_hidden(obj.left, already + "0")


def decodeHuff(root, s):
    """
    Decodes the input string `s` using the Huffman tree with root `root`.

    Args:
        root (Node): The root of the Huffman tree.
        s (str): The input string to be decoded.
    """
    cur = root
    chararray = []

    for c in s:
        if c == '0' and cur.left:
            cur = cur.left
        elif cur.right:
            cur = cur.right

        if cur.left is None and cur.right is None:
            chararray.append(cur.data)
            cur = root

    # Print final array
    print("".join(chararray))


ip = input()
freq = {}  # maps each character to its frequency

cntr = 0

for ch in ip:
    if (freq.get(ch) == None):
        freq[ch] = 1
    else:
        freq[ch] += 1

root = huffman_hidden()  # contains root of huffman tree

code_hidden = {}  # contains code for each object

dfs_hidden(root, "")

if len(code_hidden) == 1:  # if there is only one character in the i/p
    for key in code_hidden:
        code_hidden[key] = "0"

toBeDecoded = ""

for ch in ip:
    toBeDecoded += code_hidden[ch]

decodeHuff(root, toBeDecoded)