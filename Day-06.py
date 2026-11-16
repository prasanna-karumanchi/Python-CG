# SETS AND DICTIONARIES

#SETS     {UNORDERED, MUTABLE}
# Creating a set
'''my_set = {1, 2, 3, 4}
print(my_set)'''
# Creating an empty set (MUST use set())
'''empty_set = set()
print(empty_set)'''
# Set with duplicates (duplicates will be removed)
'''dup_set = {1, 2, 2, 3}
print(dup_set)'''  # Output: {1, 2, 3}

#Set Operations
# Union
'''a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)'''  # Output: {1, 2, 3, 4, 5}
# Intersection
'''a = {1, 2, 3}
b = {3, 4, 5}
print(a & b)'''  # Output: {3}
# Difference
'''a = {1, 2, 3}
b = {3, 4, 5}
print(a - b)'''  # Output: {1, 2}
# Symmetric Difference
'''a = {1, 2, 3}
b = {3, 4, 5}
print(a ^ b)'''  # Output: {1, 2, 4, 5}

#Set methods
#add()
'''my_set = {1,2,3}
my_set.add(4)
print(my_set)'''  # Output: {1, 2, 3, 4}
#remove()
'''my_set = {1,2,3}
my_set.remove(2)
print(my_set)'''  # Output: {1, 3, 4}
#discard()
'''my_set = {1,2,3}
print(my_set.discard(10))''' # No error
#pop()
'''my_set = {1,2,3}
element = my_set.pop()
print(element)     # Random element
print(my_set)'''      # Remaining set
#clear()
'''my_set = {1,2,3}
my_set.clear()
print(my_set)'''  # Output: set()
#update(other_set)
'''c
a.update(b)
print(a)'''  # Output: {1, 2, 3, 4}
#union(other_set) or a | b
'''a = {1, 2}
b = {2, 3}
print(a.union(b))'''  # Output: {1, 2, 3}
#intersection(other_set) or a & b
'''a = {1, 2}
b = {2, 3}
print(a.intersection(b))'''  # Output: {2}
#difference(other_set) or a - b
'''a = {1, 2}
b = {2, 3}
print(a.difference(b))'''  # Output: {1}
#symmetric_difference(other_set) or a ^ b
'''a = {1, 2}
b = {2, 3}
print(a.symmetric_difference(b))'''  # Output: {1, 3}
#copy()
'''a = {1, 2}
b = {2, 3}
new_set = a.copy()
print(new_set)'''  # Output: {1, 2}
#issubset(other_set)
'''small = {1, 2}
big = {1, 2, 3}
print(small.issubset(big))'''  # Output: True
#issuperset(other_set)
'''small = {1, 2}
big = {1, 2, 3}
print(big.issuperset(small))'''  # Output: True
#isdisjoint(other_set)
'''x = {1, 2}
y = {3, 4}
print(x.isdisjoint(y))'''  # Output: True

#DICTIONARIES     {KEY : VALUE}
# Creating a dictionary
'''my_dict = {
    "name": "Alice",
    "age": 22,
    "city": "Hyderabad"
}
print(my_dict)'''
#Accessing Values
'''my_dict = {
    "name": "Alice",
    "age": 22,
    "city": "Hyderabad"
}
print(my_dict["name"])      # Output: Alice
print(my_dict.get("age"))'''   # Output: 22
#Modifying Values
'''my_dict = {
    "name": "Alice",
    "age": 22,
    "city": "Hyderabad"
}
my_dict["age"] = "23"
my_dict["country"] = "India" # Adds a new key-value pair
print(my_dict)'''

