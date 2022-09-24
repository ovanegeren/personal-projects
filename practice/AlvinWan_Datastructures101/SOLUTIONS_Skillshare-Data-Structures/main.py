"""
Solutions for "Kick Butt in Coding Interviews: Data Structures in Python"
by Alvin Wan

Take the course at https://skl.sh/
Find all course resources at https://alvinwan.com/datastructures101
"""


#######
# OOG #
#######


#############
# EXERCISES #
#############


def runtime_basic1(N):
    """What is the runtime complexity of the following, as a function of N?"""
    for i in range(N):
        print(i)
    # Answer: O(N)
    # Explanation: We have a for loop that iterates over each element in N once.
    # As a result, as N grows, we expect runtime to grow proportionally.


def runtime_basic2(N):
    """What is the runtime complexity of the following, as a function of N?"""
    for i in range(N):
        for j in range(N):
            print(i, j)
    # Answer: O(N^2)
    # Explanation: We iterate over each element in N. Then, *for each iteration*
    # we iterate over each element in N again. So, we have N * N or N^2 runtime.


def runtime_basic3(N):
    """What is the runtime complexity of the following, as a function of N?"""
    i = N
    while i > 1:
        i //= 2
        print(i)
    # Answer: O(log(N))
    # Explanation: Each iteraation, we halve the workload. See subsequent lesson
    # for why log = halve. For now, just remember that if the workload is halved
    # each iteration, the function has logarithmic complexity.


def runtime_tricky1(N):
    """How many times is print called, as a function of N?

    Notice the if statement! How does that affect runtime complexity, if at all?
    """
    for i in range(N):
        for j in range(N):
            if i == j:
                print(i, j)
    # Answer: O(N)
    # Explanation: This *looks like O(N^2). However, notice our if condition.
    # This if condition ensures that each inner loop runs only once, per
    # outer loop iterate. There are several cases of tricky algorithms like this
    # where a special if statement reduces runtime complexity. Keep in mind
    # that this is a possibility!


def runtime_tricky2(N):
    """How many times is print called, as a function of N?

    Notice the inner loop only counts up to i! How does that affect runtime
    complexity, if at all?
    """
    for i in range(N):
        for j in range(i):
            print(i, j)
    # Answer: O(N^2)
    # Explanation: It *looks like the count up to i would reduce runtime.
    # However, this is unfortunately not the case. See the corresponding lesson
    # for a visualization that explains why. (If you've already seen the lesson,
    # a quick summary is: Area of half of NxN square is still 0.5N^2 ~ O(N^2))

"""
Solutions for "Kick Butt in Coding Interviews: Data Structures in Python"
by Alvin Wan

Take the course at https://skl.sh/
Find all course resources at https://alvinwan.com/datastructures101
"""


#########
# LISTS #
#########


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
    while link.next is not None:
        link = link.next
    link.next = Link(value)


def append_full(link, value):
    """Append item to the linked list.
  
    Full version accounts for invalid inputs.
    
    >>> link = Link(1, Link(2, Link(3)))
    >>> append(link, 4)
    >>> link.tolist()
    [1, 2, 3, 4]
    """
    assert link is not None, 'Link cannot be empty'
    while link.next is not None:
        link = link.next
    link.next = Link(value)


def insert(link, i, value):
    """Insert *after the provided index i
  
    >>> link = Link(1, Link(2, Link(3)))
    >>> insert(link, 0, 4)
    >>> link.tolist()
    [1, 4, 2, 3]
    """
    for _ in range(i):
        link = link.next
    link.next = Link(value, link.next)


def insert_full(link, i, value):
    """Insert *at the provided index i and return new.

    Full version accounts for edge cases and invalid inputs.
    
    >>> link = Link(1, Link(2, Link(3)))
    >>> insert_full(link, 0, 0).tolist()
    [0, 1, 2, 3]
    """
    if i == 0:  # if replacing first element, return pointer to new link
        return Link(value, link)

    head = link
    for _ in range(i - 1):  # otherwise, find the element before the new link
        assert link.next, "Index i beyond list length"
        link = link.next
    link.next = Link(value, link.next)  # insert a new link
    return head


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
        link = self.link
        while link.next is not None:
            link = link.next
        link.next = Link(value)

    def pop(self):
        link = self.link
        while link.next.next is not None:
            link = link.next
        value = link.next.value
        link.next = None
        return value


