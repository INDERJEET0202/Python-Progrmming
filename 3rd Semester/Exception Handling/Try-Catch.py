try:
    num = int(input("Enter a number: "))
    if(num < 0):
        raise ValueError("Number should be positive")
except ValueError as e:
    print(e)


# ------------------------------------------

try:
    n1 = int(input("Enter a number1: "))
    n2 = int(input("Enter a number2: "))
    result = n1 / n2
    print("Result: ", result)
except ValueError as e:
    print("Input Value Error: ", e)
except ZeroDivisionError as e:
    print("Zero Division Error: ", e)