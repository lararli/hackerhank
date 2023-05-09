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


def huffman_hidden(freq):
    cntr = 0

    class Node:
        def __init__(self, freq, data):
            self.freq = freq
            self.data = data
            self.left = None
            self.right = None
            nonlocal cntr
            self._count = cntr
            cntr += 1

        def __lt__(self, other):
            if self.freq != other.freq:
                return self.freq < other.freq
            return self._count < other._count

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


def dfs_hidden(obj, already, code_hidden):
    if obj is None:
        return
    elif obj.data != '\0':
        code_hidden[obj.data] = already

    dfs_hidden(obj.right, already + "1", code_hidden)
    dfs_hidden(obj.left, already + "0", code_hidden)


def decodeHuff(root, s):
    current = root
    result = ''
    for code in s:
        if int(code) == 0:
            current = current.left
        else:
            current = current.right
        if current.left is None and current.right is None:
            result += current.data
            current = root
    return result


def execute_decodeHuff(ip: str):
    freq = {}

    for ch in ip:
        if freq.get(ch) is None:
            freq[ch] = 1
        else:
            freq[ch] += 1

    root = huffman_hidden(freq)
    code_hidden = {}
    dfs_hidden(root, "", code_hidden)

    if len(code_hidden) == 1:
        for key in code_hidden:
            code_hidden[key] = "0"

    toBeDecoded = ""

    for ch in ip:
        toBeDecoded += code_hidden[ch]

    return decodeHuff(root, toBeDecoded)
    # assert decoded_str == "abcde"
