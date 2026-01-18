# Define a generator function
def even_numbers():
    num = 0
    while num <= 10:
        yield num  # Pauses here and returns num, then resumes next time
        num += 2

# Use the generator
evens = even_numbers()  # This doesn't run the function yet

# Get values one by one
print(next(evens))  # Output: 0
print(next(evens))  # Output: 2
print(next(evens))  # Output: 4
# ... and so on

# Or loop through all
for even in even_numbers():
    print(even)
# Output: 0 2 4 6 8 10
