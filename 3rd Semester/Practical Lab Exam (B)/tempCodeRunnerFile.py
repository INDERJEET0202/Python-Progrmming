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
print(f"Length of item is {len(tuple)} and index is {func(item, tuple)}")