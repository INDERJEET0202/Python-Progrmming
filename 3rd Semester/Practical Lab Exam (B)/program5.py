# Q5. Write a Python program to find the length and index of an item of a tuple.

def func(item, tup):
    for i in range(len(tup)):
        if tup[i] == item:
            return i + 1
    return -1

tuple = ()
x = int(input("Enter the number of elements in the tuple: "))
for i in range(x):
    tuple += (input("Enter element: "),)
# print(tuple)
item = input("Enter the item to find: ")
print(f"Length of tuple is {len(tuple)} and index is {func(item, tuple)}")


# tuplex=()
# tuplex=input("Enter the tuple elements:").split()
# n=input("enter the item:")
# print(tuplex)
# try:
#   index = tuplex.index(n)
# except:print("not found")
# else:
#   print("index = ",index)
#   try:
#     print("length = ",len(tuplex[index]))
#   except: 
#     a=str(tuplex[index])
#     print("length = ",len(a))