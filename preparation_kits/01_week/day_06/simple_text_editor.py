"""
The code is a solution to the HackerRank Simple Text Editor Challenge.
The program reads a number "no_ops" from the input, which represents the
number of operations to be performed on a string "s". Then it reads "no_ops"
lines, each containing an operation and an argument (if required).

The solution uses four types of operations:

1. Append given string to the end of s
2. Delete last k characters from s
3. Print the kth character of s
4. Revert s to the previous state in history

The program stores the current state of the string "s" after each
operation in the "history" list. To do so, the program imports the "copy"
module to make deep copies of the string. Finally, the program executes each
operation in the "ops" list in the order they were read from the input.
"""

# Import copy module to make deep copies of the string
from copy import copy


# Read number of operations from input
no_ops = int(input())

# Initialize a list to store all the operations
ops = []

# Initialize an empty string to store the current string
s = []

# Loop through each operation and append it to ops list
for i in range(no_ops):
    one_op = input().split(' ')
    ops.append(one_op)

# Initialize a list to store the history of the string
history = []

# Loop through each operation in ops list
for op in ops:

    # If the operation is "1", append the given string to s and
    # save the current state of s to history
    if op[0] == '1':
        to_append = op[1]
        history.append(copy(s))
        s.extend(to_append)

    # If the operation is "2", delete the last k characters from s and save the
    # state of s to history
    elif op[0] == '2':
        k = int(op[1])
        history.append(copy(s))
        del s[-k:]

    # If the operation is "3", print the kth character of s
    elif op[0] == '3':
        k = int(op[1])
        print(s[k - 1])

    # If the operation is "4", revert s to the previous state in history
    elif op[0] == '4':
        s = history.pop()
