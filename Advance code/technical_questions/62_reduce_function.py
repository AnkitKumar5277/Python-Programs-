from functools import reduce

# Example 1: Sum all numbers in a list
numbers = [1, 2, 3, 4]
result = reduce(lambda x, y: x + y, numbers)
print(result)  # Output: 10 (1+2+3+4)

# Example 2: Multiply all numbers in a list
result = reduce(lambda x, y: x * y, numbers)
print(result)  # Output: 24 (1*2*3*4)

