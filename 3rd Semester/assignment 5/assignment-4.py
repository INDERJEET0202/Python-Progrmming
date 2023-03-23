i, sum = 1, 0
num_of_num = int(input("Enter number of numbers you want to add: "))
while (i <= num_of_num):
    num = int(input("Enter number %d: " %(i)))
    i = i + 1
    if(num < 0):
        continue
    else:
        sum = sum + num
print("Sum of all positive numbers are: ", sum)