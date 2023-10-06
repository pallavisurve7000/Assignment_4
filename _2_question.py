# Write a Python program to triple all numbers of a given list of integers. Use Python map.

def triple_number(n):
    return 3 * n
numbers = []
size = int(input("Enter the size of list :"))
for i in range(size):
    num = int(input(f"Enter {i+1} value :"))
    numbers.append(num)
tripled_numbers = list(map(triple_number,numbers))
print("Original numbers :",numbers)
print("Tripled numbers :",tripled_numbers)