"""
Exercises for "Kick Butt in Coding Interviews: Data Structures in Python"
by Alvin Wan

Take the course at https://skl.sh/
Find all course resources at https://alvinwan.com/datastructures101
"""


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


class Link:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def tolist(self):
        """Converts linked list to a list, for visualization.
    
        You can ignore this implementation, as it is just for display in the 
        subsequent code.
        """
        lst, link = [], self
        while link is not None:
            lst.append(link.value)
            link = link.next
        return lst


#############
# EXERCISES #
#############


def append(link, value):
    """Append item to the linked list.
  
    >>> link = Link(1, Link(2, Link(3)))
    >>> append(link, 4)
    >>> link.tolist()
    [1, 2, 3, 4]
    """
    pass  # YOUR ANSWER HERE


def insert(link, i, value):
    """Insert *after the provided index i
  
    >>> link = Link(1, Link(2, Link(3)))
    >>> insert(link, 0, 4)
    >>> link.tolist()
    [1, 4, 2, 3]
    """
    pass  # YOUR ANSWER HERE


class StackViaLinkedList:
    """Implement stack using a linked list as input.

    >>> link = Link(1, Link(2))
    >>> stack = StackViaLinkedList(link)
    >>> stack.pop()
    2
    >>> stack.push(2)
    >>> stack.push(3)
    >>> stack.pop()
    3
    >>> stack.pop()
    2
    """
    def __init__(self, link):
        self.link = link

    def push(self, value):
        pass  # YOUR ANSWER HERE

    def pop(self):
        pass  # YOUR ANSWER HERE


def remove_cycle(link):
    """Find and remove cycle in linked list if present.

    You can assume all link values are distinct.
    
    Hint: Use a set to keep track of which values you've already seen!
  
    >>> link = Link(1, Link(2, Link(3)))
    >>> link.next.next.next = link  # link 3 to 1 - don't run .tolist()!
    >>> remove_cycle(link)
    >>> link.next.next.next is None
    True
    """
    pass  # YOUR ANSWER HERE


class File:
    """
    Create a file object that can efficiently merge with other files.

    There are several possible solutions:

    1. (Implemented below) Each file constructs a linked list and stores the
       head and tail. Merge is O(1). Construction is O(n).
    2. Each file constructs a linked list and during merge, navigates to the
       end of the current file, before linking to the next file. This is an
       O(n) merge. O(n) construction.
    3. Each file simply retains the original list of lines. Technically,
       file initialization is then constant time. During merge, we
       concatenate the lists together. This is also an O(n) merge.
       O(1) construction.

    >>> a = File(['hoho'])
    >>> b = File(['hehe', 'haha'])
    >>> a.merge(b)
    >>> a.link.tolist()
    ['hoho', 'hehe', 'haha']
    >>> c = File()
    >>> c.merge(b)
    >>> c.link.tolist()
    ['hehe', 'haha']
    """
    def __init__(self, lines=()):
        pass  # YOUR ANSWER HERE

    def merge(self, file):
        pass  # YOUR ANSWER HERE


def is_palindrome_link(link):
    """Check if linked list is a palindrome.
  
    >>> racecar = Link('r', Link('a', Link('c', Link('e', Link('c',
    ...     Link('a', Link('r')))))))
    >>> is_palindrome_link(racecar)
    True
    >>> raceca = Link('r', Link('a', Link('c', Link('e', Link('c',
    ...     Link('a'))))))
    >>> is_palindrome_link(raceca)
    False
    """
    pass  # YOUR ANSWER HERE


#########
# BONUS #
#########


def delete(link, i):
    """Remove item *after provided index i
  
    >>> link = Link(1, Link(2, Link(3)))
    >>> delete(link, 1)
    >>> link.tolist()
    [1, 2]
    """
    pass  # YOUR ANSWER HERE


def intersection(link1, link2):
    """Compute the intersection of two linked lists.

    Return the result as a linked list.
  
    >>> link1 = Link(1, Link(2, Link(3)))
    >>> link2 = Link(4, Link(3, Link(2)))
    >>> intersection(link1, link2).tolist()
    [2, 3]
    """
    pass  # YOUR ANSWER HERE


