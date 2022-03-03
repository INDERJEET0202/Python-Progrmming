num1 = int(input("Enter 1st number:- "))
num2 = int(input("Enter 2nd number:- "))

if num1 % 2 != 0:
    num1 = (num1 + 1)
    # print (num1)
else:
    num1 = num1
    # print (num1)
for x in range (num1, num2+1, 2):
    print(x)






# start = int(input("Enter the start of range: "))
# end = int(input("Enter the end of range: "))
  
# for num in range(start, end + 1):
      
#     if num % 2 == 0:
#         print(num, end = " ")
        