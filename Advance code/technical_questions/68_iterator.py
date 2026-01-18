# Create a list (iterable)
my_list = [1, 2, 3]

# Turn list into an iterator
my_iterator = iter(my_list)

# Get elements one by one
print(next(my_iterator))  # Output: 1
print(next(my_iterator))  # Output: 2
print(next(my_iterator))  # Output: 3

# If you call next() again, it raises StopIteration (no more elements)
