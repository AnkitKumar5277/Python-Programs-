# 2017 is not a leap year
# 1900 is a not leap year
# 2012 is a leap year
# 2000 is a leap year

# Python program to check if year is a leap year or not
year = 2000
# To get year (integer input) from the user
# year = int(input("Enter a year: "))
# divided by 100 means century year (ending with 00)
# century year divided by 400 is leap year
if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))
# not divided by 100 means not a century year
# year divided by 4 is a leap year
elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))
# if not divided by both 400 (century year) and 4 (not century year)
# year is not leap year
else:
    print("{0} is not a leap year".format(year))
# output
# 2000 is a leap year

# challenge
def count_leap_years(start_year, end_year):
    leap_years = 0
    for year in range(start_year, end_year + 1):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            leap_years += 1
    return leap_years
# Example usage
print(count_leap_years(2000, 2020))  # Output: 6
