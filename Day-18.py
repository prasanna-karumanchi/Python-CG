# List Comprehensions

# Syntax
# l = [expression for item in iterable]

# Printing list of numbers
'''nums = [10, 2, 5, 7, -2, 45, 62]
r = [x for x in nums]
print(r)'''

# Printing the characters from the string
'''name="Prasanna"
characters = [ch for ch in name]
print(characters)
            # or
upper_case = [ch .upper() for ch in name]
print(upper_case)
            # or
lower_case = [ch.lower() for ch in name]
print(lower_case)'''

#conditional statement in list comprehension

# Syntax
# l = [expression for item in iterable condition]

# Printing Even numbers
'''l = [10, 45, 76, 99, 21, 4, 3, 1, 2]
even = [x for x in l if x % 2 == 0]
print(even)'''

# Printing Odd numbers
'''l = [10, 45, 76, 99, 21, 4, 3, 1, 2]
odd = [x for x in l if x % 2 != 0]
print(odd)'''

# Printing the range of numbers
'''n = int(input("Enter a number: "))
numbers = [i for i in range(1, n + 1)]
print(numbers)'''

#Get all the even positioned elements in a tuple 
'''t=(10, 45, 76, 99, 21, 4, 3, 1, 2)
even_positioned=[t[x] for x in range(len(t)) if x % 2 == 0]
print(even_positioned)'''

#Get all the odd positioned elements in a tuple 
'''t=(10, 45, 76, 99, 21, 4, 3, 1, 2)
odd_positioned=[t[x] for x in range(len(t)) if x % 2 != 0]
print(odd_positioned)'''

#Get all the even index elements in a tuple
'''t=(10, 45, 76, 99, 21, 4, 3, 1, 2)
even_indexed=[x for x in range(len(t)) if x % 2 == 0]
print(even_indexed)'''

#Get all the odd index elements in a tuple
'''t=(10, 45, 76, 99, 21, 4, 3, 1, 2)
odd_indexed=[x for x in range(len(t)) if x % 2 != 0]
print(odd_indexed)'''

#if - else

# Checking even or odd numbers
'''numbers = [1, 4, 2, 5, 6, 4, 6, 33 ,89, 45]
even_odd = ['even' if num % 2 == 0 else 'odd' for num in numbers]
print(even_odd)''' 

#generate sqaures of the sequence from 1 to 10
'''num = 10
squares = [i ** 2 for i in range(1, num + 1)]
print(squares)'''

#length of the strings in a string 
'''l=['Python', 'code', 'program']
length = [len(i) for i in l]
print(length)'''

#extract the numbers divisible by 3 and 5
'''nums = [3, 5, 45, 15, 30, 20]
divisibility_check=[x for x in nums if x % 3 == 0 and x % 5 == 0]
print(divisibility_check)'''

#extract all the words having more than 5 characters 
'''words = ["Prasanna", "Tharuny", "Pavithra", "Muskan", "Sneha"]
characters = [ch for ch in words if len(ch) > 5]
print(characters)'''

#Get all the vowels from the given string
'''s = "comprehenssion"
v = "AEIOUaeiou"
vowels = [x for x in s if x in v]
print(vowels)
'''
#Get all the vowels from the given string
'''s = "comprehension"
v = "AEIOUaeiou"
consonants = [x for x in s if x not in v]
print(consonants)'''

#find all the prime numbers from 1 to 100
'''prime = [n for n in range(2, 101) if all(n % i != 0 for i in range(2, n))]
print(prime)'''

#another approach
'''prime_number=[n for n in range(2,101) if len([factor for factor in range(1,n+1) if n%factor==0])==2]
print(prime_number)'''

#nested loops 
'''l = [(i, j) for i in range(1, 4) for j in range(1, 4)]
print(l)'''

# Printing the numbers in Matrix order
'''matrix=[[1,2,3],[4,5,6],[7,8,9]]
# matrix[1][2]
diagonal=[matrix[i][j] for i in range(3) for j in range(len(matrix[i])) if i==j]
print(diagonal)'''

# GENERATOR

# Generator is also called as Iterator
# It is a special function which can produce the values lazily - one by one
# In function we use return so it can print all the data at a time and there is no execution after return
# But in generator we use yield so it can print the data one by one and there is execution after yield
'''def generator(x):
    yield x
    yield x + 1
    yield x + 2
result = generator(10)
print(result)
print(next(result))
print(next(result))
print(next(result))'''

# we use next to print the exact output
# We can use no.of next functions to print individual yield values
# print(next(result))
# To avoid writing multiple next() calls, we can use a for loop to retrieve all the values one by one.
'''def generator(x):
    yield x
    yield x + 1
    yield x + 2
result = generator(10)
for i in result:
    print(i)'''

# iterable
# Examples: List, Tuple, String, Set, Dictionary.
'''lst = [10, 20, 30]
for i in lst:
    print(i)'''

# iterator
'''lst = [10, 20, 30]
lst_iterator = iter(lst)
print(lst_iterator)
print(next(lst_iterator))
print(next(lst_iterator))
print(next(lst_iterator))'''