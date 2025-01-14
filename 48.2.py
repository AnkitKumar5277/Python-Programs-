# Example 3: Using copy() and update()
d1 = {1: 'a', 2: 'b'}
d2 = {2: 'c', 4: 'd'}
d3 = d2.copy()
d3.update(d1)
print(d3)
# {2: 'b', 4: 'd', 1: 'a'}
