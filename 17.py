# Example 3: Using copy() and update()
d1 = {1: 'a', 2: 'b'}
d2 = {2: 'c', 4: 'd'}
d3 = d2.copy()
d3.update(d1)
print(d3)
# {2: 'b', 4: 'd', 1: 'a'}

# Python Program to Shuffle Deck of Cards
# Python program to shuffle a deck of card
# importing modules
import itertools, random
# make a deck of cards
deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))
# shuffle the cards
random.shuffle(deck)
# draw five cards
print("You got:")
for i in range(5):
   print(deck[i][0], "of", deck[i][1])
# # ouput
# You got:
# 5 of Heart
# 1 of Heart
# 8 of Spade
# 12 of Spade
# 4 of Spade

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


