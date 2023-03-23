A = int(input("Enter A "))
B = int(input("Enter B "))
C = int(input("Enter C "))

# if (A < B) and (B < C):
#    sec_large = B
# elif (B > C) and (C > A):
#    sec_large = C
# else:
#    sec_large = A
# print (sec_large)


# -----------------------
l = [A, B, C]
l.sort()
print(l[1])