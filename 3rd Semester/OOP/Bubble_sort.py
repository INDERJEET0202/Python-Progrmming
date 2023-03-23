# bubble sort function
# def bubble_sort(list):
#     for i in range(len(list)):
#         for j in range(len(list)-1):
#             if list[j] > list[j+1]:
#                 list[j], list[j+1] = list[j+1], list[j]
#                 print(list)
#     return list

# Efficient bubble sort function
def bubble_sort(list):
    swapped = True
    while swapped:
        print("Bubble Sort status: ", str(list))
        swapped = False
        for j in range(len(list)-1):
            if list[j] > list[j+1]:
                swapped = True
                list[j], list[j+1] = list[j+1], list[j]
    return list

elements = int(input("How many elements do you want to sort? "))
list = []
for i in range(elements):
    list.append(int(input("Enter element " + str(i+1) + ": ")))
print("Unsorted list: ", list)
print("Sorted list: ", bubble_sort(list))