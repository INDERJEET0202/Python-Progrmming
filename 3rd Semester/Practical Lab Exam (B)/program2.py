# Decimal to binary conversion using recursion

def decToBin(num):
    if(num == 0):
        return 0

    rem = num % 2
    return rem + 10 * decToBin(num//2)

num = int(input("Enter your number: "))
print(decToBin(num))


def convertToBinary(n):
   if n > 1:
       convertToBinary(n//2)
   print(n % 2,end = '')
dec = int(input("Enter the decimal number : "))
print(f"The binary form of {dec} is :" ,end=' ')
convertToBinary(dec)