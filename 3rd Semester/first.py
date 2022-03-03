# -------- Questionss --------
# 1.	Python Program to Print Hello world!        
# 2.	Python Program to Add Two Numbers             
# 3.	Python Program to Swap Two Variables 
# 4.	Python Program to Calculate the Area of a Triangle

print ('hello world')
#--------------------------------------

a = 10
b = 5

print (a+b)
#--------------------------------------

c = 1
d = 3
# c,d = d,c (Single line swap)
print('before swap',c,d)
# print (c,d)
temp = c
c = d
d = temp
print('after swap', c,d)
# print (c,d)
#--------------------------------------

base = 10
height = 20
area = (base * height)/2
s = 'Area of Triangle is '
# print (area)
print (s + str(area))