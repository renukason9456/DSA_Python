'''Base Cases:
Base cases are the conditions that terminate a recursive process. 
They define the simplest possible scenarios for a problem, for which the answer is directly known. 
Without base cases, recursion can lead to infinite loops.
Example-  In calculating the factorial of a number:'''
def fact(num):
    if num == 0:  # Base case
        return 1
    return num * fact(num - 1)


print(fact(6))
print(fact(0))
