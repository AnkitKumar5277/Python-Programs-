def jpeg_res(file_path):
    # Open the image file in binary mode
    with open(file_path, 'rb') as img_file:
        # Read file content to locate resolution information
        img_file.seek(163)  # Skip to the resolution bytes
        # Read the height and width values
        a = img_file.read(2)
        height = (a[0] << 8) + a[1]
        a = img_file.read(2)
        width = (a[0] << 8) + a[1]
    print("The resolution of the image is", width, "x", height)

# Test the function with the image file name
jpeg_res("img1.jpg")

# Python Program to Display Calendar
# Program to display calendar of the given month and year
# importing calendar module
import calendar
# yy = 2014  # year
# mm = 11    # month
# To take month and year input from the user
yy = int(input("Enter year: "))
mm = int(input("Enter month: "))
# display the calendar
print(calendar.month(yy, mm))
# output
#    November 2014
# Mo Tu We Th Fr Sa Su
#              1  2
# 3  4  5  6 7  8  9
# 10 11 12 13 14 15 16
# 17 18 19 20 21 22 23
# 24 25 26 27 28 29 30

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
# Output
# 0 21
# 1 44
# 2 35
# 3 11
