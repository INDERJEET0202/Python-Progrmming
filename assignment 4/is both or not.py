N = int(input("Enter N "))
if (N % 5 == 0 or N % 11 == 0):
    print('"ONE"')
elif(N % 5 == 0 and N % 11 == 0):
    print('"BOTH"')
else:
    print('"NONE"')