# List Comprehension
# Syntax
'''list = [expression for item in iterable]'''

# Printing the numbers in the list
'''nums = [10, 2, 5, 7, -2, 45, 62]
r = [x for x in nums]
print(r)'''

# Printing the characters from the string
'''name = "Prasanna"
characters = [ch for ch in name]
print(characters)
               # or
upper_case = [ch.upper() for ch in name]
print(upper_case)
               # or
lower_case = [ch.lower() for ch in name]
print(lower_case)'''

# Conditional statements in List Comprehension
# Syntax
'''l = [expression for item in iterable condition]'''
# Printing Even Numbers
'''l = [10, 45, 76, 99, 21, 4, 3, 1, 2]
even = [num for num in l if num % 2 == 0]
print("Even Numbers:", even)'''

# Printing Odd Numbers
'''l = [10, 45, 76, 99, 21, 4, 3, 1, 2]
odd = [num for num in l if num % 2 != 0]
print("Odd Numbers:", odd)'''

# Printing the range of numbers
'''n = int(input("Enter a number: "))
numbers = [i for i in range(1, n + 1)]
print(numbers)'''

# Get all the even positioned elements in a tuple
'''t = (-2, 45, 72, 11, 1, 3, 38, 14, 61)
num = [t[i] for i in range(len(t)) if i % 2 != 0]
print(num)'''

# Get all the odd positioned elements in a tuple
'''t = (-2, 45, 72, 11, 1, 3, 38, 14, 61)
num = [t[i] for i in range(len(t)) if i % 2 == 0]
print(num)'''

# Get all the even indexing elements in a tuple
'''t = (-2, 45, 72, 11, 1, 3, 38, 14, 61)
num = [i for i in range(len(t)) if i % 2 == 0]
print(num)'''
# Get all the odd indexing elements in a tuple
'''t = (-2, 45, 72, 11, 1, 3, 38, 14, 61)
num = [i for i in range(len(t)) if i % 2 != 0]
print(num)'''

# if - else
# Syntax
'''l = ["true_expression" condition else "false_expression" for item in iterable]'''
# even or odd
'''l = [1, 2, 3, 4, 5, 6, 7, 8]
even_odd = ["even" if num % 2 == 0 else "odd" for num in l]
print(even_odd)'''

# Nested loops in List Comprehension
# Printing the range of numbers
'''l = [[i, j] for i in range(3) for j in range(3)]
print(l)'''

# Printing the equal indexed elements
'''l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix = [l[i][j] for i in range(3) for j in range(len(l[i])) if i == j]
print(matrix)'''


# Problems
# Generate squares of the sequence from 1 to 10
'''nums = [1, 2, 3, 4, 5]
squares = [x *x for x in nums]
print(squares)'''

# Find the length of every string in a list - ["Python", "code", "program"] o/p - [6, 4, 7]
'''l = ["Python", "code", "program"]
length = [len(i) for i in l]
print(length)'''

# Extract numbers divisible by 3 and 5
'''l = [3, 15, 46, 2, 40, 45]
num = [num for num in l if num % 3 == 0 and num % 5 == 0]
print(num)'''

# Extract all words having more than 5 characters - same as 2nd
'''l = ["Python", "code", "program"]
length = [len(i) for i in l if len(i) > 5]
print(length)'''

# s = "comprehension" Get all the vowels from the given string
'''s = "comprehension"
vowels = [ch for ch in s if ch in "AEIOUaeiou"]
print("Vowels:", vowels)'''

# s = "comprehension" Get all the consonants from the given string
'''s = "comprehension"
consonants = [ch for ch in s if ch not in "AEIOUaeiou"]
print("Consonants:", consonants)'''

# Find all the prime numbers from 1 to 100
