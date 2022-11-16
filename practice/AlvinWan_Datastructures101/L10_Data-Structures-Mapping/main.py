"""
Exercises for "Kick Butt in Coding Interviews: Data Structures in Python"
by Alvin Wan

Take the course at https://skl.sh/
Find all course resources at https://alvinwan.com/datastructures101

RUN USING: "python -m doctest main.py"
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
    '''
    ALGORITHM: create a hashmap for list of values in the stack. In the hashmap, store the number of occurences currently in the stack.
        When a new value is pushed, add 1 the the index stored in the stack. (assuming it does not exceed the limit)
        When a value is popped, remove 1 from the index stored for that value in the stack
        Map will be implemented using Python dictionary

    COMPLEXITY:
        runtime complexity is O(1), as stack length does not impact speed of popping / pushing
            NOTE: complexity is that of the original algorithm, pushing / popping stacks is O(1) therefore this algorithm is too
        memory complexity is O(n), as a hashmap of size n is required to store occurances. (assuming worst case scenario)
            NOTE: complexity is actually O(k), where k is the number of unique values
    '''

    '''
    NOTE: Solution presented in lesson uses custom dict library that returns 0 instead of KeyError when accessing a dict key that does not exist
        "from collections import defaultdict"
    '''
    def __init__(self, limit=3):
        self.limit = limit
        self.count = {}
        pass  # YOUR ANSWER HERE

    def push(self, value):
        # YOUR ANSWER HERE
        if self.count.get(value) is not None:
            if self.count.get(value) < self.limit:
                self.count[value] += 1          # if value exists in dictionary, decrement
            else:
                return                          # if value exists and exceeds limit, return without pushing
        else:
            self.count[value] = 1       # if value does not exist in dictionary, add it
        super().push(value)

    def pop(self):
        # YOUR ANSWER HERE
        value = super().pop()
        self.count[value] -= 1
        return value


def unique(string):
    """Return a histogram of all the unique letters and their numbers of 
    occurrences.
    
    >>> unique('abababa')
    {'a': 4, 'b': 3}
    """
    '''
    ALGORITHM: Use a dictionary to store letters and numbers in the string. If value has been entered before, increment its count in the dict,
        if value has not been seen before, enter it into the dict as a new key.
    
    COMPLEXITY:
        Runtime complexity is O(2n), because entering into a hashmap is constant time O(1) and we are fetching + writing new value
        Memory complexity is O(k) where k is unique characters in the string. 
            Unlike previous example, this is bounded by number of unique characters rather than number of unique values. 
            With a limited number of available characters, this is a significantly lower limit than possible numbers.
    '''
    # YOUR ANSWER HERE
    dict = {}
    for letter in string:
        if dict.get(letter) is None:
            dict[letter] = 1
        else:
            dict[letter] += 1
    return dict


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
    '''
    ALGORITHM: create a hashmap/dictionary as a counter, storing the most frequent value while adding to the counter.    
    COMPLEXITY: 
        runtime complexity is O(n) as we have to iterate through the list and perform O(1) to add values to the dictionary
        memory complexity is O(n) (worst case) where each entry in the list is a unique value
    '''
    # YOUR ANSWER HERE
    counter = {}            #NOTE: Solution chooses to initialize counter = {None: -1} to avoid initial if statement checking for mf == None
    mf = None                 # most frequent value is None until a number is found
    for num in numbers:
        if mf is None:
            mf = num            # most frequent initialise to first number

        if num in counter:
            counter[num] += 1
        else:
            counter[num] = 1

        if counter[num] > counter[mf]:
            mf = num

    return mf


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
    '''
    ALGORITHM: path from src -> dst is always complete. 
        iterate through list, looking for 'src' and 'dst' place 'src' at the start and 'dst' at the end. 
            Then, adjust 'src' and 'dst' to be the points connecting to 'src' and 'dst'
            continue iterating until list is ordered.
    COMPLEXITY:
        runtime complexity is O(0.5n^2), will likely need to iterate through the list n number of times, removing one (maybe 2?) elements each time.
     
    FALSE (can do better): 
    Algorithm: Iterate through list to build a hashmap from src:dst and a second one from dst:src.
            Then use the hashmaps to find the src point that does't map to a previous dst to get the absolute src
    Complexity:
        Runtime complexity is linear O(2n)(?)  as we have to 
        Memory complexity is linear O(2n)(?) as we have to build 2 seperate hashmaps to map back to front
    '''
    # YOUR ANSWER HERE
    src2dst = {}
    dst2src = {}
    src = None
    for step in steps:
        p1 = step[0]
        p2 = step[1]
        src2dst[p1] = p2
        dst2src[p2] = p1
    
    dst = p2
    while src is None:      #iterate to get absolute src
        if dst in dst2src:
            dst = dst2src.get(dst)
        else:
            src = dst
        # if dst2src.get(dst) is None:         #dst always defined from previous loop, which value is selected doesn't matter
        #     src = dst                
        # else:
        #     src = dst2src.get(dst)

    dst = src2dst.get(src)          # get initial dst from absolute src
    while src in src2dst:          # keep iterating as long as the previous destination is the source to the next
        print(src, "->", dst)
        src = dst
        dst = src2dst.get(src)

    # SOLUTION: conceptually the same, but cleaner code
    # forwards = {}
    # backwards = {}
    # for src,dst in steps:
    #     forwards[src] = dst
    #     backwards[dst] = src

    # src = steps[0][0]
    # while src in backwards:
    #     src = backwards[src]

    # while src in forwards:
    #     print(f'{src} -> {forwards[src]}')
    #     src = forwards[src]
        





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
    # YOUR ANSWER HERE
    # NOTE: exercise intended to be discussed algorithmically. see solutions document for code.
    # BONUS: write this into code
    '''
    ALGORITHM: store data in a dictionary, and retain keys in a linked list ordered in terms of usage 
        When a key is used, swap it's order in the linked list by swapping addresses.
        When a new key is entered, place it at the front of the LRU list. 
        If size is exceeded, pop the last node from the list and remove it from the dictionary.
    SOLUTION:
        Store key entries in a doubly-linked list
            doubly linked list stores addresses in both directions (ie. 1 <-> 2 <-> 3 instead of 1 -> 2 -> 3)
        NOTE: not entirely sure why a doubly-linked list is necessary - attempt coding this later to figure out why

    COMPLEXITY:
        Runtime: Complexity is Linear O(n), as it will be necessary to navigate a linked list when entering a key. 
                (In this case n will be capped to a constant k. Would this be then considered O(1)?)
        Memory: Complexity is Linear O(n), as every key will be stored. 
    SOLUTION:
        Runtime: 
            - accessing a value will be O(1)
            - insertion/deletion will be O(1)
            - updating hashmap + key order will be O(1)

    Pseudo code:
        def __getitem__(self, key):
            self.make_most_recent(key)

        def __setitem__(self, key):
            self.make_most_recent(key)

        def make_most_recent(self, key):
            *remove item from list*
            *reinsert it into beginning*
    '''