#Dictionary Methods     
'''student = {
    "name": "Vamsi",
    "age": 20,
    "branch": "AIML"
}'''
#get(key, default=None)
'''print(student.get("age"))'''       # Output: 20
'''print(student.get("grade"))'''     # Output: None
'''print(student.get("grade", "N/A"))'''  # Output: N/A
#keys()
'''print(student.keys())'''  # Output: dict_keys(['name', 'age', 'branch'])
#values()
'''print(student.values())'''  # Output: dict_values(['Ravi', 20, 'AIML'])
#items()
'''print(student.items())'''  # Output: dict_items([('name', 'Ravi'), ('age', 20), ('branch', 'AIML')])
#update([other_dict])
'''student.update({"age": 21, "grade": "A"})
print(student)'''  # Output: {'name': 'Ravi', 'age': 21, 'branch': 'AIML', 'grade': 'A'}
#pop(key[, default])
'''age = student.pop("age")
print(age)         # Output: 21
print(student)'''     # 'age' is removed
#pop item()
'''item = student.popitem()
print(item)'''        # Output: ('grade', 'A') (or another last item)
#clear()
'''student.clear()
print(student)'''     # Output: {}
#copy()
'''original = {"a": 1, "b": 2}
copy_dict = original.copy()
print(copy_dict)'''   # Output: {'a': 1, 'b': 2}
#setdefault(key, default=None)
'''marks = {"math": 90}
print(marks.setdefault("math", 100))     # Output: 90
print(marks.setdefault("science", 80))   # Output: 80
print(marks)'''  # Output: {'math': 90, 'science': 80}

# Counter
'''from collections import Counter
str1 = "Engineering"
result = Counter(str1)
print(result)'''



# Sets
'''s = {1, 2, 3, 5}
s1 = set()
s2 = {}
print(type(s), type(s1), type(s2))

# set methods
# add(element)
s.add(10)
print(s)
# remove(element)
s.remove(10)
print(s)
#s.remove(10)   #KeyError
#print(s)
# discard(element)
s.discard(10)   # No Error
print(s)'''

# Set Operations
'''s1 = {10, 20, 30, 40}
s2 = {40, 50, 60}
print(s1)
print(s2)
# Union()
print(s1 | s2)
print(s1.union(s2))
#print(s1[3])   # Type error because there is no indexing
# Intersection()
print(s1 & s2)
print(s1.intersection(s2))
# Difference()
print(s1 - s2)
print(s1.difference(s2))
print(s2 - s1)
print(s2.difference(s1))
# Symmetric_difference()
print(s1 ^ s2)
print(s1.symmetric_difference(s2))

s3 = {26, 45, 18, 1, 4}
s4 = {26}
# issuperset()
print(s3.issuperset(s4))
print(s4.issuperset(s3))
# issubset()
print(s3.issubset(s4))
print(s4.issubset(s3))'''

# Dictionaries
'''d = {}
d1 = dict()
d2 = {'a':1, 
      'b':2, 
      'c':3}
print(type(d), type(d1), type(d2))
print(d2['a'])
print(d2.keys())
print(d2.values())
print(d2.items())
# update()
d2['c'] = 6  
print(d2)
d2.update({'e':5})
print(d2)
d2.update(f=6)
print(d2)
# add()
d2['d'] = 4
print(d2)
# pop()
d2.pop('b')
print(d2)
#d2.pop('b')   Key error
#print(d2)
d2.pop('b', None)
print(d2)
# popitem()
d2.popitem()   # Removes the last item
print(d2)
# get method
print(d2.get('c'))
#print(d2['z'])   # Key error
print(d2.get('z', 0))
print(d2.get('a', 0))
# clear()
d2.clear()
print(d2)
# del()
del d2
print(d2)'''

# id()
'''a = 10
b = [10, 20]
d = {1:'r'}
print(id(a))
# hash()
print(hash(a))
#print(hash(b))   # hash() is used only for immutable data types
#print(hash(d))'''

# Counter
'''from collections import Counter
str = "Engineering"
result = Counter(str)
print(result)'''

# Problems
# Find the missing numbers    s1 = {10, 45, 62, 75, 43}, s2 = {45, 10, 1}
'''s1 = {10, 45, 62, 75, 43}
s2 = {45, 10, 1}
print(s1 - s2)'''
# Find the unique characters of word "Innovation"
'''word = "Innovation"
unique = set(word)
print("Unique:", unique)'''
# Create a dictionary from two lists
'''keys = ["name", "age", "city"]
values = ["prasanna", 22, "Hyderabad"]
my_dict = dict(zip(keys, values))
print(my_dict)'''
# Calculate total marks of marks = {'python': 85, 'Aptitude':78 , 'Soft skills':65 }
'''marks = {'python': 85, 'Aptitude':78 , 'Soft skills':65 }
total = 0
for i in marks:
    total = total + marks[i]
print(total)'''
