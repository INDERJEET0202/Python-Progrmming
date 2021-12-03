def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
        
num = int(input("Enter the number of terms: "))
if num < 0:
    print("Please enter a positive number")
else:
    print("Fibonacci sequence:")
    for i in range(num):
        print(fibonacci(i))