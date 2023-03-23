# 2 .Write a program to generate Fibonacci series upto N numbers

n = int(input("Enter N: "))
n1, n2 = 0, 1
i = 0

if n <= 0:
   print("Please enter a value greater than 0")
elif n == 1:
   print("Fibonacci sequence upto ",n,":")
   print(n1)
else:
   print("Fibonacci series:")
   while i < n:
       print(n1)
       n3 = n1 + n2
       # update values
       n1 = n2
       n2 = n3
       i = i + 1