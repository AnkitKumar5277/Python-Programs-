# Python Program to Access Index of a List Using for Loop

# Example 1: Using enumerate
l = [21, 44, 35, 11]
for index, val in enumerate(l):
    print(index, val)
#     # Output
# 0 21
# 1 44
# 2 35
# 3 11

# Example 2: Start the indexing with non zero value
l  = [21, 44, 35, 11]
for index, val in enumerate(l, start = 1):
    print(index, val)
# Output
# 1 21
# 2 44
# 3 35
# 4 11

# Example 3: Without using enumerate()
l = [21, 44, 35, 11]
for index in range(len(l)):
    value = l[index]
    print(index, value)

