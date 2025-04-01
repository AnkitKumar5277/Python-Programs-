# Python Program to find the factors of a number
# This function computes the factor of the argument passed
def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)
num = 320
print_factors(num)
# The factors of 320 are:
# 1
# 2
# 4
# 5
# 8
# 10
# 16
# 20
# 32
# 40
# 64
# 80
# 160
# 320

# This function adds two numbers
def add(x, y):
    return x + y
# This function subtracts two numbers
def subtract(x, y):
    return x - y
# This function multiplies two numbers
def multiply(x, y):
    return x * y
# This function divides two numbers
def divide(x, y):
    return x / y
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")
    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")
       # ouput

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


