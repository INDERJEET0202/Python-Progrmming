#Odd Even function
def odd_even(n):
    if(n % 2 == 0):
        print("Entered number is even")
    else:
        print("Entered number is odd")

number = int(input("Enter a number: "))
odd_even(number)