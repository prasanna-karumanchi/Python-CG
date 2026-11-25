Day-16   # LAMBDA FUNCTIONS

# Squares
'''l = [1, 2, 3, 4, 5]
squares = map(lambda x : x * x, l)
print(list(squares))'''

# Addition
'''addition = lambda x, y : x + y
print(addition(10, 20))'''

# Higher Order Functions
# filter()
'''nums = [1, 2, 3, 4, 5, 6, 26, 10]
even = filter(lambda x : x % 2 == 0, nums)
print(even)
print(list(even))'''

# map()
'''nums = [1, 2, 3, 4, 5]
squares = map(lambda x : x * x, nums)
print(squares)
print(list(squares))'''
                # or
'''nums = [1, 2, 3, 4, 5]
squares = map(lambda x : x * x, nums)
print(tuple(squares))'''

'''nums = [1, 2, 3, 4, 5, 6, 7, 8]
multiplication_by_2 = map(lambda x : x * 2, nums)
print(multiplication_by_2)
print(list(multiplication_by_2))'''

# reduce()
'''from functools import reduce
nums = [2, 5, 7, 1, 2, 6]
summation = reduce(lambda x, y : x + y, nums)
print(summation)'''

# Using lambda in a function
'''def addition(a, b):
    return a + b
print(addition(10, 20))

addition1 = lambda x, y : x + y
print(addition(10, 20))'''

# Even or Odd
'''nums = [1, 2, 3, 4, 5]
even_odd = map(lambda x : "even" if x % 2 == 0 else "odd", nums)
print(list(even_odd))'''