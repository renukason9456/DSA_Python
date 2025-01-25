'''Recursion Tree:
A recursion tree is a visual representation of how recursive calls are made and executed. It helps in understanding the flow of recursive algorithms and their time complexity.

Steps to Create a Recursion Tree:

Start with the initial problem at the root.
Break the problem into subproblems (recursive calls).
Represent each subproblem as a child node.
Continue expanding nodes until you reach the base cases.'''


def fib(n):
    if n <= 1:  # Base case
        return n
    return fib(n - 1) + fib(n - 2)


print(fib(4))
