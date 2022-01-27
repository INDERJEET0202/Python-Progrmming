# Q3. Write a Python Function that takes two lists and returns True if they have at least one common Member.

def common_member(list1, list2):
    for i in list1:
        if i in list2:
            return True
    return False

def create_list():
    list = []
    x = int(input("Enter the number of elements in the list: "))
    for i in range(x):
        list.append(input("Enter element: "))
    return list

l1 = create_list()
l2 = create_list()
print(common_member(l1, l2))