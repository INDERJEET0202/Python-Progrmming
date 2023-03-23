upto = int(input("Enter the number upto which you want - "))
for x in range(1,upto):
	if x % 15 == 0:
		print("FizzBuzz")
		continue
	elif x % 3 == 0:	
		print("Fizz")
		continue
	elif x % 5 == 0:		
		print("Buzz")
		continue
	print(x)