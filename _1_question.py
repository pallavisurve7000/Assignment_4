# Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.

add_25 = lambda x:x+25
number = int(input("enter a number :"))
res = add_25(number)
print(f"The addition is {res}")