class StackViaLinkedListFull:
    """
    Full version accounts for edge cases and invalid inputs.
  
    >>> link = Link(1, Link(2))
    >>> stack = StackViaLinkedListFull(link)
    >>> stack.pop()
    2
    >>> stack.push(2)
    >>> stack.push(3)
    >>> stack.pop()
    3
    >>> stack.pop()
    2
    >>> stack.pop()
    1
    >>> stack.push(1)
    """
    def __init__(self, link):
        self.link = link

    def push(self, value):
        link = self.link
        if not link:
            self.link = Link(value)
            return
        while link.next is not None:
            link = link.next
        link.next = Link(value)

    def pop(self):
        link = self.link
        if not link:
            raise UserWarning('No more entries')
        if not link.next:
            value = link.value
            self.link = None
            return value
        while link.next.next is not None:
            link = link.next
        value = link.next.value
        link.next = None
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
    seen = set()
    while link.next:
        if link.next.value in seen:
            link.next = None
            break
        seen.add(link.value)
        link = link.next


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
        self.link = None
        self.least_recent = None
        for line in lines[::-1]:
            self.link = Link(line, self.link)
            if self.least_recent is None:
                self.least_recent = self.link

    def merge(self, file):
        if self.link is None:
            self.link = file.link
        else:
            self.least_recent.next = file.link
        self.least_recent = file.least_recent


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
    stack = Stack()
    queue = Queue()
    while link is not None:
        stack.push(link.value)
        queue.enqueue(link.value)
        link = link.next
    while len(stack):
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
    for _ in range(i):
        link = link.next
    if link and link.next:
        link.next = link.next.next


def delete_full(link, i):
    """Remove item *at provided index i.

    Full version accounts for edge cases and invalid inputs.
    
    >>> link = Link(1, Link(2, Link(3)))
    >>> delete_full(link, 2).tolist()
    [1, 2]
    >>> delete_full(link, 0).tolist()
    [2]
    """
    if i == 0:  # if first link deleted, return second link
        return link.next

    head = link
    for _ in range(i - 1):  # otherwise, find the element before the new link
        assert link.next, "Index i beyond list length"
        link = link.next
    link.next = link.next.next
    return head


def intersection(link1, link2):
    """Compute the intersection of two linked lists.

    Return the result as a linked list.
  
    >>> link1 = Link(1, Link(2, Link(3)))
    >>> link2 = Link(4, Link(3, Link(2)))
    >>> intersection(link1, link2).tolist()
    [2, 3]
    """
    values = set()
    while link1 is not None:
        values.add(link1.value)
        link1 = link1.next
    link = None
    while link2 is not None:
        if link2.value in values:
            link = Link(link2.value, link)
        link2 = link2.next
    return link


"""
Solutions for "Kick Butt in Coding Interviews: Data Structures in Python"
by Alvin Wan

Take the course at https://skl.sh/
Find all course resources at https://alvinwan.com/datastructures101
"""


########
# TREE #
########


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


class Tree:
    """
    >>> tree = Tree(1, [
    ...   Tree(2, [
    ...     Tree(3),
    ...     Tree(4)
    ...   ]),
    ...   Tree(5, [
    ...     Tree(6),
    ...     Tree(7)
    ...   ]),
    ... ])
    >>> tree.value
    1
    >>> tree.branches[0].value
    2
    >>> tree.branches[0].branches[0].value
    3
    """
    def __init__(self, value, branches=()):
        self.value = value
        self.branches = list(branches)


#############
# EXERCISES #
#############


def bfs(tree):
    """Perform a breadth-first tree traversal.

    >>> tree = Tree(1, [
    ...     Tree(2, [Tree(3)]),
    ...     Tree(4),
    ... ])
    ...
    >>> bfs(tree)
    1
    2
    4
    3
    """
    buffer = Queue([tree])
    while buffer:
        current = buffer.dequeue()
        print(current.value)
        buffer.extend(current.branches)


def dfs(tree):
    """Perform a depth-first tree traversal.

    >>> tree = Tree(1, [
    ...     Tree(2, [Tree(3)]),
    ...     Tree(4, [Tree(5)]),
    ... ])
    ...
    >>> dfs(tree)
    1
    4
    5
    2
    3
    """
    buffer = Stack([tree])
    while buffer:
        current = buffer.pop()
        print(current.value)
        buffer.extend(current.branches)


