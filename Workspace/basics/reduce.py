from functools import reduce

numbers = [1, 2, 3, 4, 5]

sum = reduce(lambda x, y: print(x, y), numbers)
print(sum)
