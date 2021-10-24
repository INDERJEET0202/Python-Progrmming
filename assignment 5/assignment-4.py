i, sum = 1, 0
num_of_num = int(input("Enter number of numbers you want to add: "))
while (i <= num_of_num):
    num = int(input("Enter number %d: " %(i)))
    if(num < 0):
        pass
    else:
        sum = sum + num
    i = i + 1
print("Sum of all positive numbers are: ", sum)