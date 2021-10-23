x = int(input("Enter the number of numbers you want to add: "))
i, sum = 0, 0
while (i < x):
    y = int(input("Enter numbers to add: "))
    if(y < 0):
        print("Negative detected = Loop terminated")
        break
    else:
        sum = sum + y
    i = i + 1
else:
    print("Total sum is ", sum)