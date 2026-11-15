#LISTS     [ORDERED, MUTABLE]
'''fruits = ["apple", "banana", "mango"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
print(fruits)
print(numbers)
print(mixed)'''
#Accessing List Elements:
'''fruits = ["apple", "banana", "mango"]
print(fruits[0])      # apple
print(fruits[-1])     # mango (last element)'''
#List Operations:
'''Operation	      Example	               Description
Append	       list.append(item)	       Adds an item at the end
Insert	       list.insert(index, item)	   Adds at specific index
Remove	       list.remove(item)	       Removes first matching item
Pop	           list.pop()	               Removes and returns last item
Index	       list.index(item)	           Returns index of item
Count	       list.count(item)  	       Counts item occurrences
Sort	       list.sort()	               Sorts the list
Reverse	       list.reverse()	           Reverses the list
Clear	       list.clear()	               Empties the list'''
#Append – Adds an item at the end
'''my_list = [10, 20, 30, 40]
my_list.append(50)
print(my_list)'''    # [10, 20, 30, 40, 50]
#Extend - It will add list of elements as elements
'''my_list = [10, 20, 30, 40]
my_list.extend([100, 200, 300])
print(my_list)'''
#Insert – Adds item at specific index
'''my_list = [10, 20, 30, 40]
my_list.insert(2, 25)
print(my_list)'''    # [10, 20, 25, 30, 40, 50]
#Remove – Removes first matching item
'''my_list = [10, 20, 30, 40]
my_list.remove(30)
print(my_list)'''    # [10, 20, 25, 40, 50]
#Pop – Removes and returns last item
'''my_list = [10, 20, 30, 40]
last_item = my_list.pop()
print(last_item)  # 50
print(my_list)'''    # [10, 20, 25, 40]
#Index – Returns index of the item
'''my_list = [10, 20, 30, 40]
index = my_list.index(20)
print(index)'''     # 1
#Count – Counts how many times item appears
'''my_list = [10, 20, 30, 40]
count = my_list.count(20)
print(count)'''      # 1
#Sort – Sorts list in ascending order
'''my_list = [40, 10, 30, 20]
my_list.sort()
print(my_list)'''    # [10, 20, 30, 40]
#Reverse – Reverses the order of list
'''my_list = [10, 20, 30, 40]
my_list.reverse()
print(my_list)'''    # [40, 30, 20, 10]
#Clear – Empties the entire list
'''my_list = [10, 20, 30, 40]
my_list.clear()
print(my_list)'''    # []
# del() - Deletes the Entire list
'''l = [10, 20, 30, 40]
del l'''

#List Slicing:
'''numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])'''   # [20, 30, 40]

#Looping Through a List:
'''fruits = ["Apple", "Banana", "Cherry"]
for fruit in fruits:
    print(fruit)'''

#List Comprehensions
'''squares = [num ** 2 for num in [1,2,3,4,5]]
print(squares)'''   #[1, 4, 9, 16, 25]
#Add 1 to each number:
'''nums = [1, 2, 3]
result = [x + 1 for x in nums]
print(result)'''    # [2, 3, 4]
#Convert names to uppercase:
'''names = ["pavi", "sri", "moni"]
upper = [name.upper() for name in names]
print(upper)'''     # ['PAVI', 'SRI', 'MONI']
#Get only even numbers:
'''nums = [1, 2, 3, 4, 5]
evens = [x for x in nums if x % 2 == 0]
print(evens)'''     # [2, 4]
#Even or Odd:
'''nums = [1, 2, 3]
result = ["Even" if x % 2 == 0 else "Odd" for x in nums]
print(result)'''    # ['Odd', 'Even', 'Odd']

#TUPLES     (ORDERED, IMMUTABLE)
# Creating a tuple
'''my_tuple = (10, 20, 30)
print(my_tuple)'''
# Tuple with mixed data types
'''mixed_tuple = ("apple", 1, True, 3.5)
print(mixed_tuple)'''
# Tuple with one item (must include a comma)
'''single_item = (5,)
print(single_item)'''
# Without parenthesis (optional)
'''another_tuple = 1, 2, 3
print(another_tuple)'''

#Accessing Elements:
'''my_tuple = (10,20,30)
print(my_tuple[0])   # Output: 10
print(my_tuple[-1])  # Output: 30 (last element)'''

#Common Tuple Operations:
# Length
'''my_tuple = (10,20,30)
print(len(my_tuple))'''  # Output: 3
# Concatenation
'''my_tuple = (10,20,30)
new_tuple = my_tuple + (40, 50)   
print(new_tuple)'''    #output: (10, 20, 30, 40, 50)
# Repetition
'''my_tuple = (10,20,30)
repeat = my_tuple * 2  
print(repeat)'''     # Output: (10, 20, 30, 10, 20, 30)
# Membership Test
'''my_tuple = (10,20,30)
20 in my_tuple  
print(True)'''     # Output: True
# Slicing
'''my_tuple = (10,20,30)
print(my_tuple[1:])'''  # Output: (20, 30)

#Tuple Methods
#count()
'''t = (1, 2, 2, 3, 2, 4)
print(t.count(2))'''  # Output: 3
#index()
'''t = (10, 20, 30, 20)
print(t.index(20))'''  # Output: 1



# Lists
'''lst = []
lst1 = list()
print(type(lst), type(lst1))'''

#Append(element)
'''lst.append(10)
print(lst)
lst.append(20)
lst.append(30)
lst.append(40)
lst.append(50)
print(lst)
lst.append([1, 2, 3])
print(lst)'''
#Extend(multiple elements)
'''lst.extend([1, 2, 3, 4])
print(lst)'''
#Insert(position, element)
'''lst.insert(0, 100)
print(lst)'''
#Removing the elements from the list
#remove(element)
'''lst.remove(100)
print(lst)'''
#lst.remove(100) --- To overcome the error we use this membership operator
'''element = 100
if element in lst:
    lst.remove(element)
print("No element")'''
# sort() - Sorting in ascending order and descending order
'''l = [5, 4, 2, 1, 2]
l.sort()
print(l)
l.sort(reverse = True)
print(l)
# sorted()
l2 = sorted(l)
print(l)
print(l2)'''

# Shallow copy
'''import copy
l1 = [10, 20, 30, [1, 2]]
l2 = copy.copy(l1)
print(l1)
print(l2)
l1[0] = 100
print(l1)
print(l2)
l1[3][1] = 1000
print(l1)
print(l2)'''

# Deep copy
'''import copy
l1 = [10, 20, 30, [1, 2]]
l2 = copy.deepcopy(l1)
print(l1)
print(l2)
l1[0] = 100
print(l1)
print(l2)
l1[3][1] = 1000
print(l1)
print(l2)'''