# Generators

l1 = [num for num in range(1, 11)]
l2 = [num for num in range(1, 11)]

# zip
my_zipped_generator = zip(l1, l2)
for item in my_zipped_generator:
    print(item)


# print(next(my_zipped_generator))
# print(next(my_zipped_generator))
# print(next(my_zipped_generator))
# print(next(my_zipped_generator))
# print(next(my_zipped_generator))
# print(next(my_zipped_generator))
# print(next(my_zipped_generator))
# print(next(my_zipped_generator))
# print(next(my_zipped_generator))
# print(next(my_zipped_generator))

# print(list(my_zipped_generator))


# map
my_cubed_inits = map(lambda x: x**3, l1)
print(list(my_cubed_inits))