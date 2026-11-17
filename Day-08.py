# LOOPS

#Looping Statements
# for loop:- Iterates over a sequence like list, tuple, string.
'''for i in range(5):
    print(i)'''
# while loop:- Repeats code as long as a condition is True.
'''count = 1
while count < 5:
    print(count)
    count += 1'''

#Loop Control Statements
# break – Exits the loop immediately.
'''for i in range(10):
    if i == 5:
        break
    print(i)'''
# continue – Skips the current iteration.
'''for i in range(10):
    if i == 5:
        continue
    print(i)'''
# pass – Does nothing; used as a placeholder.
'''for i in range(10):
    if i == 5:
        pass
    print(i)'''


# for loop
# Printing the fruits
'''fruits = ["Apple", "Mango"]
for fruit in fruits:
    print(fruit)'''

# Printing the N natural numbers
'''n = int(input("Enter a number: "))
for num in range(1, n + 1):
    print(num)'''
                # OR
'''n = int(input("Enter a number: "))
for num in range(1, n + 1):
    print(num, end = " ")'''
                # OR
'''lst = [10, 20, 30, 40, 50]
for index in range(len(lst)):
    print(lst[index], end = " ")'''

# Printing the odd numbers
'''n = 10
for num in range(1, n + 1, 2):
    print(num)'''

# Printing the even numbers
'''n = 10
for num in range(2, 11, 2):
    print(num)'''

# Printing the characters
'''name  = "Prasanna"
for ch in name:
    print(ch)'''
            # OR
'''s = "Prasanna"
for i in range(len(s)):
    print(s[i])'''

# Printing the numbers from the list
'''l = [10, 20, 30, 40, 50]
for num in l:
    print(num)'''
              # OR
'''l = [10, 20, 30, 40, 50]
for i in range(len(l)):
    print(l[i])'''

# Printing the numbers into even list and odd list
'''even_lst = []
odd_lst = []
for i in range(1, 11):
    if i % 2 == 0:
        even_lst.append(i)
    else:
        odd_lst.append(i)
print(even_lst)
print(odd_lst)'''

# For loop with else
'''for i in range(10):
    if i == 13:
        break
    print(i, end = " ")
else:
    # print() - to print in next line
    print("Loop completed")'''

# while Loop
# Printing N natural numbers in ascending order
'''i = 1
while i <= 5:
    print(i, end = " ")
    i += 1
print()
print(i)'''

# Printing N natural numbers in descending order
'''i = 5
while i >= 1:
    print(i, end = " ")
    i -= 1'''

# while loop with else
'''i = 1
while i <= 5:
    print(i,  end = " ")
    i += 1
else:
    print("Loop completed")'''

# Jumping Statements
# break
'''for i in range(10):
    if i == 4:
        break
    print(i, end = " ")'''

# continue
'''for i in range(10):
    if i == 4:
        continue
    print(i, end = " ")'''

# pass
'''for i in range(10):
    if i == 4:
        pass
    print(i, end = " ")'''

'''if 10 % 2 == 0:
    pass'''

# Assert Method - assert will be used in testing
'''assert 10 % 2 == 0   # If we give any wrong condition then it will shows assertion error
print("Error")'''