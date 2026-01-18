import copy

# Original list
original = [1, 2, [3, 4]]

# Shallow copy
shallow_copy = copy.copy(original)

# Deep copy
deep_copy = copy.deepcopy(original)

# Modify the nested list in the original
original[2][0] = 99

print("Original:", original)         # Output: [1, 2, [99, 4]]
print("Shallow copy:", shallow_copy) # Output: [1, 2, [99, 4]] (nested list is affected)
print("Deep copy:", deep_copy)       # Output: [1, 2, [3, 4]] (nested list is unchanged)
