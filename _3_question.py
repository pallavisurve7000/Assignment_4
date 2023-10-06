# Write a Python program to square the elements of a list using map() function.

def square(n):
    return n ** 2
numbers = []
size = int(input("Enter size of the list :"))
for i in range(size):
    num = int(input(f"enter {i+1} value :"))
    numbers.append(num)
squared_numbers = list(map(square,numbers))
print("original numbers :",numbers)
print("squared numbers :",squared_numbers)