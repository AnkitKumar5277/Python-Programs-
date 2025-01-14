# Write a function to merge two dictionaries.
# Return the merged dictionary.
# For example, for inputs {'a': 1, 'b': 2} and {'c': 3, 'd': 4}, the output should be {'a': 1, 'b': 2, 'c': 3, 'd': 4}.
def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged = merge_dictionaries(dict1, dict2)
print(merged)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
