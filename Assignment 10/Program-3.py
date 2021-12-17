def check_list(list1):
    count_19 = 0
    count_5 = 0
    for i in list1:
        if(i == 19):
            count_19 += 1
        elif(i == 5):
            count_5 += 1
    if(count_19 == 2 and count_5 >= 3):
        print("True")
    else:
        print("False")

# list1 = [19, 19, 25, 5, 3, 5, 5, 2]
# check_list(list1)
# list2 = [19, 15, 19, 15, 5, 2, 3]
# check_list(list2)

elements = int(input("Enter number of elements: "))
list1 = []
for i in range(elements):
    list1.append(int(input("Enter element: ")))
check_list(list1)