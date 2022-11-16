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
    # YOUR ANSWER HERE
    '''
    HINT: Will need to use a stack or a queue.
    what example tree looks like:
            1
           / \
          2   4
         / 
        3

    ALGORITHM:  Start at the root node. Check the node (in this case, print) the value. Check the connected branches.
                Place each branch in a queue of 'nodes to inspect'
                Grab next node to inspect from the queue, checking (printing) again for connected branches and adding these nodes to the queue
                Continue inspecting nodes until the queue is empty.
                *This should work for dfs too, if using a stack instead of a queue
    Complexity:
        Runtime: complexity is O(n), as every node is iterated through
        Memory: complexity is O(n) (?), as up to n nodes are stored in the queue. 
                While nodes will leave the queue, a sufficiently lare tree will have ~n nodes in the queue
    '''
    queue = Queue([tree])
    while len(queue):
        node = queue.dequeue()
        print(node.value)
        for branch in node.branches:
            queue.enqueue(branch)




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
    # YOUR ANSWER HERE
    '''
    branch view:
            1
           /  \
          2    4
        /     /
       3     5
    ALGORITHM:
        same algorithm for dfs as for bfs, except a stack is used to store 'nodes to inspect' instead of a queue
        same complexity as bfs (O(n) runtime and memory)
    '''
    stack = Stack([tree])
    while len(stack):
        node = stack.pop()
        print(node.value)
        for branch in node.branches:
            stack.push(branch)

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
    # YOUR ANSWER HERE
    '''
            1
           / \
          2
         / \
        3   4

    ALGORITHM: do a dfs / bfs tree search (shouldn't matter? I'll go with dfs)
            in addition to a stack of branch nodes, create a seperate stack containing 'parents'
            push the current node to the 'parent' stack every time a branch is pushed
            when popping from the 'branch' stack, pop from the 'parent' stack and asign the parent as a class variable
    COMPLEXITY:
        runtime: O(n), as we have to navigate through every node in the tree
        memory: O(2n), as we creata a seperate stack for parents to double memory requirement from a simpple dfs
    '''
    branch_stack = Stack([tree])
    parent_stack = Stack([None])
    while len(branch_stack):
        node = branch_stack.pop()
        node.parent = parent_stack.pop()
        for branch in node.branches:
            branch_stack.push(branch)
            parent_stack.push(node)

    # # SOLUTION: conceptually the same, cleaner code. 
    # # Solution doesn't require a second stack, lowering the memory complexity to be the exact same as dfs/bfs
    # if tree is None:
    #     return
    # stack = Stack([tree])
    # while stack:
    #     current = stack.pop()
    #     for branch in current.branches:
    #         branch.parent = current
    #         stack.push(branch)



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
    # YOUR ANSWER HERE
    '''
    Wide but shallow tree implies depth-first search would be optimal, as dfs will result a smaller stack compared to the queue size of bfs
        - if the tree is wide, penetrating to a leaf will require a relatively small stack size (stack has to contain the full depth, which is low)
        - bfs for a wide tree will require a large queue size to contain the entirety of the tree width
    ALGORITHM:
        perform dfs inspecting node elements. Store the maximum value. If the iinspected node has a larger value than the current maximum, replace it
    Complexity:
        runtime: O(n) complexity because we need to iterate through every node
        memory: O(d) where d is depth, complexity is correlated to depth. 
    '''
    next = Stack([tree])
    largest = tree.value        # initialize to root value 
    while len(next):
        current = next.pop()
        if (current.value > largest):
            largest = current.value
        for branch in current.branches:
            next.append(branch)
    return largest



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
    # YOUR ANSWER HERE
    '''
               1
              /
             2 
            / \
           3   4
    
    ALGORITHM: when navigating the tree, we can assign a node a 'depth' variable while placing it in the stack/queue equal to the parent depth + 1
            when a node is then taken from the stack/queue, its 'depth' variable is inspected and added to a counter.
            counter best stored as a hashmap for given depth
    COMPLEXITY:
        runtime: O(2n) complexity as it is necessary to navigate through each node. We then need to navigate and compare the hashmap
        memory complexity: O(2n), as we need to add a variable to each node and additionally createa hashmap potentially size n
    '''
    count = {}
    max_width = 0
    queue = Queue([tree])
    tree.depth = 0
    depth = tree.depth          # creating seperate depth variable lets us iterate later
    while len(queue):
        current = queue.dequeue()
        depth = current.depth
        if count.get(depth) is not None:
            count[depth] += 1
        else:
            count[depth] = 1

        # print("depth =", depth, "count = ", count[depth])
        for branch in current.branches:
            branch.depth = depth + 1
            queue.enqueue(branch)

    for level in range(depth + 1):          # because search is bfs, depth = maximum depth               
        # print("level =", level, "width = ", count[level])
        if max_width < count.get(level):     # count should never be None from 0 -> depth, otherwise it wouldnt be a tree
            max_width = count.get(level)
    return max_width

    # # SOLUTION: more elegant, and does not create unwanted class variables 
    # from collections import defaultdict

    # buffer = Queue([(0, tree)])
    # widths = defaultdict(int)
    # while buffer:
    #     depth, current = buffer.dequeue()
    #     widths[depth] += 1
    #     for branch in current.branches:
    #         buffer.enqueue((depth + 1, branch))
    # return max(widths.values())