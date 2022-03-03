first_tuple = ('abcd' , 147 , 2.43, 'Tom' , 74.8)
# Print complete tuple.
print(first_tuple)
# Print the first element of tuple
print(first_tuple[0])
# Print elements starting from 2nd till 3rd
print(first_tuple[1:3])
# Print elements starting from 3rd element
print(first_tuple[2:])
# Print the total length of the tuple
print(len(first_tuple))


small_tuple = (222 , 'Tom')
print(len(small_tuple))
# Print complete tuple .
print(small_tuple)
# Print tuple 2 times.
print(small_tuple * 2)
# Print concatenated two tuple.
print(small_tuple + first_tuple)

# Program to Subtract a Tuple from Another Tuple

# Methord 1
final_tuple = ()
for i in first_tuple:
    if i not in small_tuple:
        final_tuple += (i,)
print(final_tuple)

# Methord 2
first_list = list(first_tuple)
small_list = list(small_tuple)
final_list = []
for i in first_list:
    if i not in small_list:
        final_list.append(i)
final_tuple = tuple(final_list)
print(final_tuple)