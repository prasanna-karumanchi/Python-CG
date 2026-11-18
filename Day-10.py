# Problems on loops
# Checking the factors of a number
'''num = int(input("Enter: "))
for factor in range(1, num+1):
    if num % factor == 0:
        print(factor)'''

# Checking the number of odd numbers
'''num = int(input("Enter: "))
count = 0
for i in range(1, num+1):
    if i % 2 != 0:
        count += 1
print(count)'''

# Prime numnbers
'''n = int(input("Enter: "))
count = 0
for i in range(1, n+1):
    if n % i == 0:
        count += 1
if count == 2:
    print("Prime")
else:
    print("Not a Prime")'''

# Perfect Numbers
'''n = int(input("Enter: "))
sum = 0
for i in range(1, n):
    if n % i == 0:
        sum += i
if sum == n:
    print("Perfect Number")
else:
    print("Not Perfect Number")'''

# Find the minimum number from the list
'''lst = [10, 26, 2, 4, 45, -3]   # print(min(lst))
mini = lst[0]   # float('inf') for infinite number
for num in lst:
    if num < mini:
        mini = num
print("Minimum number:", mini)'''

# Find the maximum number from the list
'''lst = [10, 26, 2, 4, 45, -3]   # print(max(lst))
maxi = lst[0]  
for num in lst:
    if num > maxi:
        maxi = num
print("Maximum number:", maxi)'''

# Find the sum of the list
'''lst = [1, 2, 3, 4, 5]   # print(sum(lst))
sum = 0
for num in lst:
    sum += num
print(sum)'''

# Find the len of the list
'''lst = [10, 20, 30, 40, 50]   # print(len(lst))
length = 0 
for num in lst:
    length += 1
print(length)'''