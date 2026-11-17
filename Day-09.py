# ATM Withdrawal System
# A user tries to withdraw money from an ATM. If withdraw<balance allow it.
# Otherwise show Insufficient balance and display transaction result.
'''withdraw = int(input("Enter amount: "))
balance = 1000
if withdraw < balance:
    balance = balance - withdraw
    print("Withdraw amount:", withdraw)
    print("Balance:", balance)
else:
    print("Insufficient Balance")'''

# ATM you can only withdraw the amount 100/500/200.
'''withdraw = int(input("Enter amount: "))
balance = 1000
if (withdraw % 100 == 0) or (withdraw % 500 == 0) or (withdraw % 200 == 0):
    if withdraw < balance:
        balance = balance - withdraw
        print("Withdraw amount:", withdraw)
        print("Balance:", balance)
    else:
        print("Insufficient Balance")
else:
    print("Enter correct amount")'''

# Online Shopping Discount
# A customer shops on an online store. if total amount is 2000 or more,give 20% discount.
# Otherwise no discount.show final price message.
'''bill = float(input("Enter actual amount: "))
discount = 0
if bill > 2000:
    discount = bill * 0.2
    print(f"You are eligible for discount, your discount is {discount}")
    final_price = bill - discount 
    print(f"Your final amount is {final_price}")
else:
    print("You are not eligible for the discount")
    print(f"Your final amount is {bill}")'''

# Password Length Validation
# A system checks password length.if length is 8 or more, password accepted.
# Otherwise,rejected.Display result.
'''password = input("Enter password: ")
print(len(password))
if len(password) >= 8:
    print("Password Accepted")
else:
    print("Password Rejected, pls select the password more than 8 characters")'''

# Convert 24-Hour Format into 12-Hour Format with AM/PM.
'''hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))
if hours <= 12:
    print(f"Time is {hours} : {minutes}")
else:
    hours = hours % 12
    print(f"Time is {hours} : {minutes}")'''  

# Check Positive Even, Positive Odd, Negative Even, Negative Odd or Zero
'''n = int(input("Enter a number: "))
if n % 2 == 0 and n > 0:
    print("Positive Even")
elif n % 2 != 0 and n > 0:
    print("Positive Odd")
elif n % 2 == 0 and n < 0:
    print("Negative Even")
elif n % 2 != 0 and n < 0:
    print("Negative Odd")
else:
    print("Zero")'''
               # or
'''n = int(input("Enter a number: "))
if n > 0:
    if n % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")
elif n < 0:
    if n % 2 == 0:
        print("Negative Even")
    else:
        print("Negative Odd")
else:
    print("Zero")'''