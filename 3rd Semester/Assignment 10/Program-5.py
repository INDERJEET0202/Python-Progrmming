# Write a Python Program to create a lambda Function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and print the result.


# a = int(input("Enter a number: "))
# x = lambda a: a + 15
# print("Result: " + str(x(a)))


a = int(input("Enter 1st argument: "))
b = int(input("Enter 2nd argument: "))
x = lambda a, b: a * b
print("Result " + str(x(a, b)))