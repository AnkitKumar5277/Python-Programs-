# This program prints Hello, world!
print('Hello, world!')
print(5)

# Python Program to Add Two Numbers
# This program adds two numbers
num1 = 1.5
num2 = 6.3
sum = num1 + num2
# Display the sum
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))
# The sum of 1.5 and 6.3 is 7.8

# Store input numbers
num1 = input('Enter first number: ')
num2 = input('Enter second number: ')
# Add two numbers
sum = float(num1) + float(num2)
# Display the sum
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))
# Enter first number: 4
# Enter second number: 5
# The sum of 4 and 5 is 9.0

# 3
print('The sum is %.1f' %(float(input('Enter first number: ')) + float(input('Enter second number: '))))


# Taking kilometers input from the user
kilometers = float(input("Enter value in kilometers: "))
conv_fac = 0.621371
miles = kilometers * conv_fac
print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))

celsius = float(input("Enter: ") 
fahrenheit = (celsius * 1.8) + 32
print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(celsius,fahrenheit))
# output
# 37.5 degree Celsius is equal to 99.5 degree Fahrenheit
# formula
# celsius = (fahrenheit - 32) / 1.8

# Program to generate a random number between 0 and 9
# importing the random module
import random 
print(random.randint(0,9))  #random.randint(a,b)
