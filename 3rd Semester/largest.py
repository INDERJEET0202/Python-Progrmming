a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))

if (a >= b) and (a >= c):
   print("The largest number is", a)
elif (b >= a) and (b >= c):
   print("The largest number is", b)
else:
   print("The largest number is", c)


   # print("a is largest") if a>b  else print("b is largest" )if a==b else print("c is largest")