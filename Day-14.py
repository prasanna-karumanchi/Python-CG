#Defining and calling function
#Write a function to print a greeting
def greet():
    print("Hello! how are you?")
greet()

#Positional Arguments
'''def function(x, y):
    return x, y
print(function(10))'''   #TypeError: function() missing 1 required positional argument: 'y'
'''def function(x, y):
    return x, y
print(function(10, 20, 30))'''   #TypeError: function() takes 2 positional arguments but 3 were given
#Write a function that adds two numbers
'''def add(a, b):
    return a + b
result = add(5, 3)
print("Sum:", result)'''

#Keyword Arguments
'''def function(x, y):
    print(x)
    print(y)
print(function(10, 20, 30))'''   #TypeError: function() takes 2 positional arguments but 3 were given
#Write a function to display student details using keyword arguments
'''def student_details(name, age, grade):
    print("Name:", name)
    print("Age:", age)
    print("Grade:", grade)
student_details(name = "Prasanna", age = 20, grade = "A")'''

#Default Arguments
'''def function (x, y, z = 0):
    return x + y + z
print(function(10, 20, 30))
print(function(10, 20))'''
#Write a function with a default argument
'''def greet(name = "Guest"):
    print("Hello", name)
greet("Prasanna")
greet()'''

#Variable-Length Arguments
'''def addition(*arg):
    print(type(arg))
    summ = 0
    for num in arg:
        summ += num
    return summ
print(addition(10, 20))'''
#Using *args (any number of positional arguments)
'''def total_sum(*numbers):
    return sum(numbers)
print("Sum:", total_sum(1, 2, 3, 4, 5))'''

#Variable-length keyword arguments
'''def addition(**kwargs):
    print(type(kwargs))
    return sum(kwargs.values())
print(addition(a = 10, b = 20, c = 30))'''
#Using **kwargs (any number of keyword arguments)
'''def student_info(**details):
    for key, value in details.items():
        print(key, ":", value)
student_info(name = "Prasanna", age = 22, course = "Python")'''