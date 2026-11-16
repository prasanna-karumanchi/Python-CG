# CONDITIONAL STATEMENTS

# if statement:- Executes a block if the condition is True.
'''a = 20
if a > 18:
    print("Eligible to vote")'''
# else statement:- Adds an alternative block if the condition is False.
'''age = 15
if age > 18:
    print("Adult")
else:
    print("Minor")'''
# elif sattement:- Checks multiple conditions in sequence.
'''marks = 33
if marks >= 90:
    print("A Grade")
elif marks >= 75:
    print("B Grade")
else:
    print("C Grade")'''

# Examples
#if
'''age = int(input("Enter: "))
if age >= 18:
    print("Eligible to vote")'''

#else
'''age = int(input("Enter: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not Eligible to vote")'''

#elif
'''marks = int(input("Enter: "))
if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 50:
    print("C")
elif marks >= 35:
    print("Pass")
else:
    print("Fail")'''

#FIZZBUZZ
'''num = int(input("Enter: "))
if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")'''

#nested if
# Greatest among 3 numbers
'''a = int(input())
b = int(input())
c = int(input())'''
'''a, b, c = map(int, input().split())
if a > b:
    if a > c:
        print(a)
    else:
        print(c)
else:
    if b > c:
        print(b)
    else:
        print(c)'''
# Using if, elif and else
'''a, b, c = map(int, input().split())
if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
else:
    print(c)'''