#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'noPrefix' function below.
#
# The function accepts STRING_ARRAY words as parameter.
#

class Tree:
    def __init__(self, words):
        self.words = words
        self.root = Node(None)
        self.checkForPrefix()

    def checkForPrefix(self):
        for word in words:
            answer = self.insert(word)

            if answer is not None:
                print("BAD SET")
                print(answer)
                return

        print("GOOD SET")

    def insert(self, word):
        current = self.root

        for i in range(len(word)):
            c = word[i]

            if current.branches[self.indexOf(c)] != None and i == len(word) - 1:
                return word

            if current.branches[self.indexOf(c)] == None:
                current.branches[self.indexOf(c)] = Node(c)

            if current.branches[self.indexOf(c)].isComplete:
                return word

            if i == len(word) - 1:
                current.branches[self.indexOf(c)].isComplete = True

            current = current.branches[self.indexOf(c)]

        return None

    def indexOf(self, c):
        return ord(c) - 97


class Node:
    def __init__(self, value):
        self.value = value
        self.isComplete = False
        self.branches = [None] * (ord("j") - ord("a") + 1)


def noPrefix(words):
    # Write your code here
    root = Tree(words)


if __name__ == '__main__':
    n = int(input().strip())

    words = []

    for _ in range(n):
        words_item = input()
        words.append(words_item)

    noPrefix(words)