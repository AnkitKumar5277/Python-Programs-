from functools import reduce

# reduce(function, iterable[, initializer])

from functools import reduce

numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, numbers)
print(result)  # Output: 15

num = [1,2,3,4,5]
result = reduce(lambda x,y: x * y, num)
print(result)

num = [3,7,2,8,5]
max = reduce(lambda x, y: x if x > y else y, num)
print(max)

num = [1,2,3,4,5]
result = reduce(lambda x, y: x+y, num, 10)
print(result)
