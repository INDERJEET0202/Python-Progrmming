# Decimal to binary conversion using recursion

def decToBin(num):
    if(num == 0):
        return 0

    rem = num % 2
    return rem + 10 * decToBin(num//2)

num = int(input("Enter your number: "))
print(decToBin(num))