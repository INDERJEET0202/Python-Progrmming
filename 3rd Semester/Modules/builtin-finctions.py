# abs()
# all()
# ascii()
# bool()
# dict()
# input()
# len()
# sorted()
# sort()
# capitalize()
# casefold()

import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%Y"))
print(x.strftime("%W"))
print(x.strftime("%S")) #Seconds
print(x.strftime("%A"))
print(x.strftime("%D")) 
print(x.strftime("%B")) #Month
print(x.strftime("%M")) 
print(x.strftime("%H")) #Hour


import math as m
x = min(7, 10, 9)
y = max(7, 10, 9)
print(x)
print(y)

print(pow(4, 3))

ceiling = m.ceil(1.4)
floor = m.floor(6.9)
print(ceiling)
print(floor)


from math import sqrt, pi
x = (sqrt(4))
print(x)