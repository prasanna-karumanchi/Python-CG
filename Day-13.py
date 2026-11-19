# FUNCTIONS

# Adding of two numbers
'''def add(x, y):
    print(x + y)
add(10, 20)'''
        # or
'''def add(x, y):
    return x + y
result = add(10, 20)
print(result)'''

# Counting the vowels and consonants in a string
# Normal Method
'''str1 = "Project"
vowel_count, consonant_count = 0, 0
for ch in str1:
    if ch in "AEIOUaeiou":
        vowel_count += 1
    else:
        consonant_count += 1
print("Vowel Count: ", vowel_count, "Consonant Count: ", consonant_count)'''
# Using Function Method
'''def alphabet_count(str1):
    vowels_count = 0
    consonants_count = 0
    for ch in str1:
        if ch.isalpha():
            if ch in "AEIOUaeiou":
                vowels_count += 1
            else:
                consonants_count += 1
    return[vowels_count, consonants_count]
result = alphabet_count("Python Project")
print(result)'''

# Types of Functions
# Built-in Functions - print(), input(), len(), max(), min(), sum()
# User-Defined Function - def()
# 1. with parameters, with return type
'''def add1(x, y):
    return x + y
z = add1(13, 6)
print(z)'''
# 2. with parameters, without return type
'''def add2(x, y):
    print(x + y)
add2(1, 2)'''
# 3. without parameters, with return type
'''def add3():
    x = 100
    y = 200
    return x + y
z = add3()
print(z)'''
# 4. without parameters, without return type
'''def add4():   # function definition
    x = int(input())   # function
    y = int(input())   # body
    print(x + y)
add4()   # function call'''

# Using Division by using these 4 methods
# 1. with parameters, with return type
'''def div1(x, y):
    if y == 0:
        print("Division with zero can't be possible, please take another number")
    else:
        return x / y, x // y, x % y
a, b, c = div1(15, 5)
print(a, b, c)'''
# 2. with parameters, without return type
'''def div2(x, y):
    print(x // y)
div2(15, 5)'''
# 3. without parameters, with return type
'''def div3():
    x = 15
    y = 5
    return x % y
z = div3()
print(z)'''
# 4. without parameters, without return type
'''def div4():
    x = 15
    y = 5
    print(x // y)
div4()'''

# Example Problems

# 1.Find the prime numbers from 2 to 100 - nested loop
# Normal method
'''n = 100
def prime(n):
    for i in range(2, n + 1):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime == True:
            print(i)
res = prime(n)
print(res)'''
           # or
'''for prime in range(2, 101):
    count = 0
    for i in range(1, prime + 1):
        if prime % i == 0:
            count += 1
    if count == 2:
        print(prime, end = " ")'''
# Function method
'''def prime(n):
    count = 0
    for i in range(2, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False
for i in range(2, 101):
    print(i, end = " ")'''

# 2.Get all the square patterns, right-angle triangle patterns, pyramid patterns and rhombus using functions
'''def square(n):
    for i in range(n):
        for j in range(n):
            print("*", end = " ")
        print()

def hallow_square(n):
    for i in range(4):
        for j in range(4):
            if i == 0 or i == 3 or j == 0 or j == 3:
                print("*", end = " ")
            else:
                print(" ", end = " ")
        print()

def diagonal_stars(n):
    for i in range(n):
        for j in range(n):
            if i == j or (i + j) == (n - 1):
                print("*", end = " ")
            else:
                print(" ", end = " ")
        print()

def right_triangle(n):
    for i in range(1, n + 1):
        for j in range(i):
            print("*", end = " ")
        print()

def inverted_right(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print("*", end = " ")
        print()

def left_triangle(n):
    for i in range(1, n + 1):
        for j in range(n - i):
            print(" ", end = " ")
        for j in range(i):
            print("*", end = " ")
        print()

def inverted_left(n):
    for i in range(n, 0, -1):
        for j in range(n - i):
            print(" ", end = " ")
        for j in range(i):
            print("*", end = " ")
        print()

def pyramid(n):
    for i in range(1, n + 1):
        for j in range(n - i):
            print(" ", end = " ")
        for j in range(2 * i - 1):
            print("*", end = " ")
        print()

def inverted_pyramid(n):
    for i in range(n, 0, -1):
        for j in range(n - i):
            print(" ", end = " ")
        for j in range(2 * i - 1):
            print("*", end = " ")
        print()

def rhombus(n):
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end = " ")
        for j in range(2 * i + 1):
            print("*", end = " ")
        print()
    for i in range(n - 2, -1, -1):
        for j in range(n - i - 1):
            print(" ", end = " ")
        for j in range(2 * i + 1 ):
            print("*", end = " ")
        print()

n = int(input("Enter a number: "))

square(n)
hallow_square(n)
diagonal_stars(n)
right_triangle(n)
inverted_right(n)
left_triangle(n)
inverted_left(n)
pyramid(n)
inverted_pyramid(n)
rhombus(n)'''

# 3.Add all the values in the dictionary and find sum, maximum, minimum, average among all the values
# Normal method
'''d = {"a" : 100, "b" : 20, "c" : 3, "d" : 200, "e" : 30}
summ = 0
count = 0
maxi = d["a"]   # float()
mini = d["a"]
for i in d:
    summ += d[i]
    count += 1
    if d[i] > maxi:
        maxi = d[i]
    if d[i] < mini:
        mini = d[i]
print("Sum of elements: ", summ)
print("Maximum: ", maxi)
print("Minimum: ", mini)
avg = summ / count
print("Average: ", avg)'''
# Function method
'''def dictionary():
    d = {"a" : 100, "b" : 20, "c" : 3, "d" : 200, "e" : 30}
    summ = 0
    count = 0
    maxi = d["a"]   # float()
    mini = d["a"]
    for i in d:
        summ += d[i]
        count += 1
        if d[i] > maxi:
            maxi = d[i]
        if d[i] < mini:
            mini = d[i]
    print("Sum of elements: ", summ)
    print("Maximum: ", maxi)
    print("Minimum: ", mini)
    avg = summ / count
    print("Average: ", avg)
dictionary()'''

# 4.Reverse the string - "Hello"
# Normal method
'''s = "Hello"   # slicing
s = s[::-1]
print(s)'''
          # or
'''s = input("Enter a string: ")   # string concatenation
rev = " "
for i in s:
    rev = i + rev
print(rev)'''
# Function method
'''def reverse(s):
    rev = " "
    for i in s:
        rev = i + rev
    return rev
s = "Hello"
result = reverse(s)
print(result)'''
# Reverse the list
'''l = [10, 20, 30]   # or l.reverse()
rev = []
for num in l:
    rev = [num] + rev
print(rev)'''

# 5.Search the target in the given list, if target is present, return it's position otherwise return -1
# Normal method
'''l = [1, 30, 3, -56, 42]
t = 3
for i in range(len(l)):
    if l[i] == t:
        print(i)
        break
else:
    print(-1)'''
# Function method
'''def search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1
l = [10, 20, 30, 40]
target = 30
res = search(l, target)
print(res)'''