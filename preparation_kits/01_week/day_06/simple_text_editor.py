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

from typing import List


def simulate_operations(input_string: str) -> List[str]:
    from copy import copy

    input_lines = input_string.strip().split('\n')
    no_ops = int(input_lines[0])
    ops = []
    outputs = []

    s = []
    history = []

    for i in range(1, no_ops + 1):
        one_op = input_lines[i].split(' ')
        ops.append(one_op)

    for op in ops:
        if op[0] == '1':
            to_append = op[1]
            history.append(copy(s))
            s.extend(to_append)
        elif op[0] == '2':
            k = int(op[1])
            history.append(copy(s))
            del s[-k:]
        elif op[0] == '3':
            k = int(op[1])
            outputs.append(s[k - 1])
        elif op[0] == '4':
            s = history.pop()

    return outputs


# Example usage
input_str = """
4
1 abc
3 3
2 2
4
"""

output = simulate_operations(input_str)
print(output)  # Output: ['c']
