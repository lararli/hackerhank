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

root = {}


def add_to(root, s):
    current_node = root.setdefault(s[0], [0, {}])
    if len(s) == 1:
        current_node[0] += 1
    else:
        add_to(current_node[1], s[1:])


def is_prefix(root, s):
    if len(s) == 1:
        if len(root[s[0]][1]) > 0 or root[s[0]][0] > 1:
            return True
        else:
            return False
    else:
        if root[s[0]][0] > 0:
            return True
        else:
            return is_prefix(root[s[0]][1], s[1:])


def execute_process(list_of_words: list):
    count = 0
    for word in list_of_words:
        add_to(root, word)
        if is_prefix(root, word):
            print('BAD SET')
            print(word)
            break
        count += 1
    if count == len(list_of_words):
        print("GOOD SET")
