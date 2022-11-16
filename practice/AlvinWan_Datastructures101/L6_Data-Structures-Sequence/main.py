"""
Exercises for "Kick Butt in Coding Interviews: Data Structures in Python"
by Alvin Wan

Take the course at https://skl.sh/
Find all course resources at https://alvinwan.com/datastructures101

RUN USING COMMAND: "python -m doctest main.py"
"""


from audioop import add
from calendar import c
import queue


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
    '''
    create a "row" of stacks, passing data from one stack to the next ?
        false - use 2 stacks. when dequeuing, pop everything but the last from stack 1 -> 2, and then pop it back from 2->1 to refill the original stack in the original order
    runtime complexity: O(n)  ?
        Correct - popping and placing items in a stack is O(1), for a queue size n, we would need to do this ~2n
        memory complexity = O(n)
        
    '''
    # ORIGINAL ATTEMPT

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

    # SOLUTION

    # def __init__(self, iterable):
    #     self.stack = Stack(iterable)

    # def enqueue(self, value):
    #     self.stack.push(value)
    
    # def dequeue(self):
    #     # Empty original stack into new stack
    #     stack = Stack()
    #     while len(self.stack):
    #         stack.push(self.stack.pop())

    #     value = stack.pop()

    #     # Empty new stack back into original old stack
    #     while len(stack):
    #         self.stack.push(stack.pop())

    #     return value




