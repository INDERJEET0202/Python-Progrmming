# list1 = [1,2,3,4,5,6]
# list2 = [12,11,10,9,8,7]

def common(list1, list2):
    result = False
    for x in list1:
        for y in list2:
            if x == y:
                result = True
    return result

list1 = []
elements = int(input("Enter number of elements you want in list 1 "))
i = 0
while(i < elements):
    x = (input("Enter number to append: "))
    list1.append(x)
    i = i+1


list2 = []
elements = int(input("Enter number of elements you want in list 2 "))
j = 0
while(j < elements):
    y = (input("Enter number to append: "))
    list2.append(y)
    j = j+1

print(list1)
print(list2)

if(common(list1, list2)):
    print("True")
else:
    print("False")


# Method 2

# def common_list(l1,l2):
#     for i in set(l1):
#         if i in l2:
#             return True
#     return False

# l1=input("Enter list 1:").split()
# l2=input("Enter list 2:").split()
# print("result is: ",common_list(l1, l2))