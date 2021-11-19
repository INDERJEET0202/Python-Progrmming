# Function to find factorial of a number
def Factorial(a):
    fact = 1
    for i in range(1, a+1):
        fact = fact * i
    return fact

number = int(input("Enter the number: "))
print("Factorial of {} is {}".format(number, Factorial(number)))