#Python Program to Swap Two Variables

# Python program to swap two variables
x = 5
y = 10
# To take inputs from the user
#x = input('Enter value of x: ')
#y = input('Enter value of y: ')
# create a temporary variable and swap the values
temp = x
x = y
y = temp
print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))
#The value of x after swapping: 10
#The value of y after swapping: 5

#2
x = 5
y = 10
x, y = y, x
print("x =", x)
print("y =", y)

#Addition and Subtraction
x = x + y
y = x - y
x = x - y
#Multiplication and Division
x = x * y
y = x / y
x = x / y
XOR swap

#This algorithm works for integers only
x = x ^ y
y = x ^ y
x = x ^ y
