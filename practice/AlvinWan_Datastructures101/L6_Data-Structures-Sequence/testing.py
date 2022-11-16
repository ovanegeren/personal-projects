
class Stack(list):
    """Simple stack implementation using lists

	>>> stack = Stack([1, 2, 3])
	>>> stack.push(4)
	>>> stack.pop()
	4
	"""
    def push(self, value):
        self.append(value)


class Queue(list):
    """Simple queue implementation using lists.

    Note this is not as efficient as it could be. Instead, this should use 
    collections.deque for efficiency.
  
    >>> queue = Queue([1, 2, 3])
    >>> queue.enqueue(4)
    >>> queue.dequeue()
    1
    """
    def enqueue(self, value):
        self.append(value)

    def dequeue(self):
        return self.pop(0)


#############
# EXERCISES #
#############


class QueueViaStack(list):
    """
    >>> queue = QueueViaStack([1])
    >>> queue.enqueue(2)
    >>> queue.dequeue()
    1
    >>> queue.enqueue(3)
    >>> queue.enqueue(4)
    >>> queue.dequeue()
    2
    >>> queue.dequeue()
    3
    """
  # YOUR ANSWER HERE 
# create a "row" of stacks, passing data from one stack to the next ?
    # false - use 2 stacks. when dequeuing, pop everything but the last from stack 1 -> 2, and then pop it back from 2->1 to refill the original stack in the original order
# runtime complexity: O(n)  ?
    # Correct - popping and placing items in a stack is O(1), for a queue size n, we would need to do this ~2n
    # memory complexity = O(n)
    def __init__(self, list):
        self.size = len(list)
        self.stack_main = Stack(list)
        self.stack_temp = Stack()

    def enqueue(self, value):
        self.stack_main.push(value)
        self.size += 1

    def dequeue(self):
        for i in range(self.size - 1):
            self.stack_temp.push(self.stack_main.pop())
        value = self.stack_main.pop()
        for i in range(self.size - 1):
            self.stack_main.push(self.stack_temp.pop())
        self.size -= 1
        return value
