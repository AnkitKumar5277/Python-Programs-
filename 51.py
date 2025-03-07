# Python Program to Flatten a Nested List
# Example 1: Using List Comprehension
my_list = [[1],[2,3],[4,5,6,7]]
flat_list = [num for sublist in my_list for num in sublist]
print(flat_list)
# [1, 2, 3, 4, 5, 6, 7]

# Example 2: Using Nested for Loops (non pythonic way)
my_list = [[1],[2,3],[4,5,6,7]]
flat_list[]
for sublist in my_list:
  for num in sublist:
    flat_list.append(num)
print(flat_list)
# [1, 2, 3, 4, 5, 6, 7]


