def my_func(a , b, c):
    if(a == b == c):
        return (3 *(a + b + c))
    else:
        return (a + b + c)

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))

result = my_func(number1, number2, number3)
print(result)