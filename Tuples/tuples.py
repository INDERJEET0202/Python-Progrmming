#Tuples are unchangeable / immutable
#Tuples cannot be changed once created
t = ("apple", "orange")
print(t)
print(len(t))

a = ("app", )
type(a)

b = ("abc", 3, True, "m")
print(b)
print(b[1])  #3
print(b[-1]) #negative indexing "m"
type(b)

#Range of indexes
thistuple = ("apple", "orange", "banana", "cherry", "kiwi", "melon", "mango")
print(thistuple[2:5]) #banana, cherry, kiwi
print(thistuple[:4]) #apple, orange, banana, cherry
print(thistuple[2:]) #banana, cherry, kiwi, melon, mango
print(thistuple[-4:-1]) #cherry, kiwi, melon

if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")
else:
    print("No, 'apple' is not in the fruits tuple")

#Convert tuple to list
thistuple = ("apple", "orange", "banana", "cherry", "kiwi", "melon", "mango")
thislist = list(thistuple) #Changing the tuple to list.
print(thislist)
thislist[3] = "you" #Changing the list
thislist.append("python") #Adding new element to the list
thislist.remove("orange") #Removing element from the list
thistuple = tuple(thislist) #Changing the list to tuple.
print(thistuple)
del thistuple #deletion of tuple

#Adding two tuples
tuple1 = ("a", "b", "c") 
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2 #Adding two tuples
print(tuple3) 

#Packing tuples
x = ("apple", "banana", "cherry", "python")  
(green, yellow, *red) = x #Unpacking the tuple
(green, *yellow, red) = x
print(green)
print(yellow)
print(red)

#Looping through a tuple
fruit = ("apple", "banana", "cherry")
for x in fruit:
    print(x)

#range in tuple
fruit = ("apple", "banana", "cherry")
for x in range(len(fruit)):
    print(x)

#Using while loop
fruit = ("apple", "banana", "cherry")
i = 0
while i < len(fruit):
    print(fruit[i])
    i += 1

#Tuple methods
