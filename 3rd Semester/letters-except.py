# 3. Prints all letters except 'a' and 't'  

s = str(input("Enter a string: "))
i = 0

str1 = 'a'
str2 = 't'
ns = ''

# print (len(s))
# print (s[-1])
# for i in range(len(s)):
#     # print (s[i])
#     if i == str1:
#         print (s[i])
#         break

# Using loop
for x in s:
    if x != str1 and x != str2:
        ns = ns + x
print("Original string was: ", s)
print("New string is: ", ns)

# Using replace()
# ns = s.replace(str1, '').replace(str2, '')
# print("New string is: ", ns)

# Using slice()
