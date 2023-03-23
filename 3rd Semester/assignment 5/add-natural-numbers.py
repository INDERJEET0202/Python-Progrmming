# 1. Program to add natural numbers up to 
# sum = 1+2+3+...+n


n = int(input("Enter n: "))
i = 0
sum = 0
while i < n:
    i = i + 1
    sum = sum + i
print("Sum of first %d natural numbers is %d" %(n,sum))
