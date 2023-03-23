# L = int(input("Enter L "))
# R = int(input("Enter R "))

L, R = map(int, input("Enter L and R -").split())

if(R > L):
    for x in range(L, R+1):
        if(x % 2 != 0):
            print (x, end = " ")
else:
    for x in range(R, L+1):
        if(x % 2 != 0):
            print (x, end = " ")