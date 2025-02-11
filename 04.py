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
