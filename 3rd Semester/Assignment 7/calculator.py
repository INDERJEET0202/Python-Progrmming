#Function for summation of two numbers
def summation(a, b):
    return a + b

#Function for subtraction
def subtraction(a ,b):
    return a - b

#Function for multiplication
def multiplication(a, b):
    return a * b

#Function for division
def division(a, b):
    return a / b

print("Select operation.\n 1 - Summation\n 2 - Subtraction\n 3 - Multiplication\n 4 - Division")
choice = int(input('Enter your choice: '))
if(choice == 1):
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(summation(a, b))
elif(choice == 2):
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(subtraction(a, b))
elif(choice == 3):
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(multiplication(a, b))
elif(choice == 4):
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(division(a, b))
else:
    print("Invalid choice")