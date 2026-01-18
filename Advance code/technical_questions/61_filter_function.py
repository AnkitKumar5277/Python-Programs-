# Example: Filter even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# Define a function to check if a number is even
def is_even(num):
    return num % 2 == 0

# Use filter() to get only even numbers
even_numbers = list(filter(is_even, numbers))

print(even_numbers)  # Output: [2, 4, 6, 8]
