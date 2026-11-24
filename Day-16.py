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

# Indirect  Recursion
# Indirect Recursion means a function calls another function, and that second function again calls the first function.
'''def f1(n):
    if n == 1:
        return
    print(n)
    return f2(n - 1)

def f2(n):
    if n == 1:
        return
    print(n)
    return f1(n - 1)
f1(10)'''