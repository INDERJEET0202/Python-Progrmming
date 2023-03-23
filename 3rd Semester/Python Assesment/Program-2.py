# Write a Python Program to replace last value of each tuple with 100 in list.
# Sample List : [(1,2,3), (4,5,6), (7,8,9)]
# Expected Output : [(1,2,100), (4,5,100), (7,8,100)]


input = input("Enter list in given format: ") #Enter list in given format
list = [] #empty list
for i in input.split('),('): #splitting the input string
    i = i.replace(')','').replace('(','') #removing ) and (
    list.append(tuple(i.split(','))) #converting string to tuple
print([t[:-1] + (100,) for t in list]) #replacing last value of each tuple with 100

#---------------------------------------

word_list = []
for i in input("Sample List : ").split(') , ('):
    i = i.replace(')','').replace('(','')
    word_list.append(tuple(i.split(',')))
    for j in range(0, len(word_list)):
        word_list[j] = tuple(map(int , word_list[j]))  

print([t[:-1] + (100,) for t in word_list])

