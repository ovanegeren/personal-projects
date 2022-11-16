"""
Exercises for "Kick Butt in Coding Interviews: Data Structures in Python"
by Alvin Wan

Take the course at https://skl.sh/
Find all course resources at https://alvinwan.com/datastructures101

RUN USING COMMAND: "python -m doctest main.py"
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
    ### YOUR ANSWER HERE
    '''
    Algorithm: find the current last element in the linked list by following links, and add an additional link to append the given value

    Complexity
        runtime: o(n), we need to search the existing list to find the last element
        memory: o(n), assuming the list input length n counts towards memory, program memory is o(n) as we need to store the list
            - false assumption: 'additional' storage is constant, therefore o(1)
    '''
    current_link = link
    ins = Link(value)
    while current_link.next is not None:
        current_link = current_link.next
    current_link.next = ins


def insert(link, i, value):
    """Insert *after the provided index i
  
    >>> link = Link(1, Link(2, Link(3)))
    >>> insert(link, 0, 4)
    >>> link.tolist()
    [1, 4, 2, 3]
    """
    ### YOUR ANSWER HERE
    '''
    Algorithm: traverse the linked list going from the start to list index i. 
    Upon getting there, instert a link copying over the link.next elment into the insert.
    Once copied, replace the link.next of the current element with the new insert-link

    Complexity
        runtime: O(n), as we have to progress through each link in the list to get to our desired point
        memory: O(1), as we are inserting a single, constant size element
    '''
    ### ORIGINAL ATTEMPT
    # ind = 0
    # current = link
    # ins = Link(value)
    # while (ind < i) and (current.next is not None):
    #     i += 1
    #     current = current.next
    
    # ins.next = current.next
    # current.next = ins

    ### SOLUTION - similar to attempt, but can insert easier using class declaration
    ind = 0
    current = link
    while (ind < i) and (current.next is not None):
        i += 1
        current = current.next
    current.next = Link(value, current.next)            #easier insertion


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
    '''
    ALGORITHM: create a linked list where the first element is the top of the stack.
            When pushing to the stack, create a new 'first' element in the linked list.
            When popping the stack, remove the first element from the list (ie. make the second element the new first element in the list)
    FALSE. Solution: similar idea to the original answer, but the top of the stack should be the end of the linked list (see example)

    Complexity:
        Runtime: O(n), as we have to navigate the entire linked list every time we want to add / pop a single element
        Memory: O(1), as we are only adding or popping a single, constant size element at a time
    '''
    def __init__(self, link):
        self.link = link

    def push(self, value):
        # YOUR ANSWER HERE
        current = self.link
        while current.next is not None:
            current = current.next
        current.next = Link(value)

    def pop(self):
        # YOUR ANSWER HERE
        current = self.link
        while current.next.next is not None:
            current = current.next
        value = current.next.value
        current.next = None
        return value


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
    # YOUR ANSWER HERE
    '''
    Algorithm: Because we assume there are no repeated values in the list, finding a repeated value indicates a list cycle. 
        (we could otherwise serach for a cycle by inspecting link addresses)
        Cycle through linked list comparing current value to second linked list containing all previous values. 
        If the current link we are inspecting has no previous instances, add the value to the list of previous values.
        If the current link does have a previous instance, remove it's future address to break the cycle.

    Complexity:
        Runtime complexity is O(n^2), we need to perform an O(n) operation on each link in the list to search for previous values
        Memory complexity is O(n), as we will need to store a list of previous values up to n links.
    FALSE: solution can be achieved with O(n) runtime complexity (???)
        NOTE: makes sense now, as set() searches in constant time (which might have been useful for a datastructures course...)
    '''
    # # ORIGINAL ATTEMPT
    # # Not sure how I can achieve this in O(n) runtime complexity (without hashmaps), so I will do it the only way I know
    # prev = Link(link.value)
    # prev_head = prev.copy()
    # while link.next is not None:
    #     while prev.next is not None:
    #         if prev.value == link.value:
    #             # if repeat detected, unlink cycle
    #             return
    #         else:
    #             prev = prev.next # iterate through all values in the list of prevous
    #     prev.next = Link(link.value)
    #     #restart linked list ??
    #     link = link.next    # iterate through all values in the main list        
    #     # if no repeat detected add value to link of prevous values
    # # ATTEMPT FAILED: not sure how to return ot the head of the linked list, as the class is mutable
    # SOLUTION: Uses set() data structure (which is bullshit - he never mentioned this in the entire course)
    seen = set()
    while link.next:
        if link.next.value in seen:         # if the next value has already been seen, break the cycle
            link.next = None
            break                           # assumes only 1 cycle per list 
        seen.add(link.value)
        link = link.next
    # TODO: research set type in Python
            




class File:
    """
    NOTE: purely conceptual exercise, solution exists, exercise not designed to be attempted but discussed algorithmically
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
    '''
    Algorithm: 
    '''
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
    '''
    ALGORITHM: the word is stored as a linked list. Combining this with a stack and queue.
        Go through the linked list, adding each letter to both a stack AND a queue.
        After this, pop a letter from the stack, and compare it to the letter taken from the queue.
        This compares first to last
    COMPLEXITY:
        runtime complexity is  O(2n), as O(n) operation required to collect letters from linked list, 
            and O(n) operation required to compare the stack / queue
        memory complexity is O(2n), as both a stack and a queue of size n are required for comparison
    '''
    # YOUR ANSWER HERE
    stack = Stack()
    queue = Queue()
    while link is not None:
        stack.push(link.value)
        queue.enqueue(link.value)
        link = link.next

    # stack and queue should always be same length, so either are useable
    while len(stack):       # len(stack) returns iterable of size stack? FALSE: lenght decreases as we pop from stack, reducing length to 0 
        if stack.pop() != queue.dequeue():
            return False
    return True


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


