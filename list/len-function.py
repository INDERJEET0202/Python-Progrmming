names = ["dog", "Cat", "moneky", "banana", "apple", "orange"]
names2 = ["python", "c", "java"]
#insert method
names.insert(2, "mouse")
names.insert(3, "mouse")
names.insert(4, "mouse")
print(names)
#remove method
names.remove("mouse")
print(names)
# print(len(names))
# print(names[2:5])
# print(names[:3])
# print(names[2:])
# print(names[-4:-1])

# if "apple" in names:
#     print("item found")

names[4] = "indrajit"
print(names)

names[1:2] = "god", "road"
print(names)

names.append("hi")
names.insert(1,"king")

names.extend(names2)
print(names)

names2.remove("python")
names.pop(4)

del names[1]
del names2

names.clear()
print(names)






























# l1 = ["banana", "apple", "orange"]
# print(type(l1))

# l2 = 123
# print(type(l2))

# l3 = [true, false]

# list = ["apple", 1, true, 30 , "not"]


# l4 = "banana", "apple", "orange"
# print(type(l4))

# list = (("apple", "not"))
# print(list[-2])
# print(list)