# Nested Loops
# Loop inside another loop
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