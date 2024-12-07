# Python Program to Check Armstrong Number
# Python program to check if the number is an Armstrong number or not
# take input from the user
num = int(input("Enter a number: "))
# initialize sum
sum = 0
# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
# Output 1
# Enter a number: 663
# 663 is not an Armstrong number
# Output 2
# Enter a number: 407
# 407 is an Armstrong number

num = 1634
# Changed num variable to string, 
# and calculated the length (number of digits)
order = len(str(num))
# initialize sum
sum = 0
# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** order
   temp //= 10
# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

#challenge
def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))
# Example usage:
number = 12345
result = sum_of_digits(number)
print(result)  # Output: 15


