# SCOPE            - LEGB
# 1 Local Scope
'''def f1(x, y):
    a = 5
    print(a)
    return a
f1(10, 2)'''

# 2 Global Scope
'''x = 10
def f2():
    print(x)'''

# 3 Enclosed Scope
'''def f3():
    x = 10
    def f4():
        y = 20
        print(x)
        print(y)
    f4()
f3()'''

# 4 Built - in Scope
# print(), input(), len(), sum(), max(), min(), range() and type()
'''def display():
    numbers = [10, 20, 30, 40]
    print(len(numbers))
    print(max(numbers))
    print(min(numbers))
    print(sum(numbers))
display()'''

# Global Keyword
'''x = 10
def f():
    global x
    print(x)
    x = x + 1
f()
print(x)'''

# Non-Local Keyword
def f1():
    x = 10
    def f2():
        nonlocal x
        y = 100
        print(x)
        x = x + 10
        print(x)
        print(y)
    f2()
f1()

# Pass by Object Reference
'''def f(x):              # 140732003767832, 140732003767832, 100
    print(id(x))
    print(x)
a = 100
print(id(a))
f(a)'''
# Immutable Data Type
'''def f(x):             # 140732003767832, 140732003767832, 140732003768152, 110
    print(id(x))
    x = x + 10
    print(id(x))
    print(x)
a = 100
print(id(a))
f(a)'''
# Mutable Data Type
'''def f(x):            # Same memory - 2681462904960, 2681462904960, 2681462904960
    print(id(x))
    x.append(100)
    print(id(x))
a = [10, 20, 30, 40]
print(id(a))
f(a)'''

'''def f(x):           # Different Memory - 2699754068096, 2699754068096, 2699754066176
    print(id(x))
    x = [10, 20, 30, 40]
    print(id(x))
a = [10, 20, 30, 40]
print(id(a))
f(a)'''

# RECURSION
# syntax
'''def function():
    if condition:
        return
    function()
function()'''
# Factorial using Recursion
'''def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
print(factorial(5))'''   # 120

# Adding N natural numbers using Recursion
'''def n_natural_numbers(n):
    if n == 1:
        return 1
    return n + n_natural_numbers(n - 1)
print(n_natural_numbers(5))'''   # 15

# Adding even numbers using Recursion
'''def even_numbers(n):
    if n == 2:
        return 2
    return n + even_numbers(n - 2)
print(even_numbers(10))'''

# Adding odd numbers using Recursion
'''def odd_numbers(n):
    if n == 1:
        return 1
    return n + odd_numbers(n - 2)
print(odd_numbers(9))'''

# Finding even or odd in N natural numbers
'''def n_natural_sum(n):
    if n % 2 == 0:
        if n == 2:
            return 2
        return n + n_natural_sum(n - 2)
    else:
        if n == 1:
            return 1
        return n + n_natural_sum(n - 2)
print(n_natural_sum(10))'''