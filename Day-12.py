#PATTERNS

#Left - Angled Triangle
'''for i in range(1,6):
    print("*" * i)'''

#Inverted Left - Angled Triangle
'''for i in range(5,0,-1):
    print("*" * i)'''

#Right - Angled Triangle
'''for i in range(1,6):
    print(" " * (5 - i) + "*" * i)'''

#Inverted Right - Angled Triangle
'''for i in range(5,0,-1):
    print(" " * (5 - i) + "*" * i)'''


#Using user input() for Right - Angled Triangle
'''n = int(input())
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)'''

#Using user input() for Inverted Right - Angled Triangle
'''n = int(input())
for i in range(5,0,-1):
    print(" " * (5 - i) + "*" * i)'''

#Pyramid
'''for i in range(1,6):
    print(" " * (5 - i) + "* " * i)'''

#Inverse pyramid
'''for i in range(5,0,-1):
    print(" " * (5 - i) + "* " * i)'''

#Diamond
'''for i in range(1,6):
    print(" " * (5 - i) + "* " * i)
for i in range(4,0,-1):
    print(" " * (5 - i) + "* " * i)'''

#Half Diamond
'''for i in range(1,6):
    print("*" * i)
for i in range(5,0,-1):
    print("*" * i)'''

#full square
'''for i in range(5):
    print("* " * 5)'''

#Hallow Square
'''for i in range(5):
    for j in range(5):
        if i == 0 or i == 4 or j == 0 or j == 4:
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()'''

#Cross Pattern
'''n = 5
for i in range(n):
    for j in range(n):
        if i == j or j == n - i - 1:
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()'''

#Number Triangle
'''for i in range(5):
    for j in range(1, i + 1):
        print(j, end = " ")
    print()'''

#Alphabet Triangle
'''for i in range(65,70):
    for j in range(65, i + 1):
        print(chr(j), end = " ")
    print()'''

# Class Work

# Printing Matrix
'''n = 1
for r in range(3):
    for c in range(3):
        print(n, end = " ")
        n += 1
    print()'''

# Square of stars
'''for r in range(4):
    for c in range(4):
        print("*", end = " ")
    print()'''
       # or
'''rows = int(input("Enter no.of rows:"))
columns = int(input("Enter no.of columns:"))
for r in range(rows):
    for c in range(columns):
        print("*", end = " ")
    print()'''
     # or
'''n = 4
for i in range(4):
    print("* " * n)'''

# Hallow Square
'''for i in range(4):
    for j in range(4):
        if i == 0 or i == 3 or j == 0 or j == 3:
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()'''

# Diagonal Stars
'''n = 5
for i in range(n):
    for j in range(n):
        if i == j or (i + j) == (n - 1):
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()'''

# Same Rows
'''for i in range(1, 5):
    for j in range(1, 5):
        print(i, end = " ")
    print()'''

# same Columns
'''for i in range(1, 5):
    for j in range(1, 5):
        print(j, end = " ")
    print()'''

# Even nums in the odd rows and odd nums in the even rows
'''even = 2
odd = 1
for i in range(1, 5):
    for j in range(1, 5):
        if i % 2 == 0:
            print(odd, end = " ")
            odd += 2
        else:
            print(even, end = " ")
            even += 2
    print()'''

# Right-Angled Triangle
'''for i in range(1, 5):
    for j in range(i):
        print("*", end = " ")
    print()'''
# Inverted Right-Angled Triangle
'''n = 4
for i in range(4):
    for j in range(n - i):
        print("*", end = " ")
    print()'''
# Left-Angled Triangle
'''n = 4
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end=" ")
    for j in range(i + 1):
        print("*", end=" ")
    print()'''
# Inverted Left-Angled Triangle
'''n = 4
for i in range(n):
    for j in range(i):
        print(" ", end=" ")
    for j in range(n - i):
        print("*", end=" ")
    print()'''

# Right-Angled Triangle
# Inner loop range change
'''for i in range(1, 5):
    for j in range(i):
        print("*", end = " ")
    print()'''
# same ranges in both loops, but we need to use conditions
'''for i in range(1, 5):
    for j in range(1, 5):
        if i >= j:
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()'''

#Numbers in Right-Angled Triangle
'''n = 1
for i in range(1, 5):
    for j in range(i):
        print(n, end = " ")
        n += 1
    print()'''
             # or
'''n = 1
for i in range(1, 5):
    for j in range(1, 5):
        if i >= j:
            print(n , end = " ")
            n += 1
        else:
            print(" ", end = " ")
    print()'''

# Same columns in Right-Angled Triangle
'''for i in range(1, 5):
    for j in range(1, 5):
        if i >= j:
            print(j , end = " ")
        else:
            print(" ", end = " ")
    print()'''

# Same rows in Right-Angled Triangle
'''for i in range(1, 5):
    for j in range(1, 5):
        if i >= j:
            print(i, end=" ")
        else:
            print(" ", end=" ")
    print()'''

# Inverted Right-Angled Triangle
'''n = 4
for i in range(4):
    for j in range(n - i):
        print("*", end = " ")
    print()'''

# Numbers in Inverted Right-Angled Triangle
'''n = 4
for i in range(n):
    for j in range(n):
        if (i + j) <= (n - 1):
            print(j + 1, end=" ")
        else:
            print(" ", end=" ")
    print()'''

# Pyramid
'''n = 3
for i in range(n):
    #Spaces
    for j in range(n - i - 1):
        print(" ", end = " ")
    #Stars
    for j in range(2 * i + 1):
        print("*", end = " ")
    print()'''

# Inverted Pyramid
'''n = 3
for i in range(n):
    #Spaces
    for j in range(i):
        print(" ", end = " ")
    #Stars
    for j in range(2 * n - (2 * i + 1)):
        print("*", end = " ")
    print()'''

# Rhombus
'''n = 3
for i in range(n):
    #Spaces
    for j in range(n - i - 1):
        print(" ", end = " ")
    #Stars
    for j in range(2 * i + 1):
        print("*", end = " ")
    print()
n = n - 1
for i in range(n):
    #Spaces
    for j in range(i + 1):
        print(" ", end = " ")
    #Stars
    for j in range(2 * n - (2 * i + 1)):
        print("*", end = " ")
    print()'''
                 # or
'''n = int(input("Enter a number: "))
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
    print()'''

n = 3
for i in range(n - 2, -1, -1):
    for j in range(n - i - 1):
        print(" ", end = " ")
    for j in range(2 * i + 1 ):
        print("*", end = " ")
    print()