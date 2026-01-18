numbers = range(1, 6)  # Creates a list: [1, 2, 3, 4, 5]
print("Using range():", list(numbers))  # Prints the full list
print("Memory used by range:", numbers.__sizeof__())  # Shows memory size

numbers_gen = range(1, 6)  # Acts like a generator in Python 3
print("Using xrange-like:", list(numbers_gen))  # Prints: [1, 2, 3, 4, 5]
print("Memory used by xrange-like:", numbers_gen.__sizeof__())  # Less memory