class StackViaQueue:
    """
    >>> stack = StackViaQueue([1, 2, 3])
	>>> stack.push(4)
	>>> stack.pop()
	4
    >>> stack.pop()
    3
    >>> stack.pop()
    2
    """
    # YOUR ANSWER HERE
    '''
    To implement a stack using queues, need 2 queues
    - a 'main' queue to hold all input data, and a secondary queue to temporarily place data while fetching a specific value.
    - to 'pop' the stack, queue every value except for the last into the 2nd queue and dequeue the final value.
    - this should have O(n) runtime complexity and O(n) memory complexity
    '''
    # INITAL ATTEMPT
    def __init__(self, iterable):
        self.q = Queue(iterable)
    
    def push(self, value):
        self.q.enqueue(value)

    def pop(self):
        temp = Queue([])
        while len(self.q) > 1:
            temp.enqueue(self.q.dequeue())
        output = self.q.dequeue()
        self.q = temp
        return output

    # SOLUTION: almost exactly the same! :)

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
    # YOUR ANSWER HERE
    '''
    Algorithm: create a stack containing [a,b] for each digit, and iterate through each digit fetching from the stack (?)
        - FALSE: recursively enqueue the start of the starting queue with 'a' and 'b' added
            -> [''] -> [a, b] -> [b, aa, ab] -> [aa, ab, ba, bb] -> [ab, ba, bb, aaa, aab] -> [ba, bb, aaa, aab, aba, abb]
    Complexity:
        - runtime complexity: o(2^n) (generating every combination of a and b is akin to binary count)
            - CORRECT ...mostly. generating baba length k requires 2^k + 2^(k-1) + ... + 2^1 + 2^0 computations
                - this is because you generate all the previous value's solutions to generate the next 'digit'
        - memory complexity: o(2^n) (needing to store every combination is akin to storing every binary combination of length n)
    '''

    # INITIAL ATTEMPT   - 
    baba = Queue([""])
    for i in range(2**k -1):      #iterate through 
        str = baba.dequeue()
        baba.enqueue(str + "a")
        baba.enqueue(str + "b")
    
    for i in range(len(baba)):
        print(baba.dequeue())

    # SOLUTION
    # queue = Queue([''])
    # while len(queue):   #while there is something in the queue...
    #     word = queue.dequeue()      # fetch the next word in the queue
    #     if len(word) == k:          # if the word is k digits long, print the word
    #         print(word)
    #     if len(word) < k:           # if the word is too short, enqueue all possible 1-digit extensions of the word
    #         queue.enqueue(word + "a")
    #         queue.enqueue(word + "b")



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
    # YOUR ANSWER HERE
    '''
    Algorithm:
    similar to how print_baba() builds up ways to print "a" and "b", its possible to climb stairs by recursively adding 1 or 2 to previous number (if the sum is <= k)
    build up a queue by continuously adding values. if the sum reaches k, add it to +1 combinations, if the sum > k, discard the possibility
    [0] -> [0+1, 0+2] = [1, 2] -> [2, 1+1, 1+2] = [2, 2, 3] -> [2, 3, 2+1, 2+2] = [2, 3, 3, 4] ....
        - (correct answer!)
    Complexity: instructed to skip (too difficult for now)
    '''

    # INITIAL ATTEMPT
    queue = Queue([0])
    combinations = 0
    while len(queue):
        stair = queue.dequeue()
        if stair == k:
            combinations += 1
        if stair < k:
            queue.enqueue(stair + 1)
            queue.enqueue(stair + 2)
        # if stair > k (from adding 2, solution is discarded as this is not a valid combination)
    return combinations

    # SOLUTION: almost exactly the same! :)



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
    # YOUR ANSWER HERE
    '''
    Algorithm: create a stack out of string input. +1 if opening parentheses, -1 if closing.
        -> if sum at the end == 0, and sum was never negative at any point, pass the test
        -> (start the stack from the back, so poping the value reads it forwards?)
    Answer: FALSE (not actually false imo, but do it this way instead)
        - add a '(' to a stack on opening a parenthesis, pop one off when closing a parenthesis ')'
    
    Complexity:
        runtime: o(n) - problem solvable when iterating through string lenght n once
        memory: o(n) - likely wont ever reach n if you actually close parentheses, but still
    '''
    # INITIAL ATTEMPT
    stack = Stack([])
    for char in string:
        if char == '(':
            stack.push(char)
        if char == ')':
            try:
                stack.pop()
            except IndexError:  #if we're trying to pop an empty stack, return false
                return False
    if len(stack) == 0:
        return True
    else:
        return False

    #SOLUTION (very similar!):
    # stack = Stack([])
    # for letter in string:
    #     if letter == '(':
    #         stack.push(letter)
    #     else:                           #assumes any letter that is not '(' is a closing parenthesis
    #         if len(stack) == 0:
    #             return False
    #         stack.pop()
    # return len(stack) == 0

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
    # YOUR ANSWER HERE
    '''
    Algorithm: create a stack out of inputs similar to the previous exercise is_valid_parenthesis(), but add opening parenthesis AND brackets to the stack
        - when trying to pop a stack on closing a grouping, make sure brackets pop brackets, and parentheses pop other parentheses. If NOT, grouping is not valid

    Complexity:
        runtime: o(n)
        memory: o(n)
    '''

    # INITIAL ATTEMPT
    stack = Stack([])
    for char in string:
        if char == '(' or char == '[':
            stack.push(char)
        if char == ']':
            if not (len(stack) > 0 and stack.pop() == '['):         #stack must not be empty, and must pop a bracket    
                return False
        if char == ')':
            if not (len(stack) > 0 and stack.pop() == '('):        #stack must not be empty, and must pop a parenthesis
                return False
    return len(stack) == 0      # once everything is added and popped, the stack should be empty

    # SOLUTION (note: solution is a 'worse' answer, as it does not account for popping an empty stack...)
    # stack = Stack()
    # for letter in string:
    #     if letter in ['(', '[']:
    #         stack.push(letter)
    #     elif letter == ')':
    #         if stack.pop() != '(':
    #             return False
    #     elif letter == ']':
    #         if stack.pop() != '[':
    #             return False
    # return len(stack) == 0

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
    # YOUR ANSWER HERE
    '''
    Algorithm: similar exercise to print_baba(). use a queue to build the binary values while iterating

    Complexity:
        runtime: o(2^n)
        memory: o(2^n)
    '''
    # INITIAL ATTEMPT
    queue = Queue(["1"])
    for i in range(k):
        num = queue.dequeue()
        print(num)
        queue.enqueue(num + "0")
        queue.enqueue(num + "1")
    
    # SOLUTION: amost exact same! :)



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
    # YOUR ANSWER HERE
    '''
    Algorithm: knowing k pennies is always k cents, build the algorithm starting at [k, 0, 0], queueing variations from this using nickels and dimes 
        - when it is possible to 'condense' currency, add these variations into the queue

    Complexity:
    because we are building and storing permutations, complexity scales extremely quickly (i think?)
    runtime: o(n!) 
    memory:  o(n!)
    '''

    #INITIAL ATTEMPT: nearly works, but prints duplicate combinations

    # queue = Queue([[k,0,0]])
    # while len(queue):
    #     money = queue.dequeue()
    #     if money[0] - 5 >= 0:   # if its possible to condense pennies -> nickels...
    #         add_nickel = money.copy()  # dont want to overwrite money
    #         add_nickel[0] -= 5
    #         add_nickel[1] += 1
    #         queue.enqueue(add_nickel)  # fill new combination into the queue
    #     if money[1] - 2 >= 0:   # if its possible to condense nickels -> dimes...
    #         add_dime = money.copy()
    #         add_dime[1] -= 2
    #         add_dime[2] += 1
    #         queue.enqueue(add_dime)     # fill new combination into the queue
    #     print(money)
        # print(queue)              #debugging

    # SOLUTION: Similar, makes use of sets to rule out duplicates
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

