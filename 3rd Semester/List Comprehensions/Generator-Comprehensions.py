evens = (i for i in range (100) if i % 2 == 0)
print(evens.__next__())

for items in evens:
    print(items)