def populate_parents(tree):
    """For every node in the tree, add a new attribute called 'parent'.
  
    This attribute will point to the node's parent in the tree.
  
    >>> tree = Tree(1, [
    ...   Tree(2, [
    ...     Tree(3),
    ...     Tree(4)
    ...   ])
    ... ])
    >>> populate_parents(tree)
    >>> leaf = tree.branches[0].branches[0]
    >>> leaf.value
    3
    >>> leaf.parent.value
    2
    >>> leaf.parent.parent.value
    1
    """
    buffer = Queue([tree])
    tree.parent = None
    while buffer:
        current = buffer.dequeue()
        for branch in current.branches:
            branch.parent = current
            buffer.append(branch)


def get_maximum(tree):
    """Get maximum value from an extremely wide but shallow tree.

	Consider what this means for your choice of traversal. What is the maximum 
    space complexity of breadth-first search? Of depth-first search?
	
	>>> tree = Tree(1, [
	...   Tree(2, [
	...     Tree(3),
	...     Tree(4),
	...     Tree(5),
	...   ]),
	...   Tree(5),
	...   Tree(6)
	... ])
	>>> get_maximum(tree)
	6
	"""
    buffer = Stack([tree])
    maximum = tree.value
    while buffer:
        current = buffer.pop()
        maximum = max(current.value, maximum)
        buffer.extend(current.branches)
    return maximum


def get_width(tree):
    """Get width of tree.
  
	The width is the maximum number of nodes at any given depth.
	
	>>> tree = Tree(1, [
	...   Tree(2, [
	...     Tree(3),
	...     Tree(4)
	...   ])
	... ])
	>>> get_width(tree)
	2
	>>> tree = Tree(1, [
	...   Tree(2, [
	...     Tree(3),
	...     Tree(4)
	...   ]),
	...   Tree(5),
	...   Tree(6)
	... ])
	>>> get_width(tree)
	3
	"""
    from collections import defaultdict # normally, this is at top of file

    buffer = Queue([(0, tree)])
    widths = defaultdict(int)
    while buffer:
        depth, current = buffer.dequeue()
        widths[depth] += 1
        for branch in current.branches:
            buffer.append((depth + 1, branch))
    return max(widths.values())

"""
Solutions for "Kick Butt in Coding Interviews: Data Structures in Python"
by Alvin Wan

Take the course at https://skl.sh/
Find all course resources at https://alvinwan.com/datastructures101
"""


###########
# MAPPING #
###########


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


class CappedStack(Stack):
    """Stack that limits all values to only 3 occurrences.
    
    >>> cstack = CappedStack()
    >>> for i in range(10):
    ...    cstack.push(1)
    >>> len(cstack)
    3
    >>> cstack.push(2)
    >>> len(cstack)
    4
    """
    def __init__(self, limit=3):
        self.limit = limit
        from collections import defaultdict  # normally at top of file
        self.counter = defaultdict(int)

    def push(self, value):
        if self.counter[value] < self.limit:
            self.counter[value] += 1
            super().push(value)

    def pop(self):
        value = super().pop()
        self.counter[value] -= 1
        return value


def unique(string):
    """Return a histogram of all the unique letters and their numbers of 
    occurrences.
    
    >>> unique('abababa')
    {'a': 4, 'b': 3}
    """
    counts = {}
    for letter in string:
        counts[letter] = counts.get(letter, 0) + 1
    return counts


def most_frequent(numbers):
    """Report the most frequent value in a list of whole numbers.

    Tip: Your first question (for the interviewer should be: What if there's a 
         tie?)

    In the event of a tie, report any of the numbers tied for the greatest 
    frequency.
    
    >>> most_frequent([1, 2, 3, 4, 3, 2])
    3
    >>> most_frequent([3, 3, 3, 1, 1, 1, 1])
    1
    >>> most_frequent([1, 2, 3])
    1
    """
    counter = {None: -1}
    greatest = None
    for value in numbers:
        counter[value] = counter.get(value, 0) + 1
        if counter[value] > counter[greatest]:
            greatest = value
    return greatest


