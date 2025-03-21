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

# Example 5: Inverted half pyramid using numbers
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1
rows = int(input("enter number of rows:"))
for i in range(rows, 0, -1):
  for j in range(1, i+1):
    print(j, end=" ")

  print()
  

# Python Program to Check Whether a String is Palindrome or Not
my_str='aIbohPhoBiA'
my_str = my_str.casefold()
rev_str = reversed(my_str)
if list(my_str) == list(rev_str):
  print("the string is a palindrom.")
else:
  print("the string is not a palindrome")
# The string is a palindrome.


# Example 10: Floyd's Triangle
# 1
# 2 3
# 4 5 6
# 7 8 9 10
rows = int(input("enter: ")
number = 1
for i in range(1, rows+1):
  for j in range(1, i+1):
    print(number, end= " ")
    number += 1
  print()
