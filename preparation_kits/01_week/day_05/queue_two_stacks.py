"""
The queue_two_stacks function simulates a queue data
structure using two stacks. It receives an integer q representing
the number of queries to be executed, and two lists stackpush and
stackdelete representing the two stacks used in the simulation.

The function loops through the queries and performs one of three
operations, depending on the query type.

If the query type is 1, it performs an enqueue operation by appending
the second element of the query list to the stackpush. If the query type is 2,
it performs a dequeue operation by popping the top element of stackdelete.

If stackdelete is empty, the function first pop elements from stackpush
and append them to stackdelete. Finally, if the query type is 3, it prints
the top element of stackdelete without removing it.
"""

def queue_two_stacks(stack_list: list, num_queries: int, stackpush: list, stackdelete: list):
    """Simulates a queue using two stacks.

    Args:
        num_queries (int): Number of queries.
        stackpush (list): Stack for push operation.
        stackdelete (list): Stack for delete operation.

    Returns:
        str: Resulting queue of each query.
    """
    for _ in range(num_queries):
        # enqueue
        if stack_list[0] == '1':
            stackpush.append(stack_list[1])

        # dequeue
        elif stack_list[0] == '2':
            if not stackdelete:
                while stackpush:
                    stackdelete.append(stackpush.pop())

            stackdelete.pop()

        # print the front element
        else:
            if not stackdelete:
                while stackpush:
                    stackdelete.append(stackpush.pop())
            print(stackdelete[-1])
