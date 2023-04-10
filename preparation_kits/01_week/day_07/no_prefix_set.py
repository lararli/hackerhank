"""
The code is a solution for the HackerRank challenge
called "No Prefix Set". The problem requires to determine
if a given set of strings is a "good" set, which means no string
is a prefix of another string in the set. If there is a string that
is a prefix of another string, then it's a "bad" set.

The solution defines two classes: Tree and Node. Tree represents a
trie data structure that stores the set of strings. Node represents
a node in the trie.

In the Tree class, the constructor takes a list of words as an input parameter.
It initializes an empty root node and then calls the checkForPrefix() method
to check if there is a prefix in the given set of words.

The checkForPrefix() method iterates through each word in the list of
words and calls the insert() method on each word. If the insert() method returns
a non-null value, it means there is a prefix in the set of words, and the method
prints "BAD SET" and the prefix. If the insert() method returns None for all words,
it means there are no prefixes, and the method prints "GOOD SET".

The insert() method takes a word as an input parameter and inserts it
into the trie. The method starts from the root and iterates through each
character in the word. For each character, it checks if there is a child
node with that character, and if there isn't, it creates a new child node.
If the child node is already marked as complete, it means there is a prefix
in the set of words, and the method returns the word. If the method reaches
the end of the word and the last character's child node isn't marked as complete,
it marks the child node as complete.

The indexOf() method takes a character as an input parameter and returns its
index in the alphabet.

The Node class represents a node in the trie. It has a value attribute that stores
the character, an isComplete attribute that marks the node as a complete word,
and a branches attribute that stores the child nodes.

The noPrefix() function is the entry point for the program. It takes a list
of words as an input parameter, creates a Tree object with the list of words,
and returns the root node of the tree.
"""

class Tree:
    """
    The Tree class represents a tree data structure that is used to check if any prefix of a word in the list
    matches with any other word in the list.
    """
    def __init__(self, words):
        """
        Initializes a new instance of the Tree class.
        :param words: A list of strings representing the words to be checked.
        """
        self.words = words
        self.root = Node(None)
        self.check_for_prefix()

    def check_for_prefix(self):
        """
        Checks if any prefix of a word in the list matches with any other word in the list.
        If a prefix match is found, it prints "BAD SET" and the word causing the issue.
        Otherwise, it prints "GOOD SET".
        """
        for word in self.words:
            answer = self.insert(word)

            if answer is not None:
                print("BAD SET")
                print(answer)
                return

        print("GOOD SET")

    def insert(self, word):
        """
        Inserts a word into the tree.
        :param word: A string representing the word to be inserted.
        :return: None if the insertion is successful; otherwise, the word that caused the issue.
        """
        current = self.root

        for i in range(len(word)):
            c = word[i]

            if current.branches[self.index_of(c)] is not None and i == len(word) - 1:
                return word

            if current.branches[self.index_of(c)] is None:
                current.branches[self.index_of(c)] = Node(c)

            if current.branches[self.index_of(c)].is_complete:
                return word

            if i == len(word) - 1:
                current.branches[self.index_of(c)].is_complete = True

            current = current.branches[self.index_of(c)]

        return None

    def index_of(self, c):
        """
        Calculates the index of a character in the branches list.
        :param c: A character whose index is to be calculated.
        :return: The index of the character.
        """
        return ord(c) - 97


class Node:
    """
    The Node class represents a node in the tree.
    """
    def __init__(self, value):
        """
        Initializes a new instance of the Node class.
        :param value: The value of the node.
        """
        self.value = value
        self.is_complete = False
        self.branches = [None] * (ord("j") - ord("a") + 1)


def noPrefix(words):
    """
    Checks if any prefix of a word in the list matches with any other word in the list.
    If a prefix match is found, it prints "BAD SET" and the word causing the issue.
    Otherwise, it prints "GOOD SET".
    :param words: A list of strings representing the words to be checked.
    """
    root = Tree(words)


if __name__ == '__main__':
    n = int(input().strip())

    words = []

    for _ in range(n):
        words_item = input()
        words.append(words_item)

    noPrefix(words)