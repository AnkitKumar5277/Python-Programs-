# ----- LIST EXAMPLES -----
# Lists are mutable, ordered collections that can store different data types
print("=== List Examples ===")

# Creating a list
my_list = [1, 2, 3, 4, 5]
print("Original List:", my_list)

# Mixed data types in a list
mixed_list = [1, "two", 3.0, [4,5,6]]
print("mixed list:", mixed_list)

# Accessing elements using indexing (starts from 0)
print("first element (index 0):", my_list[0])
print("Third element (index 2):", my_list[2])  # Outputs 3

# Negative indexing (starts from -1 for last element)
print("Last element (index -1):", my_list[-1])  # Outputs 5

# Modifying a list (mutable)
my_list.append(7)
print("After changing index 1:", my_list)  # Outputs [1, 6, 3, 4, 5]

# List Methods
# .append() - Adds an element to the end
my_list.append(7)
print("After appending 7:", my_list)  # Outputs [1, 6, 3, 4, 5, 7]

my_list.insert(2, 10)  # Insert 10 at index 2
print("After inserting 10 at index 2:", my_list)  # Outputs [1, 6, 10, 3, 4, 5, 7]

# .pop(index) - Removes and returns element at index
popped = my_list.pop(2)  # Removes element at index 2
print("After popping index 2 (popped value: {}):".format(popped), my_list)  # Outputs [1, 6, 3, 4, 5, 7]

# .remove(element) - Removes first occurrence of element
my_list.remove(5)
print("After removing 6:", my_list)  # Outputs [1, 3, 4, 5, 7]

# .sort() - Sorts the list
my_list.sort()
print("After sorting:", my_list)  # Outputs [1, 3, 4, 5, 7]

# .reverse() - Reverses the list
my_list.reverse()
print("After reversing:", my_list)  # Outputs [7, 5, 4, 3, 1]

# ----- TUPLE EXAMPLES -----
# Tuples are immutable, ordered collections
print("\n=== Tuple Examples ===")

# Creating a tuple
my_tuple = (1, 2, 3, "four")
print("Original Tuple:", my_tuple)

# Empty tuple and single-element tuple
empty_tuple = ()
single_tuple = (1,)  # Comma is needed for single-element tuple
print("Empty Tuple:", empty_tuple)
print("Single-element Tuple:", single_tuple)

# Accessing elements using indexing
print("First element (index 0):", my_tuple[0])  # Outputs 1
print("Last element (index 3):", my_tuple[3])  # Outputs 'four'

# Negative indexing
print("Last element (index -1):", my_tuple[-1])  # Outputs 'four'

# Tuple Methods
# .count(value) - Counts occurrences of value
print("Count of 2 in tuple:", my_tuple.count(2))  # Outputs 1

# .index(value) - Returns index of first occurrence
print("Index of 'four' in tuple:", my_tuple.index("four"))  # Outputs 3

# ----- LIST vs TUPLE EXAMPLE -----
print("\n=== List vs Tuple ===")
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)

# Modifying list (works)
my_list.append(4)
my_list[1] = 5
print("Modified List:", my_list)  # Outputs [1, 5, 3, 4]

print("Tuple remains unchanged:", my_tuple)  # Outputs (1, 2, 3)



