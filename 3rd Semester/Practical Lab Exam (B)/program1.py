def summation(a, b):
    return a + b

def subtraction(a ,b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

x = 0
print("Select operation.\n 1 - Summation\n 2 - Subtraction\n 3 - Multiplication\n 4 - Division")
while(x == 0):
    choice = int(input('Enter your choice: '))
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    if(choice == 1):
        print(summation(a, b))
    elif(choice == 2):
        print(subtraction(a, b))
    elif(choice == 3):
        print(multiplication(a, b))
    elif(choice == 4):
        print(division(a, b))
    else:
        print("Invalid choice")
    print("Do you want to continue?\n 1 - Yes\n 2 - No")
    choice = int(input('Enter your choice: '))
    if(choice == 1):
        x = 0
    else:
        x = 1