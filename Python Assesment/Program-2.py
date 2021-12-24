# Write a Python Program to replace last value of each tuple with 100 in list.
# Sample List : [(1,2,3), (4,5,6), (7,8,9)]
# Expected Output : [(1,2,100), (4,5,100), (7,8,100)]

# function to replace last value of each tuple with 100 in list.


input = input("Enter list in given format: ")
list = []
for i in input.split('),('):
    i = i.replace(')','').replace('(','')
    list.append(tuple(i.split(',')))
print([t[:-1] + (100,) for t in list])

word_list = []
for i in input("Sample List : ").split(') , ('):
    i = i.replace(')','').replace('(','')
    word_list.append(tuple(i.split(',')))
    for j in range(0, len(word_list)):
        word_list[j] = tuple(map(int , word_list[j]))

print([t[:-1] + (100,) for t in word_list])