# lambda arguments: expression

# square = lambda x: x**2
# print(square(2))

add = lambda x, y: x + y
print(add(8, 2))

nums = [1,2,3,4]
square = list(map(lambda x: x **2, nums))
print(square)

nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)

pairs = [(1, 2), (4, 1), (3, 3)]
sort = sorted(pairs, key = lambda x: x[1])
print(sort)
