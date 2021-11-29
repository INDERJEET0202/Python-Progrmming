first_list = ['abcd' , 147 , 2.43, 'Tom' , 74.8]
#Printing the list
print(first_list)
# Print the first element of list
print(first_list[0])
# Print elements starting from 2nd till 3rd
print(first_list[1:3])
# Print elements starting from 3rd element
print(first_list[2:])
# Print the total length of the list 
print(len(first_list))


small_list = [222 , 'Tom']
print(len(small_list))
# Print complete list.
print(small_list)
# Print list 2 times.
print(small_list * 2)
# Print concatenated two lists.
print(small_list + first_list)
# Program to Subtract a List from Another List
final_list = []
for i in first_list:
    if i not in small_list:
        final_list.append(i)
print(final_list)