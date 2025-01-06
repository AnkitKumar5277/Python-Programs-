# Python Program to Sort Words in Alphabetic Order
my_str = "Hello this Is an Example With cased letters"
words = [word.lower() for word in in my_str.split()]
words.sort()
print("the sorted words are:")
for word in words:
  print(word)
  
