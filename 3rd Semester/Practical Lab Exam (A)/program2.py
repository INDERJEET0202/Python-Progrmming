from collections import Counter

# tup = tuple(map(input().split))
tup = tuple((input().split()))
dict = Counter(tup)
# print(dict)
for key, value in dict.items():
    print(f"{key} occurred {value}")
    print()

for key, value in dict.items():
    if value > 1:
        print(f"{key} repeated {value}")

# Write a python program to find the repeated elements in a tuple without using any inbuilt method or modules.

tupe = tuple(input().split())
l = []
for i in range(len(tupe)):
    for j in range(i+1, len(tupe)):
        if tupe[i] == tupe[j]:
            l.append(tupe[i])
print(l)