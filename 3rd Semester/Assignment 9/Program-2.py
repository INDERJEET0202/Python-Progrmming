def sum_of_n_natural_numbers(n):
    sum = 0
    for x in range(0, n + 1):
        sum = sum + x
    return sum

number = int(input("Enter number - "))
result = sum_of_n_natural_numbers(number)
print(result)


# Python program to find the sum of natural using recursive function
def recur_sum(n):
   if n <= 1:
       return n
   else:
       return n + recur_sum(n-1)
num = int(input("Enter a number: "))
if num < 0:
   print("Enter a positive number")
else:
   print("The sum is",recur_sum(num))