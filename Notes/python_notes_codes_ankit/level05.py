# Dictionary Examples
# A dictionary stores key-value pairs, accessed by keys, not indices
print("=== Dictionary Examples ===")

# Creating a dictionary
my_dict = {'apple': 2, 'banana': 3, 'orange': 1}
print("Initial dictionary:", my_dict)

# Accessing a value using a key
print("Value of 'banana':", my_dict['banana'])  # Output: 3

# Adding a new key-value pair
my_dict['pear'] = 4
print("After adding 'pear':", my_dict)

# Updating an existing value
my_dict['banana'] = 5
print("after updating 'banana': ", my_dict)

# Deleting a key-value pair using del
del my_dict['orange']
print("after deleting 'orange': ", my_dict)

# Deleting a key-value pair using pop (returns the value)
popped_value = my_dict.pop('apple')
print("after popping 'apple':",my_dict, "popped value:",popped_value)

# Nested dictionary
nested_dict = {
    'key1': 'value1',
    'name': {'ankit':'kumar'}
}
print("nested dictionary access: ", nested_dict['name']['ankit'])

# Empty dictionary
empty_dict = {}
print("Empty dictionary:", empty_dict)

# Dictionary methods
marks = {'Ankit': 95, 'Rahul': 85}
print("\nDictionary Methods:")
print("Items (key-value pairs):", marks.items())
print("Keys:", marks.keys())
print("Values:", marks.values())

# Update dictionary with new key-value pair
marks.update({'Ravi':90})
print("after update:",marks)

# Update with another dictionary
new_dict = {'Ankit':88}
marks.update(new_dict)
print("After merging new dictionary:", marks)

# Using get() method (returns None if key doesn't exist)
print("Get 'Ankit':", marks.get('Ankit'))  # Output: 95
print("Get 'Unknown':", marks.get('Unknown'))  # Output: None
# print(marks['Unknown'])  # This would raise an error

# Set Examples
print("\n=== Set Examples ===")

# Creating a set
my_set = {1, 2, 3, 4}
print("Initial set:", my_set)

# Creating a set from a list
my_set2 = set([1, 2, 3, 4])
print("Set from list:", my_set2)

# Empty set (Note: {} creates empty dictionary, not set)
empty_set = set()
print("Empty set:", empty_set)

# Adding elements to a set
my_set.add(5)
print("After adding 5:", my_set)

# Adding different types (sets can store mixed types)
my_set.add('19')
print("After adding '19':", my_set)

# Sets can contain tuples (hashable)
my_set.add((6, 7))
print("After adding tuple (6, 7):", my_set)

# Sets cannot contain lists or dictionaries (unhashable)
# my_set.add([1, 2])  # This would raise an error
# my_set.add({'key': 'value'})  # This would raise an error

# Set methods
s = {1, 2, 3}
print("\nSet Methods:")
print("Length of set:", len(s))

# Remove element
s.remove(2)
print("After remove(2):", s)

# Discard element (no error if element doesn't exist)
s.discard(10)  # No error even though 10 isn't in the set
print("After discard(10):", s)

# Union of sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print("Union of set1 and set2:", union_set)

# Intersection of sets
intersection_set = set1.intersection(set2)
print("Intersection of set1 and set2:", intersection_set)

# Clear set
s.clear()
print("After clear():", s)

