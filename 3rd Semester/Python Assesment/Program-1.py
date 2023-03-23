# Write a Python program to count the number of strings where length is 2 or more and the first and last character are same from a given list of string.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

str_list = []
print("Enter the number of strings you want to enter: ")
n = int(input())
for i in range(n):
    print("Enter string: ")
    str_list.append(input())
count = 0
for i in str_list:
    if len(i) >= 2 and i[0] == i[-1]:
        count += 1
print(count)