def get_path_from_steps(steps):
    """Steps are formatted as (src, dst). Compute the complete path.
  
    You can assume there is only one path and that the one path is complete.
    There are no cycles, and no gaps.
  
    Print the sequence of steps in order, from first to last.
  
    >>> get_path_from_steps([(3, 2), (1, 3), (2, 5)])
    1 -> 3
    3 -> 2
    2 -> 5
    """
    forward = {}
    backward = {}

    for src, dst in steps:
        forward[src] = dst
        backward[dst] = src

    while src in backward:
        src = backward[src]

    while src in forward:
        print(f'{src} -> {forward[src]}')
        src = forward[src]


class LRUCache(dict):
    """Make a dictionary with a max size that operates as a least-recently-used
    cache.

    If the dictionary more keys than max size, drop the least-recently used key.
    A key is most-recently used if it was just assigned or was just accessed.
    
    >>> d = LRUCache()
    >>> d['a'] = 1
    >>> d['a']
    1
    >>> d['b'] = 2
    >>> d.most_recent.tolist()
    [2, 1]
    >>> d['a']
    1
    >>> d.most_recent.tolist()
    [1, 2]
    >>> d['c'] = 3  # b was least recently used
    >>> list(d.keys())
    ['a', 'c']
    """
    class DLink(Link):
        """Doubly-linked list. Used for least-recently-used problem.
        
        Each link in this linked list points both to the next *and to the
        previous links.
        """
        def __init__(self, key, value, next=None, prev=None):
            self.key = key
            self.value = value
            self.prev = prev
            self.next = next

    def __init__(self, size=2):
        super().__init__()
        self.most_recent = None
        self.least_recent = None
        self.size = size
        self.length = 0

    def __getitem__(self, key):
        value = super().__getitem__(key).value
        self.__setitem__(key, value)  # re-assign to make most recent
        return value

    def __setitem__(self, key, value):
        if key in self:
            self.pop(key)
        super().__setitem__(key, LRUCache.DLink(key, value))
        self.make_most_recent(key)
        self.length += 1

        if self.length > self.size:
            self.pop(self.least_recent.key)

    def make_most_recent(self, key):
        link = super().__getitem__(key)
        link.next = self.most_recent
        self.most_recent = link

        if self.most_recent.next is not None:
            self.most_recent.next.prev = self.most_recent
        if self.least_recent is None:
            self.least_recent = self.most_recent

    def pop(self, key):
        link = super().pop(key)
        if link.prev is None:
            self.most_recent = None
        else:
            link.prev.next = link.next
        if self.least_recent == link:
            self.least_recent = self.least_recent.prev
        self.length -= 1
        return link

"""
Solutions for "Kick Butt in Coding Interviews: Data Structures in Python"
by Alvin Wan

Take the course at https://skl.sh/
Find all course resources at https://alvinwan.com/datastructures101
"""


############
# SEQUENCE #
############


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


class QueueViaStack:
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
    def __init__(self, iterable):
        self.stack = Stack(iterable)

    def enqueue(self, value):
        self.stack.push(value)

    def dequeue(self):
        # empty original stack into new stack
        stack = Stack()
        while len(self.stack):
            stack.push(self.stack.pop())

        value = stack.pop()

        # empty new stack back into original stack
        while len(stack):
            self.stack.push(stack.pop())

        return value


class StackViaQueue:
    """
    >>> stack = StackViaQueue([1, 2, 3])
	>>> stack.push(4)
	>>> stack.pop()
	4
    """
    def __init__(self, iterable):
        self.queue = Queue(iterable)

    def push(self, value):
        self.queue.enqueue(value)

    def pop(self):
        # empty n-1 items in original queue into new Queue
        queue = Queue()
        while len(self.queue) > 1:
            queue.enqueue(self.queue.dequeue())

        value = self.queue.dequeue()
        self.queue = queue  # shortcut, since all items are in the right order

        return value


def print_baba(k):
    """Print all combinations of the letters a and b, of length k or less

    >>> print_baba(2)
    aa
    ab
    ba
    bb
    >>> print_baba(3)
    aaa
    aab
    aba
    abb
    baa
    bab
    bba
    bbb
    """
    queue = Queue([''])
    for i in range(2**k - 1):
        letter = queue.dequeue()
        queue.enqueue(letter + 'a')
        queue.enqueue(letter + 'b')

    for _ in range(2**k):
        print(queue.dequeue())


def print_baba_no_math(k):
    """Print all combinations of the letters a and b, of length k or less

    >>> print_baba(2)
    aa
    ab
    ba
    bb
    >>> print_baba(3)
    aaa
    aab
    aba
    abb
    baa
    bab
    bba
    bbb
    """
    queue = Queue([''])
    while len(queue):
        word = queue.dequeue()
        if len(word) == k:
            print(word)
        if len(word) < k:
            queue.enqueue(word + 'a')
            queue.enqueue(word + 'b')


