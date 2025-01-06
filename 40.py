# Python Program to Remove Punctuations From a String
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
my_str = "Hello!!!, he said ---and went."
no_punct = ""
for char in my_str:
  if char not in punctuations:
    no_punct = no_punct + char
print(no_punct)
# Hello he said and went
# # output
# Union of E and N is {0, 1, 2, 3, 4, 5, 6, 8}
# Intersection of E and N is {2, 4}
# Difference of E and N is {8, 0, 6}
# Symmetric difference of E and N is {0, 1, 3, 5, 6, 8}
