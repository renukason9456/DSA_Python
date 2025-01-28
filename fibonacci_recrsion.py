def fibonacci(n):
    # Base case: return n if n is 0 or 1
    if n <= 1:
        return n
    # Recursive case: sum of the two previous Fibonacci numbers
    return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage:
n = 5  # Find the 5th Fibonacci number
print(f"The {n}th Fibonacci number is: {fibonacci(n)}")