def print_stairs(k):
    """Print number of ways to climb k stairs, if you can take 1 or 2 steps at 
    a time.

    >>> print_stairs(1)
    1
    >>> print_stairs(2)
    2
    >>> print_stairs(3)
    3
    >>> print_stairs(10)
    89
    """
    queue = Queue([0])
    num_ways = 0
    while len(queue):
        stairs = queue.dequeue()
        if stairs == k:
            num_ways += 1
        if stairs < k:
            queue.enqueue(stairs + 1)
            queue.enqueue(stairs + 2)
    return num_ways


def is_valid_parentheses(string):
    """Check if the provided string contains matching parentheses

 	Hint: Use a stack. You can assume there are only starting or closing 
          parentheses in the string.
  	Tip: In an interview, ask if the string could contain other characters. For
         example, numbers.
  
    >>> is_valid_parentheses('()(()()')
    False
    >>> is_valid_parentheses('((())())')
    True
    >>> is_valid_parentheses(')')
    False
    >>> is_valid_parentheses(')(')
    False
    """
    stack = Stack()
    for letter in string:
        if letter == '(':
            stack.push(letter)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0


def is_valid_parentheses_wo_stack(string):
    """Check if the provided string contains matching parentheses

 	This solution does not use a stack. Oops! 
  
    >>> is_valid_parentheses_wo_stack('()(()()')
    False
    >>> is_valid_parentheses_wo_stack('((())())')
    True
    >>> is_valid_parentheses_wo_stack(')')
    False
    >>> is_valid_parentheses_wo_stack(')(')
    False
    """
    depth = 0
    for letter in string:
        if letter == '(':
            depth += 1
        elif letter == ')':
            depth -= 1
            if depth < 0:
                return False
    return depth == 0


def is_valid_grouping(string):
    """Check if the provided string contains matching parentheses and matching
    brackets.
    
    >>> is_valid_grouping('()[()()]')
    True
    >>> is_valid_grouping('()[()()')
    False
    >>> is_valid_grouping('[(])')
    False
    >>> is_valid_grouping('(([])')
    False
    """
    stack = Stack()
    for letter in string:
        if letter in ('[', '('):
            stack.push(letter)
        elif letter == ')':
            if stack.pop() != '(':
                return False
        elif letter == ']':
            if stack.pop() != '[':
                return False
    return len(stack) == 0


#########
# BONUS #
#########


def print_binary_numbers(k):
    """Print all binary numbers less than or equal to the value k
  
    >>> print_binary_numbers(1)
    1
    >>> print_binary_numbers(3)
    1
    10
    11
    >>> print_binary_numbers(5)
    1
    10
    11
    100
    101
    """
    queue = Queue(['1'])
    for i in range(k):
        value = queue.dequeue()
        queue.enqueue(value + '0')
        queue.enqueue(value + '1')
        print(value)


def print_possible_coins_challenge(k):
    """Print all possible combinations of pennies, nickels and dimes it takes to
    reach a value.

    For each combination, print a list of 3 numbers:
    - Number of pennies
    - Number of nickels
    - Number of dimes
    
    For example, `[1, 2, 3]` would mean 1 penny, 2 nickels, and 3 dimes.
  
    >>> print_possible_coins_challenge(5)
    [5, 0, 0]
    [0, 1, 0]
    >>> print_possible_coins_challenge(10)
    [10, 0, 0]
    [5, 1, 0]
    [0, 2, 0]
    [0, 0, 1]
    >>> print_possible_coins_challenge(20)
    [20, 0, 0]
    [15, 1, 0]
    [10, 2, 0]
    [5, 3, 0]
    [10, 0, 1]
    [0, 4, 0]
    [5, 1, 1]
    [0, 2, 1]
    [0, 0, 2]
    """
    queue = Queue([(k, 0, 0)])
    seen = set()
    while len(queue):
        p, n, d = queue.dequeue()
        if (p, n, d) not in seen:
            print([p, n, d])
            seen.add((p, n, d))
        if p >= 5:
            queue.enqueue([p - 5, n + 1, d])
        if n >= 2:
            queue.enqueue([p, n - 2, d + 1])


