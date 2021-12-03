from functools import reduce

data = reduce((lambda a, b: a * b), [num for num in range(100, 1001) if num % 2 == 0])
print(data)
