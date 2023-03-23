# Write a Python Function to create and print a list where the values are square of numbers between 1 and 30(both included).
# Sample Output:

def square_list():
    list = []
    for i in range(1, (30 + 1)):
        list.append(i**2)
    return list
list = square_list()
print(list)