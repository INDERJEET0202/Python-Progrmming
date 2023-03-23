# Write a python program to sort (ascending and descending) a dictionary by value without using any inbuilt method or modules.

dict = {'a': 17, 'b': 2, 'c': 23, 'd': 6, 'e': 59}
print(sorted(dict.items(), key=lambda x: x[1]))
print(sorted(dict.items(), key=lambda x: x[1], reverse=True))