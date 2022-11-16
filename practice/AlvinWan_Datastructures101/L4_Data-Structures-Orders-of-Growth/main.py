"""
Exercises for "Kick Butt in Coding Interviews: Data Structures in Python"
by Alvin Wan

Take the course at https://skl.sh/
Find all course resources at https://alvinwan.com/datastructures101

RUN USING COMMAND: "python -m doctest main.py"
"""


#############
# EXERCISES #
#############


def runtime_basic1(N):
    """What is the runtime complexity of the following, as a function of N?"""
    for i in range(N):
        print(i)
    pass  # YOUR ANSWER HERE    O(n)


def runtime_basic2(N):
    """What is the runtime complexity of the following, as a function of N?"""
    for i in range(N):
        for j in range(N):
            print(i, j)
    pass  # YOUR ANSWER HERE    O(n^2)


def runtime_basic3(N):
    """What is the runtime complexity of the following, as a function of N?"""
    i = N
    while i > 1:
        i //= 2
        print(i)
    pass  # YOUR ANSWER HERE    O(logn)


def runtime_tricky1(N):
    """How many times is print called, as a function of N?

    Notice the if statement! How does that affect runtime complexity, if at all?
    """
    for i in range(N):
        for j in range(N):
            if i == j:
                print(i, j)
    pass  # YOUR ANSWER HERE    O(n) - print only called once per pair of loops


def runtime_tricky2(N):
    """How many times is print called, as a function of N?

    Notice the inner loop only counts up to i! How does that affect runtime
    complexity, if at all?
    """
    for i in range(N):
        for j in range(i):
            print(i, j)
    pass  # YOUR ANSWER HERE    Still O(n^2) - runtime slower, but runtime complexity still of same order

